# details.py will be where most oif the functions, classes, and everything else will be placed and main.py will be the logic
import string
import random
from functools import reduce
import json

# Usual context manager
class ContextManager:
        def __init__(self,filename):
            self.file = open(filename)

        def __enter__(self):
            return self.file

        def __exit__(self, type, value, traceback):
            self.file.close()

# I want to try put everything into a single class, may not be best practice but it'll be fun
class Password:
    def __init__(self,name,length):
        self._name = name
        self._length = length

        self._password = Password.make_password(self._length)

    @classmethod
    def create_new_password(self):
        return_name = input("Name: ")
        return_length = int(input("Length: "))
        
        return Password(return_name,return_length)

    @staticmethod
    def make_password(length):
        # Fetch and group all character options
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation
        # Combine
        combined_sample = lower + upper + numbers + symbols

        # Sample from list based on length
        list_of_samples = random.sample(combined_sample,length)
        # Combine it into string
        return_value = reduce(lambda a,b:f"{a}{b}",list_of_samples)
        # return value
        return return_value

    def save_password(self):
        # I have to format the data into the right data structures
        create_json = {
            "name" : self._name,
            "password" : self._password
        }

        # The problem was that .append() returns None, so using list = list.append() will return None
        dump_list = self.import_passwords()
        dump_list.append(create_json)
        # This makes the file pretty and readable
        dump_list = json.dumps(dump_list,indent=4)
        with open('passwords/passwords.json','w') as passwords_file:
            passwords_file.write(dump_list)

    @staticmethod
    def import_passwords():
        with ContextManager('passwords/passwords.json') as pass_file:
            return list(json.loads(pass_file.read()))


    @staticmethod
    def fetch_password(name):
        passwords = Password.import_passwords()
        for item in passwords:
            if item['name'].lower() == name.lower():
                return item





    

