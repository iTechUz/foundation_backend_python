print("My name is", "Python.", end=" ")
print("Monty Python.")

"""
    Python offers another mechanism for the passing of arguments,
        which can be helpful when you want to convince the print() function to 
        change its behavior a bit.

    We aren't going to explain it in depth right now. We plan to do this
        when we talk about functions. For now, we simply want to show you how it
        works. Feel free to use it in your own programs.

    The mechanism is called keyword arguments. The name stems from the fact that
        the meaning of these arguments is taken not from its location (position)
        but from the special word (keyword) used to identify them.

    The print() function has two keyword arguments that you can use for your
        purposes. The first is called end.

    In the editor window you can see a very simple example how to use a keyword
        argument.    
"""

"""
    a keyword argument consists of three elements:
        a keyword identifying the argument (end here);
        an equal sign (=); and a value assigned to that argument;
    
    any keyword arguments have to be put after the last positional argument
        (this is very important)
    In our example, we have made use of the end keyword argument,
        and set it to a string containing one space.
"""


# print("My name is ", end="")
# print("Monty Python.")


# print("My", "name", "is", "Monty", "Python.", sep="-")



# print("My", "name", "is", "Monty", "Python.", sep="-")




# print("My", "name", "is", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")



