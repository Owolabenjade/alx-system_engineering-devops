#!/usr/bin/env ruby

# Your script should read lines from standard input and process them one by one.
# For each line, use regex to capture the sender, receiver, and flags fields.
# The regex will use named capture groups for easier reference.

ARGF.each_line do |line|
  data = line.match(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/)
  puts "#{data[:sender]},#{data[:receiver]},#{data[:flags]}"
end
