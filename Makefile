# What to compile by default?
SOURCES := cff-specifications-1.0.md
TARGETS := $(patsubst %.md,%.html,$(SOURCES)) \
			$(patsubst %.md,%.pdf,$(SOURCES)) \

STYLES := tufte-pandoc/tufte.css \
	tufte-pandoc/pandoc.css \
	tufte-pandoc/pandoc-solarized.css \
	tufte-pandoc/tufte-extra.css

.PHONY: all
all: $(TARGETS)

## Generalized rule: how to build a .html file from each .md
%.html: %.md template/tufte.html5 $(STYLES)
	mkdir -p out/css
	pandoc \
		-s \
		--katex \
		--smart \
		--section-divs \
		--from markdown+tex_math_single_backslash \
		--filter pandoc-sidenote \
		--filter pandoc-citeproc \
		--bibliography=references.bib \
		--to html5 \
		--template=./template/tufte.html5 \
		$(foreach style,$(STYLES),--css $(notdir $(style))) \
		--output $@ \
		$<
	pandoc \
		--filter pandoc-citeproc \
		--bibliography=references.bib \
		--template=./template/default.latex \
		-o cff-specifications-1.0.pdf \
		cff-specifications-1.0.md

	cp $(TARGETS) out/
	cp $(STYLES) out/css/
	mv out/cff-specifications-1.0.html out/index.html

.PHONY: clean
clean:
	rm $(TARGETS)
	rm -rf ./out