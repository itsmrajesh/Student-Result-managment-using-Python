import pymysql
import config

class DbUtil:

    @staticmethod
    def get_connection():
        try:
            con = pymysql.connect(config.mysql['host'], config.mysql['user'],config.mysql['passwd'],config.mysql['db'])
        except pymysql.MySQLError as error:
            print('Exception number: {}, value {s}'.format(error.args[0], error))
            raise
        else:
            return con

    @staticmethod
    def close_connection(conn):
        try:
            conn.close()
        except pymysql.MySQLError as error:
            print("While closing connection ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
            raise

    @staticmethod
    def close_cursor(cursor):
        try:
            cursor.close()
        except pymysql.MySQLError as error:
            print("While closing the cursor ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
