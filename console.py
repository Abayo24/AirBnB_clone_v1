#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program
        
        """
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        if line.strip() == "":
            return self.emptyline()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
