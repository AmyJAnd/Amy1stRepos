# super class
class Person:
    # super class constructor
    def __init__(self, name, yob, postcode):
        self._name = name
        self._dob = yob
        self._postcode = postcode
        self._mobile_no = 0

# sets mobile number taking input from script user
    def set_mobile(self, number):
        self._mobile_no = number  # this sets number so prog remembers it
        print("mobile number: ", number)

# prints back mobile number?
    def get_mobile(self):
        return self._mobile_no

# set country
    def set_country(self, country):
        self._country = country
        # print("Country: ", country)

# prints back country
    def get_country(self):
        return self._country




