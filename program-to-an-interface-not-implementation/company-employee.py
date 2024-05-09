# before
'''
class Designer:
    def design_software(self):
        print("Software designed by designer")

class Programmer:
    def code_software(self):
        print("Software coded by programmer")

class Tester:
    def test_software(self):
        print("Software tested by tester")

class Company:
    def create_software(self):
        designer = Designer()
        programmer = Programmer()
        tester = Tester()
        designer.design_software()
        programmer.code_software()
        tester.test_software()
        print("Software created by company") 
'''


# after some refactoring
'''
# Here Employee class works as interface for Designer, Programmer and Tester classes
class Employee:
    def do_work(self) -> None:
        """Does some work"""
        pass

class Designer(Employee):
    def do_work(self) -> None:
        print("Software designed by designer")

class Programmer(Employee):
    def do_work(self) -> None:
        print("Software coded by programmer")

class Tester(Employee):
    def do_work(self) -> None:
        print("Software tested by tester")


class Company:
    def create_software(self):
        employees = [Designer(), Programmer(), Tester()]
        for employee in employees:
            employee: Employee
            employee.do_work()

        print("Software created by company")
'''

# make Company class independent of Employee class
# Employee Class can be handled by Company Type Classes
class Employee:
    def do_work(self) -> None:
        """Does some work"""
        pass

class Designer(Employee):
    def do_work(self) -> None:
        print("Software designed by designer")

class Programmer(Employee):
    def do_work(self) -> None:
        print("Software coded by programmer")

class Tester(Employee):
    def do_work(self) -> None:
        print("Software tested by tester")


class OutSourcingCompany:
    def get_employees(self) -> list[Employee]:
        return [Designer(), Programmer()]

class GameDevCompany:
    def get_employees(self) -> list[Employee]:
        return [Designer(), Programmer(), Tester()]
    
class Company:
    def create_software(self):
        # internal logic to determine which type of company
        outsourcing_company = OutSourcingCompany()
        
        employees = outsourcing_company.get_employees()
        for employee in employees:
            employee: Employee
            employee.do_work()

        print("Software created by company")