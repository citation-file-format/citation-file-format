# coding=utf-8
import datetime
import glob
import os
import pypandoc
import shutil
import re
import frontmatter
from frontmatter.default_handlers import YAMLHandler


def conditional_sub(match):
    """
    Takes a regex match and returns a repl string, which depends on whether
    the capture group "page" for that match is empty or not. If the group
    is emtpy, it returns a Pandoc-style cite tag without page information.
    If the group is not empty, it returns a Pandoc-style cite tag with a "p."
    part followed by a whitespace and the contents of the catprure group
    "page".

    :param match: A match against a regex pattern which includes the groups
    "ref" and "page" and possibly more.
    :returns: A Pandoc-style citation tag string with included page ("p.")
    material, depending on whether the match's capture group "page" is empty
    or not.
    """
    if match.group("page"):
        return "[@" + match.group("ref") + " p. " + match.group("page") + "]"
    else:
        return "[@" + match.group("ref") + "]"


# Find all files called specifications.md, recursively
for specsfile in glob.iglob('./**/specifications.md', recursive=True):
    # Copy specs file to tmp file
    specsdir = os.path.dirname(specsfile)
    version = str(os.path.basename(specsdir))
    shutil.copy2(specsfile, specsdir + "/tmp.md")

    #################################################################
    # Replace all kramdown-specific material (e.g., Liquid tags) with
    # Pandoc-specific material where necessary (e.g., citations),
    # else remove.
    #################################################################

    with open(specsdir + "/tmp.md", "r") as f:
        contents = f.read()

        # Replace citations
        p = r"""
            (?P<cite>{%\scite\s)   # Liquid cite tag start
            (?P<ref>[\w-]+)        # Reference id, BibTeX key
            (\s-l\s(?P<page>\d+))? # Optional page number
            (?P<style>\s--style\s\./_bibliography/apa-text\.csl)?
            # Optional CSL style
            (?P<suff>\s%})         # Liquid cite tag end
            """
        pattern = re.compile(p, re.VERBOSE)
        new_contents = re.sub(pattern, conditional_sub, contents)

        # Remove "Download PDF" button
        bp = r"""
             \[\*\*Download\sPDF\*\*\]
             \({{\ssite\.baseurl\s}}/assets/pdf/cff-specifications-{{\spage\.version\s}}\.pdf\)
             {:\s\.btn\s\.btn--primary\s\.btn--large}
             """
        button_pattern = re.compile(bp, re.VERBOSE)
        new_contents = re.sub(button_pattern, "", new_contents)

        # Remove Liquid CSS style tags
        new_contents = re.sub(r"{: \.[\w-]+}", "", new_contents)

        # Remove Liquid include toc tag
        new_contents = re.sub(r"{% include toc %}", "", new_contents)

        # Replace version with real version
        new_contents = re.sub(r"{{ page.version }}", version, new_contents)

        # Replace code highlighting
        new_contents = re.sub(r"{% highlight yaml %}", "```yaml", new_contents)
        new_contents = re.sub(r"{% endhighlight %}", "```", new_contents)

        # Remove Liquid bibliography tag
        new_contents = re.sub(r"{% bibliography --cited %}", "", new_contents)

        # Replace solid circles with bullets
        new_contents = re.sub(r"●", "•", new_contents)

        # Replace string "Solid circles ("
        new_contents = re.sub(r"Solid circles \(",
                              "Bullet points (", new_contents)

        # Remove Zenodo DOI badge
        zdp = """
              \[\!\[DOI\]\(https://citation-file-format\.github\.io/assets/
              images/zenodo\.[\d]+\.svg\)\]
              \(https://doi\.org/[\d]+\.[\d]+/zenodo\.[\d]+\)
              """
        zenodo_doi_pattern = re.compile(zdp, re.VERBOSE)
        found = re.findall(zenodo_doi_pattern, new_contents)
        new_contents = re.sub(zenodo_doi_pattern, "", new_contents)

    # Write new Pandoc markdown file
    with open(specsdir + "/tmp.md", "w") as f:
        f.write(new_contents)
    output = pypandoc.convert_file(specsdir + "/tmp.md", 'markdown',
                                   outputfile=specsdir +
                                   "/cff-specifications-" +
                                   version + ".md")

    # Replace links to GitHub users using @ notation
    # Has to be done here, otherwise the first pandoc conversion simply
    # gets rid of the backslashes before the "@".
    with open(specsdir + "/cff-specifications-" + version + ".md", "r") as f:
        contents = f.read()
        new_contents = re.sub(r"\(\[@(?P<user>[\w-]+)\]",
                              "([" + r"\\@" + "\g<user>]",
                              contents)
    with open(specsdir + "/cff-specifications-" + version + ".md", "w") as f:
        f.write(new_contents)

    # Read YAML frontmatter from the original specifications.md and
    # write it to the new Pandoc markdown file
    with open(specsdir + "/tmp.md", "r") as f:
        metadata, content = frontmatter.parse(f.read())
        e = YAMLHandler().export(metadata)
    with open(specsdir + "/cff-specifications-" + version + ".md", "r") as f:
        contents = f.read()
        new_contents = "---\n" + e + "\n---\n\n" + contents
    with open(specsdir + "/cff-specifications-" + version + ".md", "w") as f:
        f.write(new_contents)

###############################################################################
# The following is not necessary when using a custom pandoc build which
# contains the fix for https://github.com/jgm/pandoc/issues/3529
###############################################################################
#    # Replace all tables with more than one column with multiline tables
#    # and make the columns equal width
#    with open(specsdir + "/cff-specifications-" + version + ".md", "r") as f:
#        # Find multiline tables
#        # ^\s\s[-]+\s+[-]+
#        lines = {}
#        separator_lines = []
#        multicol_separator = re.compile(r"^\s\s[-]+\s+[-]+")
#        multiline_headerline = re.compile(r"^\s\s[-]+\n")
#        for line_i, line in enumerate(f, 1):
#            lines[line_i] = line
#            if multicol_separator.search(line):
#                separator_lines.append(line_i)
#        # Remove those match line numbers from the list which have a line of
#        # '-' chars two lines above them, as these are multiline tables already
#        for i in separator_lines:
#            if multiline_headerline.search(lines[i - 2]):
#                separator_lines.remove(i)
#        # Now we have a definitive list of non-multiline tables via their
#        # separator line line numbers, create multiline table header and footer
#        # lines, and add whitespaces.
#        # First, copy the lines dictionary into a list for easier insertion
#        lineslist = []
#        for key, value in lines.items():
#            lineslist.insert(key, value)
#        # Insert header (and footer) lines (basically line length * "-") for
#        # all non-multiline tables
#        for line_no in separator_lines:
#            sep_line_length = len(lineslist[line_no - 1])
#            # sep_line_length - 3 (sic!) because the line break seems to count,
#            # which would lead to and off-by-one (not sure whether this is a
#            # problem for pandoc)
#            headerline_str = str((2 * " ") + ((sep_line_length - 3) * "-") +
#                                 "\n")
#            # Insert header line
#            lineslist.insert(line_no - 2, headerline_str)
#            # Insert footer line
#            for index, line in enumerate(lineslist[line_no:]):
#                real_index = index + line_no
#                if re.match(r"^\n", line):
#                    lineslist.insert(real_index, headerline_str)
#                    break
#            # Increment following separator line values by 2 (because we have
#            # added two lines to the list)
#            index = separator_lines.index(line_no)
#            for future_line in separator_lines[index + 1:]:
#                future_index = separator_lines.index(future_line)
#                separator_lines[future_index] = future_line + 2
#        # Treat adding blank lines in separate for, which is easier (also: SOC)
#        for line_no in separator_lines:
#            add_counter = 0
#            # Add blank lines after each table entry
#            skip = False
#            for index, line in enumerate(lineslist[line_no + 4:]):
#                real_index = index + line_no
#                # Until we hit the footer line:
#                if re.match(r"^[-]+\n", line):
#                    break
#                elif skip:
#                    skip = False
#                    continue
#                # Add a blank line after each line:
#                else:
#                    lineslist.insert(real_index, "\n")
#                    add_counter += 1
#                    skip = True
#            # Increment following separator line values by add_counter
#            index = separator_lines.index(line_no)
#            for future_line in separator_lines[index + 1:]:
#                future_index = separator_lines.index(future_line)
#                separator_lines[future_index] = future_line + add_counter
#        new_contents = "".join(lineslist)
#    with open(specsdir + "/cff-specifications-" + version + ".md", "w") as f:
#        f.write(new_contents)

# Build PDF
    pdoc_args = ['--pdf-engine=xelatex', '--toc', '--toc-depth=4',
                 '--bibliography=./_bibliography/references.bib',
                 '--csl=./_bibliography/ieee-with-url.csl',
                 '--metadata=date:"' +
                 datetime.date.today().strftime('%d %B %Y') + '"',
                 '--template=./template/default.latex']
    filters = ['pandoc-citeproc']
    pypandoc.convert_file(specsdir + "/cff-specifications-" + version + ".md",
                          to='pdf', extra_args=pdoc_args, filters=filters,
                          outputfile=specsdir + "/cff-specifications-" +
                          version + ".pdf")
    os.remove(specsdir + "/cff-specifications-" + version + ".md")
    os.remove(specsdir + "/tmp.md")
    shutil.move(specsdir + "/cff-specifications-" + version + ".pdf",
                "./assets/pdf/cff-specifications-" + version + ".pdf")
