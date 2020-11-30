from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json , pprint, datetime


class Crypto:
    def __init__(self, name):
        """ create a crypto called name """
        self.name = name
        self.symbol = symbol
        self.price = price
    
    def __str__(self):
        """ returns self's name """
        return self.name

# class Person:
#     def __init__(self, name):
#         """create a person called name"""
#         self.name = name
#         self.birthday = None
#         self.last_name = name.split(" ")[-1]
    
#     def __str__(self):
#         return self.name
        
#     def set_birthday(self, month, day, year):
#         """sets self's birthday to birthDate"""
#         self.birthday = datetime.date(year, month, day)

#     def get_age(self):
#         """returns self's current age in days"""
#         if self.birthday is None:
#             raise ValueError
#         return (datetime.date.today() - self.birthday).days

#     def __lt__(self, other):
#         """return True if self's name is lexicographically
#            less than other's name, and False otherwise""" 
#         if self.last_name == other.last_name:
#             return self.name < other.name
#         return self.last_name < other.last_name



def main():
    


if __name__ == "__main__":
    main()
