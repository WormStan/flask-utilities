import pymysql
import webapp.db_connection.config as config


class MYSQL_CONN:

    def __init__(self):
        self.host = config.HOST,
        self.port = config.PORT,
        self.user = config.USER,
        self.passwd = config.PWD,
        self.db = config.DATABASE,
        self.charset = config.CHARSET

    def __conn(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passwd,
            database=self.db,
            charset=self.charset
        )
        cur = self.conn.cursor()
        return cur

    def execute_query(self, sql):
        cur = self.__conn()
        cur.execute(sql)
        resultList = cur.fetchall()
        self.conn.close()
        return resultList

    def execute_non_query(self, sql):
        cur = self.__conn()
        cur.execute(sql)
        cur.commit()
        self.conn.close()
