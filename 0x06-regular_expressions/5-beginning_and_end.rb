#!/usr/bin/env ruby

def match_string(string)
  if /^h.n$/ =~ string
    puts "#{string}"
  else
    puts ""
  end
end

input = ARGV[0]
match_string(input)
