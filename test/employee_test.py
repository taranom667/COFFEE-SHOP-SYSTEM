from model.employee import Employee
from repository.employee_repository import Employee_repository
import sqlite3





employee1 = Employee("1","taranom","bagheri","manager","tari","slriuhf",98765)
employee_r=Employee_repository()
employee_r.delete(employee1)

