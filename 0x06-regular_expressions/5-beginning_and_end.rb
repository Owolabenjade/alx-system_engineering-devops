#!/usr/bin/env ruby

# The script will match a string that starts with 'h', ends with 'n',
# and has any single character in between.

# Check if an argument is given
if ARGV.length != 1
  puts "Usage: #{$0} 'string'"
  exit
end

# Regular expression pattern
pattern = /^h.n$/

# Read the argument from the command line
input_string = ARGV[0]

# Perform the regex match
match = input_string.match(pattern)

# Print the match result
puts match unless match.nil?
