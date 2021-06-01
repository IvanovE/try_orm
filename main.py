from classes import *
from class_generators import generate_salary, generate_employees, generate_departmets

from sqlalchemy import create_engine

engine = create_engine('sqlite:///orm9', connect_args={'timeout': 15})  # an Engine, which the Session will
# use for connection

from sqlalchemy.orm import sessionmaker

session = sessionmaker()  # A configurable Session factory.

# ... later, when an engine URL is read from a configuration
# file or other events allow the engine to be created
session.configure(bind=engine)  # bind -Engine или другой объект Connectable, с которым будут связаны вновь
# созданные объекты Session.

Base.metadata.create_all(engine)

# work with session

s = session()

# generate_departmets(5, s)
# departments = s.query(Department.id).all()
# print(departments)

#  Добавить 20 работников

# generate_employees(20, s, departments)


# сделать 10 штук (выбор из 20, 30, 40)

# employees = s.query(Employee).all()
# print(employees)
# generate_salary(10, s, employees)

# result = s.query(Employee).filter(Employee.department_id == 5).all()
# print(result)
# print(len(result))


# Получить всех работник, у которых нет зп


# Добавить 30 селари и получить тех, у кого зп 20, 30, 40к

# employees = s.query(Employee.id).all()
# generate_salary(20, s, employees)

# result = s.query(Employee, Salary.salary).join(Salary).filter(Salary.salary == 20000).all()
# print(result)

# result_20 = []
# result_30 = []
# result_40 = []
# for p in s.query(Employee).join(Salary).filter(Salary.salary == 20000).all():
#     result_20.append((p.id, p.name))
# print(result_20)
# for p in s.query(Employee).join(Salary).filter(Salary.salary == 30000).all():
#     result_30.append((p.id, p.name))
# print(result_30)
# for p in s.query(Employee).join(Salary).filter(Salary.salary == 40000).all():
#     result_40.append((p.id, p.name))
# print(result_40)


# Одинаковые департаменты

# for p in s.query(func.count(Employee.department_id) >= 2, Employee.id, Employee.name, Employee.department_id)\
#         .group_by(Employee.department_id).all():
#     print(p)


# Вывести, у кого больше одной зп

from sqlalchemy import func

# result = s.query(func.count(Salary.employee_id) >= 2, Salary.employee_id).group_by(Salary.employee_id).all()
# print(result)

# result = s.query(Salary.employee_id, Salary.id).group_by(Salary.employee_id).having(func.count(Salary.employee_id) > 1).all()
# print(result)

# print(
#     s.query(Employee, func.count(Salary.employee_id)).join(Salary).group_by(Salary.employee_id).having(
#         func.count(Salary.employee_id) > 1).all()
# )

# print(
#     s.query(Employee, Salary.id).join(Salary, isouter=True).filter(Salary.id is None).count())


# print(s.query(Salary).group_by(Salary.employee_id).count())


# print(
#     s.query(Employee, Salary.id).join(Salary, isouter=True).filter(Salary.id == None,
#                                                                    Employee.department_id == 2).all())

# print(
#     s.query(Employee, func.count(Salary.employee_id)).join(Salary).filter(Employee.department_id == 1).group_by(
#         Salary.employee_id).having(func.count(Salary.employee_id) > 1).all())


# print(
#     s.query(Employee.department_id, func.count(Employee.id)).join(Salary, isouter=True).filter(
#         Salary.id == None).group_by(Employee.department_id).having(func.count(Employee.id)).order_by(
#         func.count(Employee.id).desc()).first())


# Вывести для каждого работника его последнюю зарплату

# print(
#     s.query(Employee.id, Employee.name, Salary.salary).join(Salary).group_by(Employee.id).all()
# )


# Посчитать сколько в сумме зп у каждого департамента, учесть что работники могут повторяться
# (два запроса: с учетом повторения и без)

# print(
#     s.query(Department.id, Department.name, ).join(Salary).join(Employee).group_by(Department.id).all()
# )


engine.dispose()
