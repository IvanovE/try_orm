from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    departament_id = Column(Integer, primary_key=True)
    name = Column(String)


class Salary(Base):
    __tablename__ = 'salary'
    salary_id = Column(Integer, primary_key=True)
    salary = Column(Integer)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", back_populates="salary")


class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))
    salary = relationship(
        Salary,
        backref=backref('employee',
                        uselist=True,
                        cascade='delete,all'))


from sqlalchemy import create_engine

engine = create_engine('sqlite:///orm.sqlite')  # an Engine, which the Session will use for connection

from sqlalchemy.orm import sessionmaker

session = sessionmaker()  # A configurable Session factory.

# ... later, when an engine URL is read from a configuration
# file or other events allow the engine to be created
session.configure(bind=engine)  # bind -Engine или другой объект Connectable, с которым будут связаны вновь
# созданные объекты Session.

Base.metadata.create_all(engine)

# def generate_employee(count):
#     result = []
#     for _ in range(count):
#         item = Employee(name=)

d = Department(name="TIds")
emp1 = Employee(name="Jocsxhn", department=d)
salary1 = Salary(salary=30000, employee=emp1)

# work with session
s = session()

s.add(d)
s.add(emp1)
s.add(salary1)
s.commit()
# s.delete(emp1)
s.close()


# Проблема блокировки бд

# con = sqlite3.connect()
# con.isolation_level = 'EXCLUSIVE'
# con.execute('BEGIN EXCLUSIVE')
# #exclusive access starts here. Nothing else can r/w the db, do your magic here.
# con.commit()
# con.close()
