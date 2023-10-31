#!/usr/bin/env ruby
# Check if there is exactly ne command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Define your regular expression pattern here
pattern = /hbt{2,5}n/

# Match the pattern in the input text
matches = ARGV[0].scan(pattern)

# Output the matched text
puts matches.join("\n")
