AirBnB Clone - The Console
Overview
This project is aimed at building a command-line interface (CLI) for managing AirBnB objects. The CLI will allow users to create, retrieve, update, and delete various AirBnB objects such as users, states, cities, places, etc.

Getting Started
To run the AirBnB console, follow these steps:

Clone the project repository:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd <project_directory>
Run the console:

bash
Copy code
./console.py
Usage
Once the console is running, you can use the following commands:

help: Display available commands and their descriptions.
EOF: Exit the console.
quit: Exit the console.
Interactive Mode
In interactive mode, the console prompts users to input commands and displays results interactively.

Example:

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-Interactive Mode
In non-interactive mode, users can provide commands via standard input (stdin) and receive output via standard output (stdout).

Example:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
Running Tests
To run unit tests, execute the following command:

Copy code
python3 -m unittest discover tests
File Organization
The project file organization should follow the structure below:

markdown
Copy code
- console.py
- models/
  - __init__.py
  - base_model.py
  - user.py
  - state.py
  - city.py
  - place.py
- tests/
  - __init__.py
  - test_models/
    - __init__.py
    - test_base_model.py
    - test_user.py
    - test_state.py
    - test_city.py
    - test_place.py
Dependencies
Python 3.8.5
cmd module
unittest module
Contributors
Abayo Akinyi <abayo.akinyi@riarauniversity.ac.ke>
