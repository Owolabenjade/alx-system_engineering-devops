#!/usr/bin/env ruby

# The script will match a string that is exactly a 10 digit phone number

# Check if an argument is given
if ARGV.length != 1
  puts "Usage: #{$0} 'phone_number'"
  exit
end

# Regular expression pattern for a 10 digit phone number
pattern = /^\d{10}$/

# Read the argument from the command line
input_string = ARGV[0]

# Perform the regex match
match = input_string.match(pattern)

# Print the match result
puts match unless match.nil?
