from person import Person


class Customer(Person):
    # constructor
    def __init__(self, p_name, p_dob, p_postcode, centile, mailable, main_store):
        # is looking to super constructor for inherited attributes
        super().__init__(p_name, p_dob, p_postcode)
        # adding attributes particular to Employee class
        self.centile = centile
        self.mailable = mailable
        self.main_store = main_store


    def set_points(self, points:int):  # type hinting but won't stop you putting in a string
        self._points = points  # this is so it remembers points
        print("Points balance: ", points)

    def check_points(self):  # not (self, points) because points are set as attribute in set points above
        if self._points > 500:
            print(self._name + ", you can redeem your points")  # need self._name
        else:
            print(self._name + ", keep saving to redeem your points")
