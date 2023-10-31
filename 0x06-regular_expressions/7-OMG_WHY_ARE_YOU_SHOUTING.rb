#!/usr/bin/env ruby
# Check if there is exactly one command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Define the regular expression pattern to match the specified cases
pattern = /[A-Z]/

# Extract capital letters from the input text
capital_letters = ARGV[0].scan(pattern).join

# Output the extracted capital letters
puts capital_letters
