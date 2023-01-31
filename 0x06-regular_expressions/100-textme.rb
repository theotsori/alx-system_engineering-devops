#!/usr/bin/env ruby

log_file = ARGV[0]

if log_file.nil?
  puts "ERROR: No log file specified."
  exit 1
end

File.open(log_file, "r") do |file|
  file.each_line do |line|
    if line =~ /from:(\S*)\s.*to:(\S*)\s.*flags:([\d:-]*)/
      puts "#{S1},#{S2},#{S3}"
    end
  end
end
