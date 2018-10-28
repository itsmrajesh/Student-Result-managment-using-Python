if __name__ == '__main__':
        from contactservice import ContactService
        cs=ContactService()
    
        while True:
            
            print("*"*80)
            print("WELCOME TO STUDENT RESULT MANAGEMENT ")
            print("*"*80)
            print(" 1.ADD/REGESTER NEW STUDENT\n 2.UPADTE DETAILS OF EXISTING STUDENT\n 3.ADD STUDENT RESULTS(ADMIN)\n 4.SHOW ALL RESULTS(ADMIN)\n 5.RESULTS\n 6.RV\n 7.Show all Students Details\n 8.EXIT ")
            choice = int(input("Please Enter your Choice for following (1~8) :"))    
            if choice == 1:
                cs.add_student()
            elif choice == 2:
                cs.update_student()
            elif choice == 3:
                cs.add_result()
            elif choice == 5:
                cs.search_usn()
            elif choice == 4:
                    user=input("Enter username :")
                    pwd=input("Enter Password :")
                    if user =='ncet' and pwd =='ncet' :
                            cs.show_all_result()
                    else:
                            print("Invalid Login")
            elif choice == 6:
                cs.apply_rv()
            elif choice == 7:
                    cs.show_all_contacts()
            elif choice == 8:
                    exit()
            else:
                print("Enter 1 to 7 .....")
        
    
     
