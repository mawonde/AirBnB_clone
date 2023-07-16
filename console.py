<<<<<<< HEAD
#!/usr/bin/python3

"""Importing the cmd and storage modules"""
=======
"""Command line to interact with the class Models """
import ast
from shlex import split
>>>>>>> junior
import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

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
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        print(instances[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        storage.save()

    def do_all(self, arg):
        """Print string representations of all instances."""
        args = arg.split()
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return

            print(
                [
                    str(instance)
                    for instance in instances.values()
                    if type(instance).__name__ == class_name
                ]
            )

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

