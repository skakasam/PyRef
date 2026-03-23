"""Python Class Decorators"""

################################################################################
# Class Decorators are a way to manage classes or wrap instance-creation calls
# with extra logic. They need to handle/manage two levels of augmentation:
#   1. Instance construction calls
#   2. Instance interface access
################################################################################

print("--> CLASS DECORATORS <--")


# Managing Instance Construction using Decorators with Singleton Pattern
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):  # On @ decoration
        if cls not in instances:  # On instance creation
            instances[cls] = cls(*args, **kwargs)  # One dict entry per class
        return instances[cls]

    return get_instance  # Closure remembers instances dict


@singleton  # Decorates the DBConn class, i.e., DBConn = singleton(DBConn)
class DBConn:  # Rebinds DBConn to get_instance
    def __init__(self, db_url):  # get_instance remembers DBConn
        self.db_url = db_url

    def connect(self):
        print(f"Connecting to database at {self.db_url}")

    def __repr__(self) -> str:
        return f"DBConn(id={id(self)!r}, db_url={self.db_url!r})"


db1 = DBConn("sqlite:///:memory:")
db2 = DBConn("sqlite:///:memory:")

print(f"{db1 = }")
print(f"{db2 = }")
print(f"{db1 is db2 = }")  # True


# Managing Instance Interface Access using Decorators with Wrapper/Proxy Pattern
def with_tracing(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            print(f"TRACE: '{name}' attribute fetched")
            attr = getattr(self.wrapped, name)
            self.fetches += 1
            return attr

    return Wrapper


@with_tracing
class Employee:
    def __init__(self, name, rate, hours):
        self.name = name
        self.rate = rate
        self.hours = hours

    def pay(self):
        return self.rate * self.hours


print()

bob = Employee("Bob", 25, 40)
print(f"{bob.name = }")
print(f"{bob.pay() = }")
print(f"{bob.fetches = }")

sue = Employee("Sue", 30, 35)
print(f"{sue.name = }")
print(f"{sue.pay() = }")
print(f"{sue.fetches = }")
