# stupidscript
A stack based scripting language made in a day for fun.

## syntax:
    2 2 + print
prints "4".

    'Hello world!\n' say
Say is just print without automatic newline.
Quotes support '\n' while doublequotes are like
raw lines.

    0 'x' let
'let' gets the last item on the stack and makes a variable with that name, it also
gets the second last item and assigns that variable that value.

## Variables & types
When a variable is changed in stupidscript it is a string, for example:

    'x' ask
    "x" ask
Since ask get the user input and changes the variable we use quotes.

    x print
Since print doesn't change "x" we leave it without quotes.

Quotes are used to refer to the address while without quotes we just return
the value of that variable.

## Operators
Stupidscript supports + - * / %

## Loops and ifs
Not implemented in the language.

## Comments
Not implemented in the language.

## Args
You can access arguments by referring to the variable "args":

    args 2 get

## Dicts & Get & Set
In stupidscript there are 4 types: int, str, bool and dicts.
Make a dict:

    'x' dict
Set a item in the dict:

    'x' 'Salute' 'Hello' set (Sets 'Salute' to have as a value 'Hello')
    x 'Salute' get (Pushes on the stack the value of the key 'Salute', in this case it's 'Hello')
