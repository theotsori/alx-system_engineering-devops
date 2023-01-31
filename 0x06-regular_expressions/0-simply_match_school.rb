#!/usr/bin/env ruby

def match_string(string)
  result = string.scan(/School/).join
    puts result.empty? ? "" : result
end

input = ARGV[0]
match_string(input)
