# Project Title
My first project in python with classes and git repository.

conda create --name python_project python=3.10
conda activate python_project

For install libraries I can use :
conda install "some library".
Install always conda libraries if there in't in conda repository use pip.
pip install "some library"

Folder structure:

myproject/
│
├── src/                       
|  |  ├── classes/
|  |       ├── __init__.py 
|  |       ├── class1.py
|  |       ├── class2.py
|  |       ├── class3.py
|  |
│  ├── main.py                 
│                  
│
├── tests/                     
│   ├── __init__.py
│   └── test_module.py         
│
├── docs/                      
│   └── index.md               
│
├── scripts/                   
│   └── setup_env.sh            
│
├── data/                       
│
├── .gitignore                  
├── LICENSE                     
├── README.md                   
├── requirements_conda.txt      
└── requirements_pip.txt  


Always finish the project to export libraries to requirements_conda.txt and requirements_pip.txt
conda list -e > requirements_conda.txt
pip freeze > requirements_pip.txt



pip install -r requirements.txt
## Introduction
This project is a Python console application designed to demonstrate effective project structuring, incorporating several fundamental software development practices. The core functionalities include interacting with users, testing user inputs, logging processes and errors, and user management (creation and validation).

## Prerequisites
Before you can run this project, you'll need the following installed:
- Python 3.8 or later
- Pip (Python package installer)

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
  git clone https://github.com/tonilogar/python_project.git

2. Navigate to the project directory:

3. Install the required dependencies:


## Usage

To run the application, execute:

Replace `main.py` with the script you want to run.

## Features

- **User Interaction**: Utilizes libraries to prompt user input and handle responses.
- **Testing**: Integrates testing libraries to verify user responses and ensure functionality correctness.
- **Logging**: Implements both process and error logging to aid in debugging and tracking application behavior.
- **User Management**: Supports creating and validating user profiles within the console application.

## Building Executables

The project is set up to be packaged into executables for Windows, Linux, and macOS. This ensures that users can run the application on any platform without needing a Python environment set up.

To build the executables, use the following commands:

- For Windows:
pyinstaller --onefile main.py

- For Linux and macOS:
pyinstaller --onefile main.py


## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your features or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

