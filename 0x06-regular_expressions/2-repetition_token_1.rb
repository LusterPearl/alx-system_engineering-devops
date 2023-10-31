#!/usr/bin/env ruby
# Check if there is exactly one command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Define the regular expression pattern to match the specified cases
pattern = /hb*t+n/

# Match the pattern in the input text
matches = ARGV[0].scan(pattern)

# Output the matched text
puts matches.join
