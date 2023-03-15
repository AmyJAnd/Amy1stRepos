from person import Person


class Employee(Person):
    # constructor
    def __init__(self, p_name, p_dob, p_postcode, service, emp_no, salary):
        # is looking to super constructor for definitions
        super().__init__(p_name, p_dob, p_postcode)
        # adding attributes particular to Employee class
        self._service = service
        self._emp_no = emp_no
        self._salary = salary

    def set_department(self, department):
        print("Department: ", department)

    def set_pension_date(self, pension):
        print("Pension scheme joined: ", pension)

    def check_pension_elig(self):  # only need self as all info is in init
        # if Employee.salary > 25000 not right because that would be a class attribute
        if self._salary > 25000:
            print(True)
        else:
            print(False)

