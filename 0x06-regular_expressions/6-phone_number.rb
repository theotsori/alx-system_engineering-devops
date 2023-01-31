#!/usr/bin/env ruby

def match_string(string)
  if /\d{10}/ =~ string
    puts "#{string}"
  else
    puts ""
  end
end

input = ARGV[0]
match_string(input)
