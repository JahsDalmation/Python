### __init__.py / lns / 2 / 15
### import / 2 / 'from functions import hello'
### ln / 15 / 'hello(msg)'
def hello(message):

    print(message)

### main.py / lns / 2 / 47
### import / 2 / 'from functions import exampleFunction1'
### ln / 47 / 'exampleFunction1(exampleList)'
def exampleFunction1(exampleList):

    counter = 1
    for example in exampleList:

        print(
            "[ %s ] > [ %s ]" %
            (counter, example)
        )
        counter += 1

### main.py / lns / 3 / 48
### import / 3 / 'from functions import exampleFunction2'
### ln / 48 / 'exampleFunction2()'
def exampleFunction2():

    print("...")
