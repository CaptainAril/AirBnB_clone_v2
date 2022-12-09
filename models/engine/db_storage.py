#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.place import Place
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        obj_list = []
        if cls:
            obj_list = self.__session.query(cls).all()
        else:
            for cl in [City, State, User]:
                obj = (self.__session.query(cl).all())
                for obj in obj:
                    obj_list.append(obj)
        for obj in obj_list:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(sess)
        self.__session = Session()
