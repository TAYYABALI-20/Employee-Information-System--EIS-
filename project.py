import time
import sys

def authenticating_dots(num_dots):
    return '.' * num_dots

def animating_dots(dots=5, delay=0.6):
    
    for i in range(1, dots + 1):
        
        sys.stdout.write(f'\r  🛡 Authenticating, please wait{authenticating_dots(i)}')
        sys.stdout.flush()
        time.sleep(delay)

def main():
    time.sleep(1)
    animating_dots()
    
def loading():
    if __name__ == "__main__":
        main()

employees = [
    (1, "SARIM", "Logistics", 50000),
    (2, "Wahaj", "Inventory", 55000),
    (3, "MUSAWIR", "Finance", 60000),
    (4, "AHSAN", "Quality Control", 48000),
    (5, "S.M HAMZA", "Sales", 47000),
    (6, "TAYYAB", "IT", 75000),
    (7, "ALISHBA AHMED", "Human Resources", 52000),
    (8, "SAMAN ZAHRA", "Marketing", 45000),
    (9, "AFSAN BALOCH", "Logistics", 53000),
    (10, "ALISHBA IQBAL", "Finance", 57000),
    (11, "NARGIS", "Inventory", 46000),
    (12, "ALISHBA KHAN", "Quality Control", 50000),
    (13, "MUHAMMAD ZAID", "Sales", 48000),
    (14, "IRFAN RASOOL", "IT", 78000),
    (15, "MUHAMMAD OWAIS", "Human Resources", 54000),
    (16, "Nasir Khan", "Marketing", 51000),
    (17, "Raj Bhagat", "Logistics", 62000),
    (18, "Abdul Wasay", "Finance", 56000),
    (19, "Hasnain", "Inventory", 47000),
    (20, "John", "Sales", 49000)
]

def display_employees(employees):
    if __name__ == "__main__":
        main()
    print("\nEmployee Records:")
    print('-' * 68)
    print("|   ID    |          Name          |    Department     |  Salary   |")
    print('-' * 68)
    for employee in employees:
        print(f"|  {employee[0]:<5}  |  {employee[1]:<20}  |  {employee[2]:<15}  |  {employee[3]:<7}  |")
    print('-' * 68)
    
display_employees(employees)

def add_employees(employees):
    
    ended_list = input('Please begin entering the employee records by typing "Start". Once you have finished, type "Done" to complete the process: ').strip().lower()
    
    print()
    loading()
    
    if ended_list == 'start':
        
        while True:
            
            new_id = int(input('\n\nEnter the new Employee ID: '))
            name = input('\nEnter the new Employee Name: ')
            department = input('\nEnter the new Employee Department: ')
            salary = int(input('\nEnter the new Employee Salary: '))
            
            print()
            loading()
    
            if any(employee[0] == new_id for employee in employees):
                print('\nThis Employee ID already exists. Please try a unique ID.')
            
            else:
                new_employee = (new_id, name, department, salary)
                employees.append(new_employee)
                print('\n\nNew employee added successfully.')
                print()
                display_employees(employees)
            
            ended_list = input('\nWould you like to add another employee? Type "Start" to continue or "Done" to exit: ').strip().lower()
            
            print()
            loading()
            
            if ended_list == 'done':
                print('\n\nExiting the employee record entry process.')
                break
            
    elif ended_list == 'done':
        print('\nNo new records were added. Exiting the process.')
    
    else:
        print('\nInvalid input. Please type "Start" to add records or "Done" to exit.')

add_employees(employees)

def search_employees(employees):
    
    while True:
        
        search_employee = input('\n\nType "Search" to begin searching for employee records or "Done" to exit: ').strip().lower()
        
        print()
        loading()

        if search_employee == 'search':
            
            while True:
                
                try:
                    
                    search_id = int(input('\n\nEnter the Employee ID you want to search for: '))
                    
                    print()
                    loading()
                    
                    search_found = False
                    
                    for employee in employees:
                        
                        if employee[0] == search_id:
                            print('\n\nEmployee Found:')
                            print('-' * 68)
                            print(f"|   ID    |          Name          |    Department     |  Salary   |")
                            print('-' * 68)
                            print(f"|  {employee[0]:<5}  |  {employee[1]:<20}  |  {employee[2]:<15}  |  {employee[3]:<7}  |")
                            print('-' * 68)
                            search_found = True
                            break
                    
                    if not search_found:
                        print('\nEmployee ID not found.')

                    continue_search = input('\nDo you want to search for another employee? (yes/no): ').strip().lower()
                    
                    print()
                    loading()
                    
                    if continue_search == 'no':
                        break
                
                except ValueError:
                    print('\n\nInvalid input. Please enter a numeric value for the Employee ID.')

        elif search_employee == 'done':
            print('\n\nExiting the employee search process.')
            break

        else:
            print('\n\nInvalid input. Please type "Search" to search for records or "Done" to exit.')

search_employees(employees)

def delete_employee(employees):
    
    while True:
        
        delete_employee = input('\nType "Delete" to begin deletion for employee records or "Done" to exit: ').strip().lower()
        
        print()
        loading()
        
        if delete_employee == 'delete':
            
            while True:
                
                try:
                    
                    delete_id = int(input('\n\nEnter the Employee ID you want to delete: '))
                    
                    print()
                    loading()
                    
                    employee_found = False
                    
                    for employee in employees:
                        
                        if employee[0] == delete_id:
                            
                            employees.remove(employee)
                            
                            print('\n\nDeleted Employee:')
                            print('-' * 68)
                            print(f"|   ID    |          Name          |    Department     |  Salary   |")
                            print('-' * 68)
                            print(f"|  {employee[0]:<5}  |  {employee[1]:<20}  |  {employee[2]:<15}  |  {employee[3]:<7}  |")
                            print('-' * 68)
                            employee_found = True
                            break
                    
                    if not employee_found:
                        print('\n\nEmployee ID not found.')

                except ValueError:
                    print('\n\nInvalid input. Please enter a numeric value for the Employee ID.')

                continue_deletion = input('\nDo you want to delete another employee? (yes/no): ').strip().lower()
                
                print()
                loading()
                
                if continue_deletion == 'no':
                    break
        
        elif delete_employee == 'done':
            
            print('\nExiting the employee delete process.')
            
            print()
            loading()
            
            display_employees(employees)
            
            break

        else:
            print('\nInvalid input. Please type "Delete" to delete any record or "Done" to exit.')

delete_employee(employees)

def calculate_average_salary_by_department(employees):

    view_list = input('Would you like to see the average salary by department? (yes/no): ').strip().lower()
    
    print()
    loading()
    
    if view_list == 'yes':

        department_salary = {}
        
        for employee in employees:
            
            department = employee[2]
            salary = employee[3]
            
            if department not in department_salary:
                department_salary[department] = {'total_salary': 0, 'count': 0}
            
            department_salary[department]['total_salary'] += salary
            department_salary[department]['count'] += 1

        print('\n\nAverage Salary by Department:')
        print('-' * 42)
        print(f"| {'Department':<20} | {'Average Salary':<15} |")
        print('-' * 42)
        
        for department, data in department_salary.items():
            average_salary = data['total_salary'] / data['count']
            print(f"| {department:<20} | {average_salary:<15.2f} |")
        
        print('-' * 42)
    
    elif view_list == 'no':
        print('\nExiting without displaying the average salary list.')
    
    else:
        print('\nInvalid input. Please type "yes" or "no".')

calculate_average_salary_by_department(employees)

# import time
# import sys
# 
# def authenticating_dots(num_dots):
#     return '.' * num_dots
# 
# def animating_dots(dots=5, delay=0.6):
#     
#     for i in range(1, dots + 1):
#         
#         sys.stdout.write(f'\r  🛡 Authenticating, please wait{authenticating_dots(i)}')
#         sys.stdout.flush()
#         time.sleep(delay)
# 
# def main():
#     time.sleep(1)
#     animating_dots()
#     
# def loading():
#     if __name__ == "__main__":
#         main()
# 
# print("\n+" + "-" * 52 + "+")
# print("" + " " * 2 + "😊 Welcome To The Employee Information System (EIS)")
# print("+" + "-" * 52 + "+")
# 
# print("\n+" + "-" * 26 + "+")
# print("" + " " * 3 + "🔐 ADMIN LOGIN REQUIRED!")
# print("+" + "-" * 26 + "+")
# 
# admin_email = "admin@gmail.com"
# admin_password = "admin123"
# 
# admin_credential_1 = str(input("\nDear Admin, Please Enter Your 📧 Email Here: ")).lower()
# admin_credential_2 = str(input("\nDear Admin, Please Enter Your 🔑 Password Here: "))
# 
# print()
# 
# if admin_credential_1 == admin_email and admin_credential_2 == admin_password:
# 
#     loading()
# 
#     print("\n\nWelcome, Admin! You have successfully logged in.")
# 
#     print("Displaying the list of employee records:")
# 
# else:
# 
#     loading()
# 
#     print("\n\nLogin failed. Please check your email and password and try again.")
# 
#     print("\nIt looks like you forgot your password. No worries, let's help you reset it.")
# 
#     print("\nSet your new password. Remember to use a combination of uppercase, lowercase, \nnumbers, and symbols for enhanced security.")
# 
# def forgot_password(admin_password):
# 
#     new_password = str(input("\nEnter your new password: "))
# 
#     while new_password == admin_password:
#         print()
#         loading()
#         print("\n\nYour new password cannot be the same as your old password. Please choose a different password.")
#         new_password = str(input("\nEnter your new password: "))
# 
#     print()
#     loading()
# 
#     confirm_new_password = str(input("\n\nPlease confirm your new password: "))
# 
#     while confirm_new_password != new_password:
#         loading()
#         print("\n\nPassword mismatch detected. Make sure both entries are identical and try again.")
#         confirm_new_password = str(input("\n\nPlease confirm your new password: "))
# 
#     print()
#     loading()
# 
#     print("\n\nYour password has been changed. You can now log in with your new password.")
# 
#     admin_credential_1 = str(input("\nDear Admin, Please Enter Your 📧 Email Here: ")).lower()
#     admin_credential_2 = str(input("\nDear Admin, Please Enter Your 🔑 Password Here: "))
# 
#     while admin_credential_1 == admin_email and admin_credential_2 != new_password:
#         print()
#         loading()
#         print("\nIncorrect password. Please try again. If you've recently updated your password, \nmake sure you're using the new one.")
#         admin_credential_2 = input("\nDear Admin, Please Enter Your 🔑 Password Here: ")
# 
#         if admin_credential_1 == admin_email and admin_credential_2 == new_password:
#             print()
#             loading()
#         print("\n\nWelcome, Admin! You have successfully logged in.")
# 
# forgot_password(admin_password)