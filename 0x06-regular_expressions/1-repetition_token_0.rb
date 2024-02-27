#!/usr/bin/env ruby

# This script is designed to match strings that start with 'h', followed by zero or more 't's, and end with 'n'.
# It's part of a project that utilizes regular expressions with the Oniguruma library.

# ARGV[0] is the first command-line argument passed to the script.
# The scan method is used to find all occurrences that match the regular expression /hbt*n/.
# The regular expression /hbt*n/ will match any string that starts with 'hb', followed by any number of 't's (including zero), and ends with 'n'.
# The join method then combines the array elements into a single string, which is printed to the console.

puts ARGV[0].scan(/hbt*n/).join

# How to use:
# Save this script to a file named '2-repetition_token_1.rb'.
# Change the file's permissions to allow execution with the command: chmod +x 2-repetition_token_1.rb
# Run the script with a string argument like so: ./2-repetition_token_1.rb "some test string"
# If the string contains 'hb' followed by any number of 't's and ending with 'n', it will be printed; otherwise, nothing will be printed.
