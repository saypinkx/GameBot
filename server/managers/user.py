from server.database import config


class User:
    users = config.db.users

    def __init__(self, chat_id: int, parameters: dict = None):
        self._id = chat_id
        if parameters:
            for key in parameters:
                self.__dict__[key] = parameters[key]

    def __setattr__(self, key, value):
        if key == '_id':
            if type(value) is not int:
                raise ValueError('The id parameter must be an integer')
        super().__setattr__(key, value)

    @classmethod
    def get(cls, chat_id):
        user_dict = cls.users.find_one({'_id': chat_id})
        if not user_dict:
            return None
        return cls(chat_id=chat_id, parameters=user_dict)

    def add(self):
        self.users.insert_one(self.__dict__)

    def update(self, parameters):
        self.__dict__.update(parameters)
        self.users.update_one({'_id': self._id}, self.__dict__)

    def delete(self):
        self.users.delete_one({'_id': self._id})
