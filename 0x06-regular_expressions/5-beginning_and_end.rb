#!/usr/bin/env ruby
# Check if there is exactly ne command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Define the regular expression pattern to match the specified cases
pattern = /^h.n$/

# Match the pattern in the input text
if ARGV[0] =~ pattern
  puts ARGV[0]
else
  puts ""
end
