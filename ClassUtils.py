
# Class with some utils functions.
class Utils(object):
    # Function that clears the terminal.
    @staticmethod
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
