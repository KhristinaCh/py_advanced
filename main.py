from datetime import date

import application.db.people
import application.salary


if __name__ == '__main__':
    print(date.today())
    application.db.people.get_employees()
    application.salary.calculate_salary()
