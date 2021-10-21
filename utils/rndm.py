from random import choice
import string



    

class CreedsGenerator():
    '''coming soon...'''

    D = string.digits
    LC = string.ascii_lowercase
    UC = string.ascii_uppercase
    SC = string.punctuation
    
    
    
    def generate_pswrd(length: int, from_what_generate = D + LC + SC) -> string:

        '''Input length of password and from what generate. Defaults to generating a password
        from numbers, lowercase and uppercase, but you can input your string value or use values ​​
        or combinations of them to specify what to generate the password from:
        'PSWRD.D' = digits, 'PSWRD.LC' = ascii lowercase, 'PSWRD.UC' - ascii uppercase,
        'PSWRD.SC' - special characters   
        Sample: 'D + SC', 'LC + SC' or more...
        '''

        return (''.join(choice(from_what_generate) for i in range(length))) 

    def generate_mail():
        '''coming soon'''
        pass

    def generate_login():
        '''coming soon'''
        pass



