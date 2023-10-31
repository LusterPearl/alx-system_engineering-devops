#!/usr/bin/env ruby
# Check if there is exactly one command-line argument

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
  exit 1
end

# Define the regular expression pattern to match and extract information
pattern = /\[from:(?<sender>[^\]]*)\] \[to:(?<receiver>[^\]]*)\] \[flags:(?<flags>[^\]]*)\]/

# Extract sender, reciever, and flags using the regular expression
matches = ARGV[0].scan(pattern)

# Output the extracted capital letters
if !matches.empty?
  sender = matches[0][0]
  reciever = matches[0][1]
  flags = matches[0][2]
  puts "#{sender},#{reciever},#{flags}"
else
  puts ""
end
