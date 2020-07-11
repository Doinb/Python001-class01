# -*- coding: utf-8 -*-
"""
    db_util.py
    DB工具类
"""
import pymysql

db_setting = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'maoyan'
}


class ConnDB:
    def __int__(self):
        self.host = db_setting['host']
        self.port = db_setting['port']
        self.user = db_setting['user']
        self.password = db_setting['password']
        self.db = db_setting['db']

    def exec(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            cur = conn.cursor()
            cur.execute(sql)
        except Exception as e:
            if conn is not None:
                conn.rollback()
            print('操作数据库出现异常')
            print(e)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

    def insert(self, sql, args):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            cur = conn.cursor()
            cur.execute(sql, args)
        except Exception as e:
            if conn is not None:
                conn.rollback()
            print('操作数据库出现异常')
            print(e)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
