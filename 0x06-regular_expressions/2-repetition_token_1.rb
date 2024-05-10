#!/usr/bin/env ruby
Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$0} <string>"
  exit(1)
end

# Extract the argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /hb+n/

# Match the pattern against the input string and print the results
puts input_string.scan(pattern).join("\n")
