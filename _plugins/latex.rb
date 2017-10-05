## Newthought tag will render anything in the tag with small caps
## Usage {% newthought Your text string here} will render a span
## YOUR TEXT STRING HERE (sort of, you know, small caps) if you are using the tufte.css file

module Jekyll
  class RenderLatexTag < Liquid::Tag

#require "shellwords"

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end


    def render(context)
      "<span class=\"latex\">L<span class=\"latex-sup\">a</span>T<span class=\"latex-sub\">e</span>X</span>"
    end
  end
end

Liquid::Template.register_tag('latex', Jekyll::RenderLatexTag)