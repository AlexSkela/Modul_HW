from application.salary import *
from application.people import *

def dirty_main():
    person = get_employees()
    cal = calculate_salary()

if __name__ == '__main__':
    dirty_main()