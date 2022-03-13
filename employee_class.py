import employee_m


class Employee:

    def __init__(self, id, first_name, last_name, position, birthDate, birthMonth, birthYear, grad):
        self.eid = id
        self.efirst_name = first_name
        self.elast_name = last_name
        self.eposition = position
        self.ebirth_day = birthDate
        self.ebirth_month = birthMonth
        self.ebirth_year = birthYear
        self.egraduated = grad


    def print_employee_info(self):
        print(f'Employee ID: {self.eid}')
        print(f"Employee first name: {self.efirst_name}")
        print(f"Employee last name: {self.elast_name}")
        print(f"Employee position: {self.eposition}")
        print(f"Employee birth day: {self.ebirth_day}")
        print(f"Employee birth month: {self.ebirth_month}")
        print(f"Employee birth year: {self.ebirth_year}")
        print(f"Employee graduated?  {self.egraduated}")


    def read_first_name():
        while True:
        first_name = input("Please Enter The Employee First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")


#id, firstname, lastname, position, birth_day, birth_month, birth_year, graduated


if __name__ == "__main__":

    employee_list = []
    employee_dict = {}

    employeesn = int(input("Input employee count:" ))

    for index in range (employeesn):
        employee_id = input("Please Enter the Employee ID: ")
        employee_firstname = input("Please Enter the Employee First Name: ")
        employee_lastname = input("Please Enter the Employee Last Name: ")
        employee_position = input("Please Enter the Employee Position:")
        employee_birthd = input("Please Enter the Employee Birth day:")
        employee_birthm = input("Please Enter the Employee Birth month:")
        employee_birthy = input("Please Enter the Employee Birth year:")
        employee_g = input("Graduated? y/n")
        emp = Employee(employee_id, employee_firstname, employee_lastname, employee_position, employee_birthd,
                       employee_birthm, employee_birthy, employee_g)
        employee_dict[employee_id] = emp










