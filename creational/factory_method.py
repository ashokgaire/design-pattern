# -----------------------------------------------------------------------------------------------------------------
# Abstract Factory example:  Web and intranet are two different applications. Both use Sql And No SQL databases,
# Web uses mongodb and SQL but intranet uses Oracle and OrientDB. Both have different implementations.
# --

from abc import ABC, abstractmethod

class db_factory(ABC):
    @abstractmethod
    def create_no_sql_db(self):
        pass
    @abstractmethod
    def create_sql_db(self):
        pass

class WebFactory(db_factory):
    def create_no_sql_db(self):
        return MongoDB()
    def create_sql_db(self):
        return SQL()

class IntranetFactory(db_factory):
    def create_sql_db(self):
        return Oracle()
    def create_no_sql_db(self):
        return Orientdb()

class sql_database(ABC):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def select(self):
        pass

class  SQL(sql_database):
    def save(self):
        return('sql save called')
    def select(self):
        return('sql select called')

class Oracle(sql_database):
    def save(self):
        return('oracle save called')
    def select(self):
        return('select select called')

class nosql_database(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def get_object(self):
        pass

class MongoDB(nosql_database):
    def insert(self):
        return("insert called on mongodb")
    def get_object(self):
        return("get objectc called on mongodb")

class Orientdb(nosql_database):
    def insert(self):
        return ("insert called on orientdb")

    def get_object(self):
        return ("get objectc called on orientdb")



class Clinet:
    def get_database(self):
        abs_factory = WebFactory()
        sql_factory = abs_factory.create_sql_db()
        sql_factory.save()
        sql_factory.select()
        abs_factory = IntranetFactory()
        oracle_factory = abs_factory.create_sql_db()


clinet = Clinet()
clinet.get_database()



