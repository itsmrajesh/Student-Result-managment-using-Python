import config
from util import DbUtil
import pymysql
from contact import Contact
from contact import result
from contact import res
from contact import update


class ContactDbOperations:

    def add_student(self, new_contact):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into new_student(name,usn,semister,dept,contact) values(%s,%s,%s,%s,%s)", (new_contact.name, new_contact.usn, new_contact.sem,new_contact.dept,new_contact.numb))
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)


    def add_result(self, new_result):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into result(name,usn,subject_code,subject_name,marks,result) values(%s,%s,%s,%s,%s,%s)", (new_result.name, new_result.usn, new_result.subc,new_result.subn,new_result.marks,new_result.res))
            connection.commit()

        except pymysql.MySQLError as error:
            print("While inserting Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def get_all_results(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,usn,subject_code,subject_name,marks,result from result")
                rows = cursor.fetchall()
                contacts = self.get_list_data1(rows)
                return contacts
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

                
    def get_all_res(self,search_str):
        try:

            conn = DbUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("select name,usn,sum((marks*10)/600) from result where usn = %s",('%' + search_str + '%'))
            contact = res(*cursor.fetchone())
            contacts = self.get_list_data2(contact)
            return  contact
        except pymysql.DatabaseError as error:
            print("While getting data from DB using usn... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(conn)
            DbUtil.close_cursor(cursor)

    def user_update(self, contact):
        try:
            conn = DbUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("update new_student set name=%s,semister=%s,dept=%s,contact=%s where usn = %s",contact)
            conn.commit()

        except pymysql.DatabaseError as error:
            print("While updating ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(conn)
            DbUtil.close_cursor(cursor)

    def get_all_contacts(self):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,usn,semister,dept,contact from new_student")
                rows = cursor.fetchall()
                contacts = self.get_list_data(rows)
                return contacts
        except Exception as error:
            print("While retrieving data ... ")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            if connection:
                DbUtil.close_connection(connection)
                DbUtil.close_cursor(cursor)

    def search_student(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,usn,semister,dept,contact from new_student where usn like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                contacts = self.get_list_data(rows)
                return contacts
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def search_usn1(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,usn,sum((marks*10)/600) from result where usn = %s",('%' + search_str + '%'))
                rows = cursor.fetchall()
                contacts = self.get_list_data2(rows)
                return contacts
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    def search_usn(self, search_str):
        try:
            connection = DbUtil.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select name,usn,subject_code,subject_name,marks,result from result where usn like %s ", ('%' + search_str + '%'))
                rows = cursor.fetchall()
                contacts = self.get_list_data1(rows)
                return contacts
        except Exception as error:
            print("While searching Data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

            
    @staticmethod
    def delete_contact(cid):
        try:
            connection = DbUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("delete from contact where cid = %s ", cid)
            connection.commit()

        except pymysql.DatabaseError as error:
            print("While deleting data ...")
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
        finally:
            DbUtil.close_connection(connection)
            DbUtil.close_cursor(cursor)

    @staticmethod
    def get_list_data(rows):
        return [Contact(*row) for row in rows]



    @staticmethod
    def get_list_data1(rows):
        return [result(*row) for row in rows]

 
    @staticmethod
    def get_list_data2(rows):
        return [res(*row) for row in rows]   
