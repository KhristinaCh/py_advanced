from datetime import date

from application import *
from application.db import *


if __name__ == '__main__':
    print(date.today())
    salary.calculate_salary()
    people.get_employees()
