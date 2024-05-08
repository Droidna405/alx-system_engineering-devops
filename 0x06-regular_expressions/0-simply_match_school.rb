#!/usr/bin/env ruby

# Function to match the regular expression
def match_school(string)
  regex = /School/

  match = string.match(regex)

  puts match ? match[0] : ''
end

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
else
  match_school(ARGV[0])
end
