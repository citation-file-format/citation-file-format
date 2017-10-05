require 'jekyll/scholar'
require 'uri'

module MarkdownFilter
  class Markdown < BibTeX::Filter
    def apply(value)
      value.to_s.gsub(URI.regexp(['http','https','ftp'])) { |c| "[#{$&}](#{$&})" }
    end
  end
end