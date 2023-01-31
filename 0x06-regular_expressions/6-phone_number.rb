#!/usr/bin/env ruby

def match_string(string)
  if /[^0-9]/ =~ string
    puts ""
  else /[0-9]/ =~ string
    puts "#{string}"
  end
end

input = ARGV[0]
match_string(input)
