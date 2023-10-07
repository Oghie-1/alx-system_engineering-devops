#!/usr/bin/env ruby

# Check if a log file path is provided as an argument
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Read the log file and iterate through each line
log_file = ARGV[0]
File.readlines(log_file).each do |line|
  # Use regular expressions to extract relevant information
  sender = line.match(/\[from:(.*?)\]/)&.captures&.first
  receiver = line.match(/\[to:(.*?)\]/)&.captures&.first
  flags = line.match(/\[flags:(.*?)\]/)&.captures&.first

  # Print the extracted information in the desired format
  puts "#{sender},#{receiver},#{flags}" if sender && receiver && flags
end
