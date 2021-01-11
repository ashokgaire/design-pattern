#singleton pattern

class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()
print('first object', s1)

s2 = Singleton()
print('second object', s1)

# noinspection PyInterpreter
'''result (same instancec for both object )

first object <__main__.Singleton object at 0x7f7ad5bbb850>
second object <__main__.Singleton object at 0x7f7ad5bbb850>

'''

# implementaton of singleton pattern for databaseconnection

import sqlite3

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print ("Connection db1", db1)
print ("Connection db2", db2)



# Lazy instantiation in singleton pattern

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("method called")
        else:
            print("instance alreaddy created.", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__inistance=Singleton()
        return cls.__instance()

# Class is initialized and object is not created yet.
s = Singleton()

print ("Object created:", Singleton.getInstance())

# instance already created.
s1 = Singleton()

