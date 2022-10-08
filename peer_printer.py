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
    aaron_jumawan = Person('Aaron Jumawan', True)
    alex_souv = Person('Alex Souv', False)
    amir_talakoob = Person('Amir Talakoob', False)
    andreas_zignago = Person('Andreas Zignago', True)
    anish_chouhan = Person('Anish Chouhan', True)
    anuja_chouhan = Person('Anuja Chouhan', False)
    branden_nguyen = Person('Branden Nguyen', False)
    brandon_kmiec = Person('Brandon Kmiec', True)
    blake_danz =Person('Blake Danz', False)
    casey_paras = Person('Casey Paras', False)
    cesar_MDC = Person('Cesar Martin Del Campo', True)
    christian_vela = Person('Christian Vela', True)
    danny_zhou = Person('Danny Zhou', True)
    diya_soneji = Person('Diya Soneji', False)
    eduardo_lopez = Person('Eduardo Lopez', True)
    eric_brutskiy = Person('Eric Brutskiy', True)
    gary_kane = Person('Gary Kane', False)
    haoyang_li = Person('Haoyang Li', False)
    jacob_correa = Person('Jacob Correa', False)
    kiranjot_kaur = Person('Kiranjot Kaur', True)
    mohammed_alchalabi = Person('Mohammed Al Chalabi', True)
    phuc_dinh = Person('Phuc Dinh', False)
    tom_bolyard = Person('Tom Bolyard', False)
    vincent_lam = Person('Vincent Lam', False)
    william_hong = Person('William Hong', False)
    jonathan_camarena_camacho = Person('Jonathan Camarena Camacho', True)
    joshua_cupler = Person('Joshua Cupler', True)
    jose_martinez = Person('Jose Martinez', False)
    rishi_somanchi = Person('Rishi Somanchi', False)
    sachal_ali = Person('Sachal Ali', False)
    samuel_caus = Person("Samuel Caus", True)
    Zhijun_Li = Person("Zhijun Li", False)
    # List of people in our class (alphabetical order by first name)


    peers = [aaron_jumawan,alex_souv, amir_talakoob, andreas_zignago,  anish_chouhan, anuja_chouhan, blake_danz, branden_nguyen, brandon_kmiec, casey_paras, christian_vela, danny_zhou, diya_soneji, eduardo_lopez, eric_brutskiy, gary_kane, haoyang_li, jacob_correa, jonathan_camarena_camacho, joshua_cupler, jose_martinez, kiranjot_kaur, mohammed_alchalabi, phuc_dinh, rishi_somanchi, sachal_ali, samuel_caus, tom_bolyard, vincent_lam, Zhijun_Li]



    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
    if aaron_jumawan.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % aaron_jumawan.name)
    else: 
        print ("%s DOES NOT like pineapple pizza" % aaron_jumawan.name)
    if alex_souv.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % alex_souv.name)
    else:
        print("%s DOES NOT like pineapple pizza" % alex_souv.name)
    
    if amir_talakoob.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % amir_talakoob.name)
    else:
        print("%s DOES NOT like pineapple pizza" % amir_talakoob.name)
	
    if andreas_zignago.likes_pineapple_pizza:
        print("%s likes pinapple pizza" % andreas_zignago.name)
    else:
        print("%s DOES NOT like pinapple pizza" % andreas_zignago.name)
		
    if anish_chouhan.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % anish_chouhan.name)
    else:
        print("%s DOES NOT like pineapple pizza" % anish_chouhan.name)

    if anuja_chouhan.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % anuja_chouhan.name)
    else: 
        print("%s DOES NOT like pineapple pizza" % anuja_chouhan.name)

    if branden_nguyen.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % branden_nguyen.name)
    else:
        print("%s DOES NOT like pineapple pizza" % branden_nguyen.name)
        
    if brandon_kmiec.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % brandon_kmiec.name)
    else:
        print("%s DOES NOT like pineapple pizza" % brandon_kmiec.name)

    if blake_danz.likes_pineapple_pizza:
        print("% likes pinapple pizza" % blake_danz.name)
    else:
        print("%s DOES NOT like pineapple pizza" % blake_danz.name)

    if casey_paras.likes_pineapple_pizza:
        print("% likes pinapple pizza" % casey_paras.name)
    else:
        print("%s DOES NOT like pineapple pizza" % casey_paras.name)

    if cesar_MDC.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % cesar_MDC.name)
    else
        print("%s DOES NOT like pineapple pizza" % cesar_MDC.name)

    if christian_vela.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % christian_vela.name)
    else:
        print("%s DOES NOT like pineapple pizza" % christian_vela.name)   

    if danny_zhou.likes_pineapple_pizza:
        print(f'{danny_zhou} likes pineapple pizza')
    else:
        print(f'{danny_zhou} DOES NOT like pineapple pizza')

    if diya_soneji.likes_pineapple_pizza:
        print(f'{diya_soneji} likes pineapple pizza')
    else:
        print(f'{diya_soneji} DOES NOT like pineapple pizza')

    if eduardo_lopez.likes_pineapple_pizza:
    	print("%s likes pineapple pizza" % eduardo_lopez.name)
    else:
    	print("%s DOES NOT likes pineapple pizza" % eduardo_lopez.name)

    if eric_brutskiy.likes_pineapple_pizza:
    	print("%s likes pineapple pizza" % eric_brutskiy.name)
    else:
    	print("%s DOES NOT likes pineapple pizza" % eric_brutskiy.name)
    
    if gary_kane.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % gary_kane.name)
    else:
        print("%s DOES NOT like pineapple pizza" % gary_kane.name)

    if haoyang_li.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % haoyang_li.name)
    else:
        print("%s DOES NOT like pineapple pizza" % haoyang_li.name)

    if jacob_correa.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % jacob_correa.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jacob_correa.name)

    if jonathan_camarena_camacho.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % jonathan_camarena_camacho.name)
    else:
        print("%s DOES NOT like pineapple pizza" %
              jonathan_camarena_camacho.name)

    if joshua_cupler.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % joshua_cupler.name)
    else:
        print("%s DOES NOT like pineapple pizza" % joshua_cupler.name)

    if jose_martinez.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % jose_martinez.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jose_martinez.name)

    if kiranjot_kaur.likes_pineapple_pizza:
      print("%s likes pineapple pizza" % kiranjot_kaur.name)
    else: 
      print("%s DOES NOT like pineapple pizza" % kiranjot_kaur.name)

    if mohammed_alchalabi.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % mohammed_alchalabi.name)
    else:
        print("%s DOES NOT like pineapple pizza" % mohammed_alchalabi.name)

    if phuc_dinh.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % phuc_dinh.name)
    else:
        print("%s DOES NOT like pineapple pizza" % phuc_dinh.name)

    if rishi_somanchi.likes_pineapple_pizza:
	    print("%s likes pineapple pizza" % rishi_somanchi.name)
    else:
	    print("%s DOES NOT like pineapple pizza" % rishi_somanchi.name)

    if sachal_ali.likes_pineapple_pizza:
	    print("%s likes pineapple pizza" % sachal_ali.name)
    else:
	    print("%s DOES NOT like pineapple pizza" % sachal_ali.name)

    if tom_bolyard.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % tom_bolyard.name)
    else:
        print("%s DOES NOT like pineapple pizza" % tom_bolyard.name)

    if vincent_lam.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % vincent_lam.name)
    else:
        print("%s DOES NOT like pineapple pizza" % vincent_lam.name)
    if william_hong.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % william_hong.name)
    else:
        print("%s DOES NOT like pineapple pizza" % william_hong.name)
    if Zhijun_Li.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % Zhijun_Li.name)
    else:
        print("%s DOES NOT like pineapple pizza" % Zhijun_Li.name)
    if samuel_caus.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % samuel_caus.name)
    else:
        print("%s DOES NOT like pineapple pizza" % samuel_caus.name)

if __name__ == "__main__":
    main()

