#!/usr/bin/env ruby

# This script uses a regular expression to match strings that begin with 'h',
# followed by zero or more characters that are not 'b', and end with 'tn'.

# The pattern /h[^b]*tn/ is used to match the required strings.
# The 'scan' method searches for the pattern in the provided argument.
# The 'join' method combines the resulting array into a single string.

puts ARGV[0].scan(/h[^b]*tn/).join if ARGV.length == 1

# To execute the script, pass a single string argument to it.
# Example: ./4-repetition_token_3.rb "htn hbtn hbbtn hbbbttn"
