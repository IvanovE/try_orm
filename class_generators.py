from classes import *
from random import choice, choices


def generate_departmets(count, session):
    """
    Генератор департаментов
    :param count: количество департаментов
    :param session: сессия бд
    :return: непосредсвтенное добавление (commit) департаментов в бд
    """
    result = []
    for _ in range(count):
        department = Department(name=''.join(choices(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), k=8)))
        result.append(department)
    session.add_all(result)
    session.commit()


def generate_employees(count, session, departments):
    """
    Генератор сотрудников
    :param count: количество сотрудников
    :param session: сессия бд
    :param departments: ID департаментов
    :return: непосредсвтенное добавление (commit) сотрудников в бд
    """
    result = []
    for _ in range(count):
        item = Employee(name=''.join(choices(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), k=8)),
                        department_id=choice(departments)[0])
        result.append(item)
    session.add_all(result)
    session.commit()


def generate_salary(count, session, employees):
    """
    Генератор ЗП для сотрудинов
    :param count: количество ЗП
    :param session: сессия бд
    :param employees: ID сотрудников
    :return: непосредсвтенное добавление (commit) ЗП в бд
    """
    result = []
    for _ in range(count):
        item = Salary(salary=choice([20000, 30000, 40000]), employee_id=choice(employees)[0])
        result.append(item)
    session.add_all(result)
    session.commit()
