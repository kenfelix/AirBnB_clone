#!/usr/bin/python3
"""This is the console module.

Contains the entry point of the command interpreter.
"""
import cmd
import shlex
import model


class HBNBCommand(cmd.Cmd):
    """The class of our HBNB project"""
    prompt = "(hbnb) "

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **",
        "missingAttr": "** attribute name missing **",
        "missingValue": "** value missing **"
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
            usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
            usage: EOF (Ctrl+d)
        """
        return True

    def emptyline(self):
        """Handles the empty line behaviour"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and print the id.
            usage: create <class_name>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            new = eval(args[0])()
            new.save()
            print(new.id)
        else:
            print(self.errors["wrongClass"])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
