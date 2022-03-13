class Employee:

    def __init__(self, f_name):
        self.first_name = f_name

    def print_name(self):
        print(self.first_name)


if __name__ == "__main__":
    employee_list = []
    employee_dict = {}
    for index in range(4):
        employee_first_name = input("Please Enter the Employee Name:")
        employee = Employee(employee_first_name)

        print(employee)
        employee.print_name()
        employee_dict[employee_first_name] = employee
        print("----------------------------------")

    '''
    print("The list of all employees")
    for employee_variable in employee_list:
        print(employee_variable)
        employee_variable.print_name()
        print("----------------------------------")

    '''
    print("====================== Dictionary ================")
    for employee_key in employee_dict:
        print(employee_key)
        print(employee_dict[employee_key])
        employee_dict[employee_key].print_name()