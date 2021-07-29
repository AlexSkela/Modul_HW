from application.people import get_employees
from application.salary import calculate_salary

def main():
    person = get_employees()
    cal = calculate_salary()

if __name__ == '__main__':
    main()
