#!/usr/bin/python3
""" The Console Module """
import cmd


class Console(cmd.Cmd):
    """
        The class that defines the Console
    """

    prompt = '(hbnb) '
    file = None

    # =======================================

    def do_quit(self, arg):
        """ Method to quit console window"""
        self.close()
        quit()
        return True

    def do_EOF(self, arg):
        """ Method that implements the EOF functionality"""
        return True

    # =======================================

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    Console().cmdloop()
