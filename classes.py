from sqlalchemy import Column, Integer, String, func, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employee',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        return f'({self.id}, {self.name}, {self.department_id})'


class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    salary = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship(
        Employee,
        backref=backref('salary',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        return f'({self.id}, {self.salary}, {self.employee_id})'