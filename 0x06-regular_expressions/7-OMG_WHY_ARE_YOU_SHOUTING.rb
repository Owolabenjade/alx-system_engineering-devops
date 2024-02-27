#!/usr/bin/env ruby

# This script matches all uppercase letters in the input string
# and prints them out without any spaces.

# The 'scan' method finds all occurrences of the regex pattern in the argument.
# The regex pattern /[A-Z]/ matches any single uppercase letter.
# The 'join' method concatenates all matched uppercase letters into a single string.

puts ARGV[0].scan(/[A-Z]/).join
