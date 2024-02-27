#!/usr/bin/env ruby

# This script uses a regular expression to match strings that begin with 'h',
# followed by zero or more 'b's, and end with 'ttn'.

# The pattern /hbt*n/ is used to match the required strings.
# The 'scan' method searches for the pattern in the provided argument.
# The 'join' method combines the resulting array into a single string.

puts ARGV[0].scan(/hbt*n/).join if ARGV.length == 1

# To execute the script, pass a single string argument to it.
# Example: ./3-repetition_token_2.rb "hbtn hbbtn hbbbttn"
