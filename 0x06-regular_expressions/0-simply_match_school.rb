#!/usr/bin/env ruby
# Check if there is exactly ne command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Regular expression to match "School"
pattern = /School/

# Match the pttern in the input text
matches = ARGV[0].scan(pattern)

# Output the matched text
puts matches.join
