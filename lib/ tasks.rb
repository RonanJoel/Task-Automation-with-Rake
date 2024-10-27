# lib/tasks.rb

require 'rake'

namespace :my_tasks do
  desc "Task example: Print a message"
  task :example_task do
    puts "Hello, this is an automated task using Rake!"
  end

  desc "Task example: Create a directory"
  task :create_directory do
    dir_name = 'my_directory'
    Dir.mkdir(dir_name) unless Dir.exist?(dir_name)
    puts "Directory '#{dir_name}' created."
  end

  desc "Task example: Clean up temporary files"
  task :cleanup do
    temp_file = 'temp.txt'
    File.delete(temp_file) if File.exist?(temp_file)
    puts "Temporary file '#{temp_file}' cleaned up."
  end
end


