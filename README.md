# holbertonschool-AirBnB_clone

## Description of the project

The AirBnB Clone project is a project with the purpose of creating a simpler version of the AirBnB website. The project has a long-term timeline and the main objective is the creation of a web application that incorporates several of its important programming concepts. At the end of this project, you will have available a web application that includes:

- A command interpreter for manipulating data, similar to a Shell. This interpreter is useful for development and debugging.
- A data storage system that can persist objects, either in a database or in files.
- A website (the front-end) that displays the final product, including static and dynamic elements.
- An API that provides a communication interface between the front-end and its data, allowing you to retrieve, create, delete, and update objects.

## Command Interpreter

The command interpreter is crucial for this project. It allows manipulate and interact data, therefore it is a valuable tool for development and debugging.

### How to Start It

To start the command interpreter, simply run the `console.py` file.

```bash
python console.py
```

### How to Use It

The command interpreter provides a set of commands an use commands create,destroy, update and show for managing objects (manipulate data).

### Examples

Here are some examples of using the command interpreter:

```bash
(hbnb) create User
(hbnb) show User 12345
(hbnb) destroy User 12345
(hbnb) all
(hbnb) update User 67890 first_name "Nany"
```

## Description of the command interpreter:

`help` (help) - displays all commands available
`create` (create <class>) - creates new object (ex. a new User, Place)
`update` (User.update `123`) - updates attribute of an object
`destroy` (User.destroy(`123`) - destroys specified object
`show` (User.show `123`) - retrieve an object from a file, a database
`all` (User.all()) - display all objects in class
`count` (User.count()) - returns count of objects in specified class
`quit` (quit) - exits

## Collaborative work (branches)

We encourage collaborative work to help organize and optimize this project so that they can manage and coordinate their efforts effectively.

## Concepts

Have the opportunity to learn various concepts and technologies:

- Unittest: Collaborate on test cases to ensure the reliability and functionality of the code.
- Serialization/Deserialization: Covert objects into serializable data and return.
- Python packages: Understand the concept of organizing code into packages.
- *args and **kwargs: Explore how to work with dynamic function arguments.
- datetime: Manipulate date and time information.

## Steps

Will be developed in multiple steps, each focusing on specific aspects of the application:

1. The Console
2. Web Static
3. MySQL Storage
4. Web Framework - Templating
5. RESTful API
6. Web Dynamic

## Structure

The project repository is organized as follows:

- `models` directory contains all classes.
- `tests` directory contains all unit tests.
- `console.py` entry point of the command interpreter.
- `models/base_model.py` is the base class for all models, containing common attributes and methods.
- `models/engine` directory contains storage classes, initially focusing on file storage.

## Storage

Persistency is a key for a web application to retain data across multiple program executions. This project employs two types of storage: file storage and database storage.

## The console

-  create your data model
-  manage (create, update, destroy, etc) objects via a console / command interpreter
-  store and persist objects to a file (JSON file)

## My SQL storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

## Web static

- learn HTML/CSS
- create the HTML of your application
- create template of each object

## Web framework - templating

- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

## RESTful API

- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

## Web dynamic

- learn JQuery
- load objects from the client side by using your own RESTful API

# JSON Serialization

To store instances of objects in a file, they are converted into JSON format standar representation.

## *args and **kwargs

These concepts allow dynamic handling of function arguments. *args represents anonymous arguments as a tuple, while **kwargs represents named arguments as a dictionary.

## datetime

The datetime module is used to manipulate date and time information in Python.

## Data Diagram

A data diagram detailing the structure and relationships of the project's data models is available to provide a clear overview of how data is organized and interconnected.

## Interactive Mode

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### AUTHORS
Hector Vazquez
Neischaly Ruidiaz
