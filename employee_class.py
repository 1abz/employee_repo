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

    def set_first_name(self, first_name):
        self.efirst_name = first_name

    def set_last_name(self, last_name):
        self.elast_name = last_name

    def set_birth_year(self, birth_year):
        self.ebirth_year = birth_year

    def set_birth_month(self, birth_month):
        self.ebirth_month = birth_month

    def set_birth_day(self, birth_day):
        self.ebirth_day = birth_day

    def set_emp_position(self, emp_position):
        self.eposition = emp_position

    def set_is_graduated(self, grad):
        self.egraduated = grad

    def set_ids(self, emp_id):
        self.eid = emp_id

    def get_first_name(self):
        return self.efirst_name

    def get_last_name(self):
        return self.elast_name

    def get_birth_year(self):
        return self.ebirth_year

    def get_birth_month(self):
        return self.ebirth_month

    def get_birth_day(self):
        return self.ebirth_day

    def get_emp_position(self):
        return self.eposition

    def get_is_graduated(self):
        return self.egraduated

    def get_emp_id(self):
        return self.eid

    def print_employee_info(self):
        print(f'Employee ID: {self.eid}')
        print(f"Employee first name: {self.efirst_name}")
        print(f"Employee last name: {self.elast_name}")
        print(f"Employee position: {self.eposition}")
        print(f"Employee birth day: {self.ebirth_day}")
        print(f"Employee birth month: {self.ebirth_month}")
        print(f"Employee birth year: {self.ebirth_year}")
        print(f"Employee graduated?  {self.egraduated}")

    def __str__(self):


    def update_eid(self, new_employeeid):
        if new_employeeid > 0:
            self.eid = new_employeeid
            print (f"Employee's Updated ID is {self.eid}")
        else:
            print("Updated Employee ID is not accepted")




def read_option():
    while True:
        user_option = input("This is a list of your options: add: Add an Employee, remove: Remove an Employee, list: List the Employees ,update: Update Employee Data, exit: Exit the app, total: Total number of employees, retrieve: Retrieve employee using ID ")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "update", "list", "exit", "total", "retrieve", ]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_first_name():
    while True:
        first_name = input("Please Enter The Employee First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")


def read_last_name():
    while True:
        last_name = input("Please Enter The Employee Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Employee Last Name should be at least 2 Characters")


def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")


def read_year():
    while True:
        year_str = input("Please Enter the Employee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Employee Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Employee Birth Year should be a number")


def read_month():
    while True:
        month_str = input("Please Enter the Employee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Employee Birth Month should be between 1 and 12")
        else:
            print("Error, The Employee Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Employee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Employee Birth Day should be between 1 and 31")
        else:
            print("Error, The Employee Birth Day should be a number")


def read_is_graduated():
        while True:
            is_graduated_str = input("Have the Employee graduated from the univesity (y/n):")
            is_graduated_str = is_graduated_str.strip()

            if is_graduated_str in ["y", "n"]:
                if is_graduated_str == "y":
                    return True
                else:
                    return False
            else:
                print("Error, Please Enter y or n")


def create_employee_dictionary():
    employee_id = read_employee_id()
    employee_firstname = read_first_name()
    employee_lastname = read_last_name()
    employee_position = read_position()

    employee_birthy = read_year()
    employee_birthm = read_month()

    employee_birthd = read_day()

    employee_g = read_is_graduated()



    emp = Employee(employee_id, employee_firstname, employee_lastname, employee_position, employee_birthd,
                   employee_birthm, employee_birthy, employee_g)

    employee_dict[employee_id] = emp

    print(emp)
    return emp


def read_employee_id():
    while True:
        id_str = input("Please Enter the Employee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0 :
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")


def print_all_employees_data():
    for employee_id_key in employee_dict:
        print(f"(The data of the employee with Employee_ID = {employee_id_key}")
        print(employee_dict[employee_id_key])


def read_field_option():
    while True:
        field_option = input("Please Enter the field you want to update: first_name, last_name, position, birth_year, birth_month, birth_day, is_graduated:")
        field_option = field_option.strip()

        if field_option in ["first_name", "last_name", "position", "birth_year", "birth_month", "birth_day", "is_graduated"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")


#id, firstname, lastname, position, birth_day, birth_month, birth_year, graduated


if __name__ == "__main__":

    employee_dict = {}

    while True:
        option = read_option()

        if option == "add":
            print("The user wants to add an Employee")
            employee_dict = create_employee_dictionary()

            employee_id = read_employee_id()
            employee_id = employee_dict["id"]

            all_employees_dict[employee_id] = employee_dict

            print(all_employees_dict)

        elif option == "remove":
            print("The user wants to remove an Employee")
            employee_id = read_employee_id()
            del all_employees_dict[employee_id]

        elif option == "list":
            print("The user wants a list of the employees")
            print_all_employees_data()

        elif option == "update":
            print("The user wants to update the data of an employee")
            employee_id = read_employee_id()
            update_employee_data(employee_id)

        elif option == "total":
            print("The user wants the total number of employees")
            print(len(all_employees_dict))

        elif option == "retrieve":
            print("The user wants to retrieve an Employee using ID")
            employee_id = read_employee_id()
            print(all_employees_dict[employee_id])

        elif option == "exit":
            print("Thanks, see you later")
            break

        else:
            print("Unknown option")








            #employee_id = input("Please Enter the Employee ID: ")
            #employee_firstname = Employee.read_first_name()





        """"
        #employee_lastname = input("Please Enter the Employee Last Name: ")
        #employee_position = input("Please Enter the Employee Position:")
        #employee_birthd = input("Please Enter the Employee Birth day:")
        employee_birthm = input("Please Enter the Employee Birth month:")
        employee_birthy = input("Please Enter the Employee Birth year:")
        employee_g = input("Graduated? y/n")
           """

        #emp = Employee(employee_id, employee_firstname, employee_lastname, employee_position, employee_birthd,
                       #employee_birthm, employee_birthy, employee_g)

        #emp = Employee(first_name)
        #employee_dict[employee_id] = emp












