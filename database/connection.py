from mongoengine import *
from utils.get_configs import database_configs


class MongoDB:
    """
    db_name is collection
    """

    def __init__(self,
                 db_name=database_configs['db_name'],
                 host=database_configs['host'],
                 port=database_configs['port']):
        self.db_name = db_name
        self.host = host
        self.port = port
        # connect(self.db_name, host=self.host, port=self.port)

    def connect_db(self):
        connect(db=self.db_name, host=self.host, port=self.port)
    #
    # def close_connect(self, alias='default'):
    #     disconnect(alias=alias)
