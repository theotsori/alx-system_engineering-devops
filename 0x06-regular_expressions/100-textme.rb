#!/usr/bin/env ruby

log = ARGV[0]

sender = log.match(/from:(.*?)\s/)[1]
receiver = log.match(/to:(.*?)\s/)[1]
flags = log.match(/flags:(.*?)\s/)[1]

puts "#{sender},#{receiver},#{flags}"
