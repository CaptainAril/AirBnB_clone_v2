#!/usr/bin/python3
from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

class FileStorage:
    ''' Defines the FileStorage Class '''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        ''' returns dictionary of all created objects '''
        if not cls:
            return self.__objects

        if cls not in classes.keys() and cls not in classes.values():
            return None

        cls = eval(cls) if type(cls) is str else cls

        return {key: obj for key, obj in self.__objects.items()
                if obj.__class__.__name__ == cls.__name__}

    def new(self, obj):
        '''
            creates dictionary of objects with
            key as <class_name>.<obj_id> and
            value as the created object itself
         '''
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        ''' Serializes objects into JSON '''
        objects = FileStorage.__objects
        dict_from_obj = {key: obj.to_dict() for key, obj in objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            dump(dict_from_obj, file)

    def reload(self):
        ''' Deserializes JSON into objects '''
        try:
            with open(FileStorage.__file_path) as file:
                dict_from_json = load(file)
                for obj in dict_from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except Exception:
            return

    def delete(self, obj=None):
        ''' deletes obj from __objects if it's inside else do nothing '''
        if obj is not None:
            obj_keys = FileStorage.__objects.keys()
            obj_key = f'{obj.__class__.__name__}.{obj.id}'
            if obj_key in obj_keys:
                del FileStorage.__objects[obj_key]

    def close(self):
        ''' deserializes the JSON file to objects '''
        self.reload()
