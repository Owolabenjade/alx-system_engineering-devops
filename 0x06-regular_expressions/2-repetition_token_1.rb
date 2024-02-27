#!/usr/bin/env ruby

# This script is designed to match a specific pattern using regular expressions.
# The pattern consists of strings that start with 'h', followed by one or more 'b' characters, and end with 'tn'.

# To execute the script, you need to provide a string as an argument.
# Example usage:
# ./2-repetition_token_1.rb "hbtn hbbtn hbbbtn"

# ARGV[0] refers to the first argument passed to the Ruby script.
# The 'scan' method is used to find all occurrences that match the regular expression.
# The regular expression /hb+tn/ will match any string that starts with 'h', has at least one 'b', and ends with 'tn'.
# The 'join' method is used to convert the resulting array from 'scan' into a string.

puts ARGV[0].scan(/hb+tn/).join if ARGV.length == 1

# Note: If no argument or more than one argument is provided, the script will not output anything.
