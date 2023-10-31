#!/usr/bin/env ruby
# Check if there is exactly ne command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <phone_number>"
  exit 1
end

# Define the regular expression pattern to match the specified cases
pattern = /^\d{10}$/

# Remove non-digit characters from input
phone_number = ARGV[0].gsub(/\D/, '')

# Match the pattern in the input text
if phone_number.match?(pattern)
  puts phone_number
else
  puts ""
end
