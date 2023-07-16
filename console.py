#!/usr/bin/python3

"""Importing the cmd and storage modules"""
import cmd
from models import storage
from models.base_model import BaseModel

"""The class inherites from cmd.Cmd"""
class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
                   print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
