import pymongo
from server.config import USER, PASSWORD

client = pymongo.MongoClient('mongodb://localhost:27017')


# client = pymongo.MongoClient(F'mongodb+srv://{USER}:{PASSWORD}@cluster.whbbl1q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster')
# db = client.game_bot


class LinkBD:
    def __init__(self, client):
        self.client = client
        self.db = client.game_bot

    def get_db(self):
        return self.db

    def use_test(self):
        self.db = client.test_db


config = LinkBD(client=client)
db = config.get_db()
