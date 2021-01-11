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

'''result (same instancec for both object )

first object <__main__.Singleton object at 0x7f7ad5bbb850>
second object <__main__.Singleton object at 0x7f7ad5bbb850>

'''

