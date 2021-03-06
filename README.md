# Pokedex

Project Name: Pokédex

Documentation Website:
https://kuvapcsitrd01.kutztown.edu/~tlaud746/CSC402/Project3/index.html

Author: Tyler Laudenslager

How to use the Pokédex program
--------------------------------------

Interactive Mode:
  
  -> python3 pokedex.py

Interactive mode allows for an 
interactive command session.
For help building commands use
this command
  
  $ Get : Help $

Batch Mode:
  
  -> python3 pokedex.py file [ file ]*

Batch mode is used to run alot of commands
from a file without having to type in each
command in manually from the keyboard. At
least one text file that contains commands
is required, however multiple files can be
added after. The brackets are to indicate
an optional feature not included at all when
using batch mode.

Description
---------------------------------------

This project was not initially envisioned 
to provide a robust way to obtain specific data
from an arbitrary dataset in a streamlined 
way. However, that is exactly what I have
developed due to the various design decisions
explained below.

We will begin starting with the dataset I choose
from kaggle.com at the URL address here

https://www.kaggle.com/abcsds/pokemon

Author : Alberto Barradas

This data was initially a bit messy to work with,
however using the pandas library with Python3 I was
able to remove all the data that I thought was
irrelevant to the project's purpose. Mostly the
second type column, legendary column, and the
sum of all attributes. I also deleted all the Pokémon
that had strange names. Once I was able to format
the data in a way I was confident could be used
I made the Pokémon class to make Pokémon objects
from each line of data in the file.

The Pokémon class in the pokemon.py module is the
blueprint for creating Pokémon objects. A Pokédex
is simply a collection of Pokémon so I decided I
would use a list to hold all the pokemon. In order
to make the Pokédex I simply skipped the first
line in the file and then used the * (splat) operator
to deconstruct each of the line components into the
proper parameters in the initilization method. Example
if the line is "Charmander","Fire",...,87. Then the
pokemon object would be created as follows

Pokemon("Charmander","Fire",...,87)

Where the ... indicates there are more parameters inside
that are not shown for brevity. The Pokemon class has
one additional method called repr which stands for
representation. In which, whenever a function needs to
print an object to the screen this function will be
called. This also me to have very precise control of
how Pokémon are displayed to the user. 

Accordingly, the function that handles all the specific 
details of building the Pokédex mentioned above is aptly 
named build_pokedex.

The next thing I have to mention is the command interface
I built. The command interface is an idea I had from the 
need to quickly be able to find the Pokémon I was looking 
for without needing to go through multiple sub-menus. I
thought if I simply need to find one pokemon by name I 
should not need to go through multiple menus with options 
for extended filtering and sorting.

The solution I made for this problem is a simple command
parser. The command parser requires a string as input from
the user and then breaks the string down in the following
ways. First I make sure the first character in the string
matches the last character. Then I split the string into
a list using the ";" character as my seperator value. Next
for each value I split into another list and make sure the
second item is the ":" character. Lastly I make a dictionary
in which the keys are the commands and the values are the
values of the commands. This dictionary is created using
a dictionary comprehension a feature exclusively used in
Python.

A major feature in Python3 is that functions are considered
first-class objects meaning they have all the normal operations
of an object. I can pass functions as arguments to other functions
and assign functions to variables. The one aspect of functions
being first-class objects that I relied on is that functions can 
also be returned from functions. These are sometimes referred to
as factory functions in other languages. This allowed me to make
custom lambda expressions for filtering data from the Pokédex.

Lambda expressions are simply functions that do not have a name.
The name of the lambda expression depends on which variable gets
assigned to that particular lambda expression. However, in most
cases the the power comes from having one variable being able
to call a whole array of functions one by one.

Filtering data from a sequence is straightforward in Python3. Lets
say we have a list of numbers [1,2,3,4,5] and we have a function called
find_odds then filter(find_odds,[1,2,3,4,5]) = [1,3,5]. This is because
find_odds takes a integer and returns true if odd or false if not. The
elements in the list that came back as true value stay in the list
the elements that returned false get removed. Using this information I
was able to make a bunch of lambda expressions to pass to filter
depending on which commands the user has chosen from the command
dictionary mentioned above. The way I did this was if any commands
were in the command dictionary that were not also in a static command
list I threw an error that displayed command invalid error message.
Then I matched command keys to lambda expressions and for each match
I would populate a list of filter functions that ultimately get passed
to a recursive function that would return the appropriate filtered
Pokédex according to the attributes requested.

Before I called the function that would filter the Pokédex I checked
to see if the user requested the Pokémon to be sorted in a particular
way. If the user did request a sort I would then call the sorted function
which can use a lambda function as the key for sorting. I made the program
be able to sort by any attribute available. I also decided that ascending
order would be the default with an optional @descend feature for
descending sorting.

This design implementation allows users be able to input commands 
in any order to quickly view any type of Pokémon. The bigger picture
is that I can apply this design implementation to any dataset and
provide robust commands for filtering and sorting any data that
can be encapsulated in a object.

The last thing I want to mention is that my program has a batch mode.
Batch mode is activated by creating a file that is allowed to hold
numerous commands and having the file be used as a command line
argument when I run the program. Example

  python3 pokedex.py input1

This command will run the pokedex and execute all the commands contained
inside the input1 text file. The output is organized in a way that
you can see exactly which command is being run with the ouput displayed
underneath. Batch mode also includes lines to tell the user which
file's commands are being executed.

Multiple files can be supplied after the initial file in the above 
command to execute more commands from different files. This feature
allows for orgainization of similiar commands across multiple files.

Conclusion
----------------------------- 

Initially I had a bunch of menus that would provide options for
filtering and sorting. I realized this is a standard way to write
this kind of program. I wanted to see if I could design something
that was a bit more complex. The command structure base for
controlling how the data was to be filtered and sorted made for
a robust and convienent way to access specific data very quickly.
The way I designed the program allows a straightforward way to 
implement more feature rich commands when needed very easily.
I hope I can extend this design pattern to more projects in the
future. 
