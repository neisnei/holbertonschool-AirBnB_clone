#!/usr/bin/python3
"""This module defines a class HBNBCommand"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that contains the entry point of the command interpreter."""

    prompt = '(hbnb)'

    def do_help(self, arg):
        """Help command to show the documentation of the commands."""
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "Place", "State", "City",
                         "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_instance = BaseModel()
            elif arg == "User":
                new_instance = User()
            elif arg == "Place":
                new_instance = Place()
            elif arg == "State":
                new_instance = State()
            elif arg == "City":
                new_instance = City()
            elif arg == "Amenity":
                new_instance = Amenity()
            elif arg == "Review":
                new_instance = Review()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name."""
        if arg not in ["BaseModel", "User", "Place", "State", "City",
                       "Amenity", "Review", ""]:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg:
                    if arg in key:
                        print(value)
                else:
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()

    def default(self, line):
        """Method called on an input line when the command prefix is not
        recognized"""
        if '.' in line:
            args = line.split('.')
            if 'all()' in line and args[0] in ["BaseModel", "User", "Place",
                                               "State", "City", "Amenity",
                                               "Review"]:
                self.do_all(args[0])
            elif 'count()' in line and args[0] in ["BaseModel", "User",
                                                   "Place", "State", "City",
                                                   "Amenity", "Review"]:
                self.do_count(args[0])
            elif 'show(' in line and args[0] in ["BaseModel", "User", "Place",
                                                 "State", "City", "Amenity",
                                                 "Review"]:
                id = args[1].split('(')[1].split(')')[0]
                self.do_show(args[0] + " " + id)
            elif 'destroy(' in line and args[0] in ["BaseModel", "User",
                                                    "Place", "State", "City",
                                                    "Amenity", "Review"]:
                id = args[1].split('(')[1].split(')')[0]
                self.do_destroy(args[0] + " " + id)
            elif 'update(' in line and args[0] in ["BaseModel", "User",
                                                   "Place", "State", "City",
                                                   "Amenity", "Review"]:
                params = args[1].split('(')[1].split(')')[0].split(', ')
                id = params[0]
                if '{' in params[2]:
                    attribute_dict = json.loads(', '.join(params[2:]))
                    for key, value in attribute_dict.items():
                        self.do_update(args[0] + " " + id +
                                       " " + key + " " + str(value))
                else:
                    attribute_name = params[1]
                    attribute_value = params[2]
                    self.do_update(args[0] + " " + id + " " + attribute_name +
                                   " " + attribute_value)
        else:
            super().default(line)

    def do_count(self, arg):
        """Retreives the number of instances of a class:
        <class name>.count()."""
        count = 0
        for key in storage.all():
            if arg in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
