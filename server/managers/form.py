from server.database import config
from bson import json_util
import json
from bson.objectid import ObjectId


def parse_json(data):
    return json.loads(json_util.dumps(data))


class Form:
    forms = config.db.forms

    def __init__(self, chat_id: int = None, age: str = None, first_name: str = None, last_name: str = None,
                 tag: str = None, link_tg: str = None):
        self.chat_id = chat_id
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.tag = tag
        self.link_tg = link_tg

    def __setattr__(self, key, value):
        if key == 'chat_id':
            if type(value) is not int and value is not None:
                raise ValueError('The id parameter must be an integer')
        super().__setattr__(key, value)

    @classmethod
    def get(cls, id):
        form_dict = cls.forms.find_one({'_id': ObjectId(id)})
        if not form_dict:
            return None
        form = cls()
        form.fill_form(form_dict)
        form._id = id
        return form

    @classmethod
    def get_all(cls):
        forms = []
        forms_db = cls.forms.find({})
        for form_db in forms_db:
            form = cls()
            form.fill_form(form_dict=form_db)
            form._id = str(form._id)
            forms.append(form)
        return forms

    def add(self):
        self.forms.insert_one(self.__dict__)

    def update(self):
        self.forms.update_one({'_id': self.id}, self.__dict__)

    def delete(self):
        self.forms.delete_one({'_id': self.id})

    def fill_form(self, form_dict: dict):
        self.__dict__.update(form_dict)

    @staticmethod
    def parse_json(data):
        return json.loads(json_util.dumps(data))
