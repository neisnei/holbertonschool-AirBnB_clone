#!/usr/bin/python3
"""This module defines a class HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that contains the entry point of the command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
