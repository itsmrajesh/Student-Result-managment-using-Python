from dboperations import ContactDbOperations
from contact import Contact
from beautifultable import BeautifulTable
from contact import result
from contact import res
from contact import update

class ContactService:

    def __init__(self):
        self.cs = ContactDbOperations()

    def add_student(self):
        name = input("Enter Student Name : ")
        usn = input("Enter Student USN : ")
        sem = int(input("Enter Student Semester : "))
        dept = input("Enter Student Dept :")
        numb = input("Entet Student Contact number :") 
        contact = Contact(name, usn, sem, dept,numb)
        self.cs.add_student(contact)
        print("Student Details Added sucesfully ")
        contacts = self.cs.search_student(usn)
        if contacts:
            ContactService.paint_data_list(contacts)
        else:
            print("No data found with Student USN :{}".format(usn))

    def search_student(self):
        usn = input("Enter Student USN :")
        contacts = self.cs.search_student(usn)
        if contacts:
            ContactService.paint_data_list(contacts)
        else:
            print("No data found with Student USN :{}".format(usn))

    def show_all_contacts(self):
        contacts = self.cs.get_all_contacts()
        ContactService.paint_data_list(contacts)

    def add_result(self):
        un=input("Enter user name :")
        pwd=input("Enter password :")
        if un == 'ncet' and pwd == 'ncet' :
            name = input("Enter Student Name : ")
            usn = input("Enter Student USN : ")
            n = 0
            m = int(input("ENTER NO OF SUBJECTS  : "))
            while (n < m):
                subc = input("Enter Subject  Code : ")
                subn = input("Enter Subject Name  :")
                marks = int(input("Entet Marks obtained by Student :"))
                if marks >= 40:
                    res='PASS'
                else:
                    res='FAIL'
                n = n + 1
                print("Results added sucessfully with USN",usn)
                contact = result(name, usn, subc, subn,marks,res)
                self.cs.add_result(contact)
                contacts = self.cs.search_usn(usn)
                if contacts:
                    ContactService.paint_data_list1(contacts)
                else:
                    print("No data found with search name :{}".format(usn))

                
            mar=int(input("Enter Total marks scored by student : "))   
            cgpa = ((mar*10)/(m*100))
            print("CGPA Scored by student  :",cgpa)
        else :
            print("Invalid Login")
            
    def show_all_result(self):
        contacts = self.cs.get_all_results()
        ContactService.paint_data_list1(contacts)

#update***************************************************************************
    def update_student(self):
        usn = input("Enter Student USN to Update details : ")
        name = input("Enter Student Name : ")
        sem = int(input("Enter Student Semester : "))
        dept = input("Enter Student Dept :")
        numb = input("Entet Student Contact number :") 
        contact = Contact(name,sem, dept,numb,usn)
        self.cs.user_update(contact)
        print("Updated sucessfully.....")
        contacts = self.cs.search_student(usn)
        if contacts:
            ContactService.paint_data_list(contacts)
        else:
            print("No data found with Student USN :{}".format(usn))


#update****************************************************************       
#search usn **********************************************    
    def search_usn(self):
        usn1=input("Enter USN :")
        pwd=input("Enter DOB like ddmmyyyy :")
        if usn1 == '1nc16cs001' and pwd == '01021998' :
            
            usn = input("Enter Student USN :")
            contacts = self.cs.search_usn(usn)
            if contacts:
                ContactService.paint_data_list1(contacts)
            else:
                print("No data found with search name :{}".format(usn))
        else:
            print("Invalid USN & DOB")
#ends **************************************************************************************************************************************************
    def show_resu(self):
        usn = input("Enter USN :")
        contact = result(0,usn,0,0,0,0)
        contacts = self.cs.get_all_res()
        ContactService.paint_data_list3(contacts)

    def show_res(self):
        usn = input("Enter usn  :")
        contacts = self.cs.search_usn1(usn)
        if contacts:
            ContactService.paint_data_list2(contacts)
        else:
            print("No data found with search name :{}".format(usn))
#revaluation ******************************************************************************************************************************************
    def apply_rv(self):
        name = input("Enter Student Name : ")
        usn = input("Enter Student USN : ")
        n = 0
        m = int(input("ENTER NO OF SUBJECTS FOR REVALUATION  : "))
        while (n < m):
            subc = input("Enter Subject  Code : ")
            subn = input("Enter Subject Name  :")
            n=n+1
            print("Your Request has been received  ")
        fees = 500*m
        print("Pay {} Fees in Account Section to proceed".format(fees))    
            
#ends here********************************************************************************            
#ends********************************************************************************************************************************************************
    @staticmethod
    def paint_data(data):
        table = BeautifulTable()
        table.column_headers = ["NAME", "USN", "SEMISTER", "DEPT","CONTACT"]
        table.append_row([data.name, data.usn, data.sem, data.dept,data.numb])
        print(table)

    @staticmethod
    def paint_data_list(data):
        table = BeautifulTable()
        table.column_headers = ["NAME", "USN", "SEMISTER", "DEPT","CONTACT"]
        for li in data:
            table.append_row([li.name, li.usn, li.sem, li.dept,li.numb])
        print(table)


    @staticmethod
    def paint_data(data):
        table = BeautifulTable()
        table.column_headers = ["NAME", "USN", "SUBJECT_CODE", "SUBJECT_NAME","MARKS","RESULT"]
        table.append_row([data.name, data.usn, data.subc, data.subn,data.marks.data.res])
        print(table)

    @staticmethod
    def paint_data_list1(data):
        table = BeautifulTable()
        table.column_headers = ["NAME", "USN", "SUBJECT_CODE", "SUBJECT_NAME","MARKS","RESULT"]
        for li in data:
            table.append_row([li.name, li.usn, li.subc, li.subn,li.marks,li.res])
        print(table)    


    @staticmethod
    def paint_data(data):
        table = BeautifulTable()
        table.column_headers = ["USN", "NAME","MARKS"]
        table.append_row([data.usn, data.name, data.cgpa])
        print(table)

    @staticmethod
    def paint_data_list2(data):
        table = BeautifulTable()
        table.column_headers = ["USN", "NAME","MARKS"]
        for li in data:
            table.append_row([li.usn, li.name, li.cgpa])
        print(table)
