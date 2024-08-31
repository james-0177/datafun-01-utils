
# Online Python - IDE, Editor, Compiler, Interpreter

# Online Python - IDE, Editor, Compiler, Interpreter
''' ITERATION 2

Module: Pinkston Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
In this second iteration, add a function that returns the byline as a string.
I'll create a function called get_byline().
It'll return my byline to whatever calls the get_byline() function.
I'll update the main function to use the new get_byline() function.

Same conditional boilerplate at the end.

I'll test this version before adding more code.'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Pinkston Analytics: Professional Data Analysis On Demand'

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
