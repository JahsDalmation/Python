### imports

#### functions
from functions import (
    exampleFunction1,
    exampleFunction2,
)

#### classes
from classes import (
    exampleClass,
)

### variables
counter = 1
reply = 'hi'

### data
exampleList = (
    "Hi",
    "Hello",
    "Goodbye",
)

### spaget...
riding = False
while riding != True:

    rides = input("[ 1 ] <= [ x ] <= [ 5 ]")

    try:

        rides = int(rides)
        if 1 <= rides <= 5:

            riding = True

        else:

            riding = False

    except ValueError:

        riding = False

while rides > 0:

    exampleFunction1(exampleList)
    exampleFunction2()

    e = exampleClass()

    e.exampleFunction(reply)

    rides -= 1
