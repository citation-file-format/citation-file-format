## Newthought tag will render anything in the tag with small caps
## Usage {% newthought Your text string here} will render a span
## YOUR TEXT STRING HERE (sort of, you know, small caps) if you are using the tufte.css file

module Jekyll
  class RenderEpigraphTag < Liquid::Tag

require "shellwords"

    def initialize(tag_name, text, tokens)
      super
      @text = text.shellsplit
    end


    def render(context)
      "<blockquote>
         <p class=\"epigraph\">#{@text[0]}<cite class=\"epigraph\">#{@text[1]}</cite>
</p>
          </blockquote>"
    end
  end
end

Liquid::Template.register_tag('epigraph', Jekyll::RenderEpigraphTag)