# Fall 2022 CSC 131-06
# Welcome to Coding using Git! We all must edit this same file.

# Create a Person object under 'Person objects' (starting on line 47*).
# Keep the list of persons in alphabetical by first name order. Example:
# john_doe = Person('John Doe', True)

# Update peers list (line 50*) with your Person object alphabetical order by
# first name. This list will increase as more students make commits.
# Example: peers = [fiz_ban, foo_bar, john_doe]

# Add an if-statement (line 57*) to print a message on whether or not you like
# pineapple pizza. Keep the if-statements alphabetical order by first name.
# See my example.

# *Note line numbers will change as people complete the homework.

# Run the program and make sure it works!
# You can use a simple online IDE if you don't have a Python3 environment
# Example: https://ideone.com/l/python-3

COURSE = ['CSC 131-06']
SEMESTER = ['Fall 2022']


class Person:
    '''
    This class is the Person class. It represents basic person info.
    Attributes
    ----------
    name : str
        a string for a person's full name (first and last) used to print
    likes_pineapple_pizza : bool
        whether or not this person likes pineapple on pizza
    '''
    # Python constructor to initialize attributes (fields in Java)

    def __init__(self, name: str, likes_pineapple_pizza: bool):
        self.name = name
        self.likes_pineapple_pizza = likes_pineapple_pizza

    # Special Python method used to represent a class's objects as a string
    def __repr__(self):
        return self.name


def main():
    # Person objects (alphabetical order by first name)
    alex_souv = Person('Alex Souv', False)
    gary_kane = Person('Gary Kane', False)
    haoyang_li = Person('Haoyang Li', False)
    vincent_lam = Person('Vincent Lam', False)
    jonathan_camarena_camacho = Person('Jonathan Camarena Camacho', True)

    # List of people in our class (alphabetical order by first name)
<<<<<<< HEAD
    peers = [alex_souv, gary_kane, haoyang_li, vincent_lam]
=======
    peers = [gary_kane, haoyang_li, jonathan_camarena_camacho, vincent_lam]
>>>>>>> 641e77359e62c68b9a395f8a05c558a8d3056b87

    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
    if alex_souv.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % alex_souv.name)
    else:
        print("%s DOES NOT like pineapple pizza" % alex_souv.name)
    if gary_kane.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % gary_kane.name)
    else:
        print("%s DOES NOT like pineapple pizza" % gary_kane.name)

    if haoyang_li.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % haoyang_li.name)
    else:
        print("%s DOES NOT like pineapple pizza" % haoyang_li.name)

    if jonathan_camarena_camacho.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % jonathan_camarena_camacho.name)
    else:
        print("%s DOES NOT like pineapple pizza" %
              jonathan_camarena_camacho.name)

    if vincent_lam.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % vincent_lam.name)
    else:
        print("%s DOES NOT like pineapple pizza" % vincent_lam.name)


if __name__ == "__main__":
    main()
