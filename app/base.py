from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), '.env'))

#sql_database = os.getenv("SQLALCHEMY_DATABASE_URI")
sql_database = 'postgresql://biohackaton:biohackaton@localhost/biohackaton'
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            print("hi")
            self.engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), convert_unicode=True, pool_size=20,
                                        max_overflow=0, pool_pre_ping=True)
            print(os.environ.get('SQLALCHEMY_DATABASE_URI'))
            self.session = scoped_session(sessionmaker(autocommit=False, expire_on_commit=False,
                                                       autoflush=False,
                                                       bind=self.engine))
            Singleton.__instance = self


# engine = None
# _SessionFactory = None
#
#
# def initialize(connectionString):
#     global engine
#     engine = create_engine(connectionString)
#     # use session_factory() to get a new Session
#     global _SessionFactory
#     _SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

#LogBase = declarative_base()


def get_session():
    s = Singleton.getInstance()
    # engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'), convert_unicode=True, pool_size=20, max_overflow=0)
    # return scoped_session(sessionmaker(autocommit=False, expire_on_commit=False,
    #                                             autoflush=False,
    #                                             bind=s.engine))
    return s.session


def get_log_session():
    s = Singleton.getInstance()
    return s.log_session


Base.query = get_session().query_property()


def init_db():
    s = Singleton.getInstance()
    # engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'), convert_unicode=True)
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=s.engine)
    # Base.query = get_session().query_property()


# def init_log_db():
#     s = Singleton.getInstance()
#     from .request_log_model import RequestWebLogger
#     LogBase.metadata.create_all(bind=s.log_engine)
#     # Base.query = get_log_session().query_property()
