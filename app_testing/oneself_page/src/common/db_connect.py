# coding:utf-8

import psycopg2
import configparser
from config.globalparameter import config_file_path


class Db_Connect(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self.host = config.get("dbServer", "dbServer")
        self.user = config.get("user", "user")
        self.password = config.get("password", "password")
        self.db = config.get("db", "db")
        self.port = config.get("port", "port")


    def db_connect(self):
        db = psycopg2.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=int(self.port))
        return db


    def db_executesql(self, sql):
        db = psycopg2.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=int(self.port))

        cur = db.cursor()
        try:
            cur.execute(sql)
            return cur
        except Exception as e:
            raise e