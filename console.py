#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB_clone project command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program gracefully"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
