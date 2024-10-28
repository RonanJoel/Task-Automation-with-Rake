Task Automation with Rake and Python
Project Description

This project uses Rake, a Ruby tool, along with Python and Tkinter to automate and simplify repetitive tasks in software development. It provides a graphical interface that allows users to execute tasks interactively, improving efficiency and reducing manual errors.
Key Features

    Custom Task Definitions: Allows creating specific tasks tailored to different workflows.
    Dependency Management: Ensures the ordered execution of complex tasks.
    Activity Logging: Logs all activities and errors in a file called actividad_log.txt.
    Result Exporting: Exports the results of executed tasks to a file called resultados.csv.
    Graphical Interface: Interacts with tasks through a user-friendly GUI.

Available Tasks

    rake my_tasks:example_task: Prints a message.
    rake my_tasks:create_directory: Creates a new directory called my_directory.
    rake my_tasks:cleanup: Cleans up temporary files.

Prerequisites

    Ruby (version 3.3.5 or higher)
    Rake (installed with gem install rake)
    Python (version 3.6 or higher)
    Tkinter (usually included with Python)

Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/RonanJoel/Task-Automation-with-Rake.git
cd Task-Automation-with-Rake

```

Execution

To run the application, use the following command:

```bash

python3 rake_gui.py

```

Select a task from the menu and click "Run Task".
Contribution

If you wish to contribute to this project, please follow these steps:

    Fork the repository.
    Create your branch (git checkout -b feature/new-feature).
    Make your changes and commit (git commit -m 'Add new feature').
    Push to the branch (git push origin feature/new-feature).
    Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

