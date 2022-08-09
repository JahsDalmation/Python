### __init__.py / lns / 5 / 9 / 18
### import / 5 / 'from classes import hi'
class hi:

    ### ln / 9 / 'h = hi()'
    def __init__(self):

        print("hello?")

    ### ln / 18 / 'h.hey()'
    def hey(self):

        print("hey!")

### main.py / lns / 8 / 51 / 55
### import / 8 / 'from classes import exampleClass'
class exampleClass:

    ### ln / 51 / 'e = exampleClass'
    def __init__(self):

        print("Welcome!")
        reply = input("> ")
        self.exampleFunction(reply)

    ### self / __init__() / 'self.exampleFunction(reply)'
    ### ln / 55 / 'e.exampleFunction(reply)'
    def exampleFunction(self, Reply):

        print(Reply)
