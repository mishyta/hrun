import base64
from getpass import getpass
# a temporary solution 
class crds():
    
    def set():
        c = str.encode(input('l:')) +b' '
        c += str.encode(getpass('p:'))
        with open("crds", "wb") as image_file:
            image_file.write(base64.b64encode(c))

    def get():
        with open("crds", "rb") as image_file:
            return tuple(base64.b64decode(image_file.read()).decode('ascii').split())
