#!/usr/bin/python3
"""Command line to interact with the class Models """

import cmd
import shlex
import models
import ast

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


"""The class inherites from cmd.Cmd"""
class HBNBCommand(cmd.Cmd):
    """The console class"""
    prompt = "(hbnb) "

    classes = [
            "BaseModel", "Amenity", "City", "Place", "Review", "State", "User"
            ]
    
    errors = {
            "missingValue": "** value missing **",
            "missingClass": "** class name missing **",
            "wrongClass": "** class doesn't exist **",
            "missingID": "** instance id missing **",
            "wrongID": "** no instance found **",
            "missingAttr": "** attribute name missing **"
            }
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
        """Create a new instance"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            nw = eval(args[0])()
            nw.save()
            print(nw.id)
        else:
            print(self.errors["wrongClass"])

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        print(instances[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])
        

    def do_all(self, arg):
        """Print string representations of all instances."""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print([v.__str__() for v in models.storage.all().values()])
        elif args[0] in self.classes:
            print([v.__str__() for v in models.storage.all().values()
                   if type(v) is eval(args[0])])
        else:
            print(self.errors["wrongClass"]) 

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    if len(args) < 3:
                        print(self.errors["missingAttr"])
                    else:
                        if len(args) < 4:
                            print(self.errors["missingValue"])
                        else:
                            obj = models.storage.all()[key]
                            try:
                                attr_type = type(getattr(obj, args[2]))
                                args[3] = attr_type(args[3])
                            except:
                                try:
                                    args[3] = int(args[3])
                                except:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        pass

                            setattr(obj, args[2], args[3])
                            obj.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

if __name__ == "__main__":
    HBNBCommand().cmdloop()

