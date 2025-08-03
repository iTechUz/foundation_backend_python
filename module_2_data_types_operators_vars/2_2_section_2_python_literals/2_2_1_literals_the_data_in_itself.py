print("2")
print(2)


"""
    The first line looks familiar. The second seems to be erroneous due to the visible lack of quotes.

    Try to run it.

    If everything goes okay, you'll now see two identical lines.

    What happened? What does it mean?

    Through this example, you encounter two different types of literals:

    a string, which you already know,
    and an integer number, something completely new.
    The print() function presents them in exactly the same way ‒
        this example is obvious, as their human-readable representation is also the same.
        Internally, in the computer's memory, these two values are stored in
        completely different ways ‒ the string exists as just a string ‒ a series of
        letters.

    The number is converted into machine representation (a set of bits).
        The print() function is able to show them both in a form readable to humans.
"""