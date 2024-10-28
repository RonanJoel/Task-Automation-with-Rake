require 'rake'
require_relative '../lib/tasks/example_task'

Rake.application.load_rakefile

describe 'my_tasks:example_task' do
    it 'should run without errors' do
        expect { Rake::Task['my_tasks:example_task'].invoke }.not_to raise_error
    end
end
