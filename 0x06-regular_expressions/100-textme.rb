#!/usr/bin/env ruby

log = ARGV[0]

sender = log[/from:(\w+|\+\d+)/, 1]
receiver = log[/to:(\w+|\+\d+)/, 1]
flags = log[/flags:([\w:]+)/, 1]

puts "#{sender},#{receiver},#{flags}"
