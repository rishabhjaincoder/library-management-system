#main program

import dl
from models import Category,Book,Student,Login,Teacher,IssuedRegister,ReturnedRegister
from datetime import date

def StudentUI():
    print("1. Create Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Logout")

    option=int(input("Enter your choice: "))
    if(option==1):
        print("\t\t\t CREATE PROFILE \t\t\t")
        name=input("Enter name: ")
        course=input("Enter course: ")
        email=input("Enter email-id: ")
        phone=int(input("Enter mobile number: "))
        address=input("Enter address: ")

        student=Student(name=name,course=course,email=email,phone=phone,address=address)
        add_student=dl.AddStudent(student)

        if(add_student==True):
            print("Hey "+student.name + " your profile is successfully added.")
        else:
            print( "Oops!!! "+student.name +" your profile is not added.Please Try Again.")

    if(option==2):
        print("\t\t\t UPDATE PROFILE \t\t\t")
        name=input("Enter name : ")
        o_email=input("Enter email-id(original) : ")
        course=input("Enter course: ")
        email=input("Enter email-id(updated): ")
        phone=int(input("Enter mobile number: "))
        address=input("Enter address: ")       

        student=Student(name=name,course=course,email=email,phone=phone,address=address)
        get_student=dl.GetStudent(name,o_email)
        update_student=dl.UpdateStudent(get_student[0],student)

        if(update_student==True):
            print("Hey "+student.name + " your profile is successfully updated.")
        else:
            print( "Oops!!! "+student.name +" your profile is not updated.Please Try Again.")

    if(option==3):#view profile
        print("\t\t\t VIEW PROFILE \t\t\t")
        name=input("Enter name : ")
        o_email=input("Enter email-id : ")
        get_student=dl.GetStudent(name,o_email)
        if(get_student!=None):
            print("Name: "+get_student[1])
            print("Course: "+get_student[2])
            print("Email: "+get_student[3])
            print("Phone: "+str(get_student[4]))
            print("Address: "+get_student[5])
            print()
        else:
            print( "Oops!!! your profile is not available. Please Try Again.")        

    if(option==4):#issue book
        print("\t\t\t ISSUE BOOK \t\t\t")
        name=input("Enter your name: ")
        email=input("Enter Email-Id: ")
        bname=input("Enter book name: ")
        display_book=dl.GetBook(bname)
        issuer_id=dl.GetStudent(name,email)
        issue_date=date.today()
        
        if(display_book[8]>0 and display_book[7]==0):
            stock=display_book[8]-1            
            update_stock=dl.UpdateStock(bname,stock)
            bid=display_book[0]
            issuerid=issuer_id[0]
            issuertype="S"
            issueddate=issue_date

            issuedregister=IssuedRegister(bid=bid,issuerid=issuerid,issuertype=issuertype,issueddate=issueddate)
            add_issued_register=dl.AddIssued(issuedregister)

            if(update_stock==True and add_issued_register==True ):
                print("Your book is issued. Kindly visit again.")
            else:
                print("Book not issued.Please Try Again.")

        else:
            print("Book not available.")

    if(option==5):#return book
        print("\t\t\t RETURN BOOK \t\t\t")
        name=input("Enter Name: ")
        email=input("Enter Email-Id: ")
        issuer_id=dl.GetStudent(name,email)
        issuertype="S"

        showissued=dl.GetIssued(issuer_id[0],issuertype)
        if(showissued!=None):
            print("\t\t\t LIST OF ISSUED BOOKS \t\t\t")
            for record in showissued:
                print()
                print("Book Name:"+record[0]+"\t\t Issue Date:"+str(record[1]))

            bname=input("Enter Book Name to be Returned: ")
            display_book=dl.GetBook(bname)
            bid=display_book[0]
            issuerid=issuer_id[0]
            issuertype="S"
            returneddate=date.today()
            issued_date=dl.GetIssued1(bid,issuerid)
            diff=returneddate-issued_date
            if(diff.days>14):
                fine=diff.days-14
            else:
                fine=0
            delete_register=dl.DeleteIssued(bid,issuerid)    
            returnedregister=ReturnedRegister(bid=bid,issuerid=issuerid,issuertype=issuertype,returneddate=returneddate,fine=fine)
            returned_register=dl.AddReturned(returnedregister)

            stock=display_book[8]+1            
            update_stock=dl.UpdateStock(bname,stock)            

            if(returned_register==True and update_stock==True and delete_register==True):
                print("You have successfully returned the book. Kindly visit again. ")
            else:
                print("Book not returned.")
        
    else:
        return False

    return True
def TeacherUI():
    print("1. Create Profile")
    print("2. Update Profile")
    print("3. View Profile")
    print("4. Issue Books")
    print("5. Return Books")
    print("6. Logout")

    option=int(input("Enter your choice: "))
    if(option==1):
        print("\t\t\t CREATE PROFILE \t\t\t")
        empid=input("Enter Employee id: ")        
        name=input("Enter name: ")
        dept=input("Enter department: ")


        teacher=Teacher(empid=empid,name=name,dept=dept)
        add_teacher=dl.AddTeacher(teacher)

        if(add_teacher==True):
            print("Hey "+teacher.name + " your profile is successfully added.")
        else:
            print( "Oops!!! "+teacher.name +" your profile is not added.Please Try Again.")

    if(option==2):
        print("\t\t\t UPDATE PROFILE \t\t\t")
        name=input("Enter name : ")
        o_empid=input("Enter Employee id:(original) : ")
        empid=input("Enter Employee id:(Updated): ")        
        dept=input("Enter department: ")     
        teacher=Teacher(empid=empid,name=name,dept=dept)
        get_teacher=dl.GetTeacher(name,o_empid)
        update_teacher=dl.UpdateTeacher(get_teacher[0],teacher)

        if(update_teacher==True):
            print("Hey "+teacher.name + " your profile is successfully updated.")
        else:
            print( "Oops!!! "+teacher.name +" your profile is not updated.Please Try Again.")

    if(option==3):#view profile
        print("\t\t\t VIEW PROFILE \t\t\t")
        name=input("Enter name : ")
        o_empid=input("Enter Employee-Id : ")
        get_teacher=dl.GetTeacher(name,o_empid)
        if(get_teacher!=None):
            print("Employee Id: "+str(get_teacher[1]))
            print("Name: "+get_teacher[2])
            print("Department: "+get_teacher[3])
            print()
        else:
            print( "Oops!!! your profile is not available. Please Try Again.")        

    if(option==4):#issue book
        print("\t\t\t ISSUE BOOK \t\t\t")
        name=input("Enter name : ")
        empid=input("Enter Employee-Id : ")        
        bname=input("Enter book name: ")
        display_book=dl.GetBook(bname)
        
        issuer_id=dl.GetTeacher(name,empid)
        issue_date=date.today()
        
        if(display_book[8]>0):
            stock=display_book[8]-1            
            update_stock=dl.UpdateStock(bname,stock)
            bid=display_book[0]
            issuerid=issuer_id[0]
            issuertype="T"
            issueddate=issue_date

            issuedregister=IssuedRegister(bid=bid,issuerid=issuerid,issuertype=issuertype,issueddate=issueddate)
            add_issued_register=dl.AddIssued(issuedregister)

            if(update_stock==True and add_issued_register==True ):
                print("Your book is issued. Kindly visit again.")
            else:
                print("Book not issued.Please Try Again.")

        else:
            print("Book not available.")

    if(option==5):#return book
        print("\t\t\t RETURN BOOK \t\t\t")
        name=input("Enter Name: ")
        email=input("Enter Employee-Id: ")
        issuer_id=dl.GetTeacher(name,empid)
        issuertype="T"

        showissued=dl.GetIssued(issuer_id[0],issuertype)
        if(showissued!=None):
            print("\t\t\t LIST OF ISSUED BOOKS \t\t\t")
            for record in showissued:
                print()
                print("Book Name:"+record[0]+"\t\t Issue Date:"+str(record[1]))

            bname=input("Enter Book Name to be Returned: ")
            display_book=dl.GetBook(bname)
            bid=display_book[0]
            issuerid=issuer_id[0]
            issuertype="T"
            returneddate=date.today()
            issued_date=dl.GetIssued1(bid,issuerid)
            diff=returneddate-issued_date
            if(diff.days>14):
                fine=diff.days-14
            else:
                fine=0
            delete_register=dl.DeleteIssued(bid,issuerid)    
            returnedregister=ReturnedRegister(bid=bid,issuerid=issuerid,issuertype=issuertype,returneddate=returneddate,fine=fine)
            returned_register=dl.AddReturned(returnedregister)

            stock=display_book[8]+1            
            update_stock=dl.UpdateStock(bname,stock)            

            if(returned_register==True and update_stock==True and delete_register==True):
                print("You have successfully returned the book. Kindly visit again. ")
            else:
                print("Book not returned.")
    else:
        return False

    return True
                
def LibrarianUI():
    print("1. Add New Book")
    print("2. Delete Book")
    print("3. Update Book Details")
    print("4. Display Books")
    print("5. Search Book")
    print("6. Fine Collection")
    print("7. Logout")

    option=int(input("Enter Your Choice: "))

    if(option==1):#add book
        print("\t\t\t ADD BOOK \t\t\t")
        name=input("Enter Book Name To Be Added: ")        
        cname=input("Enter Category Name: ")
        category=dl.GetCategory1(cname)
        cid=category[0]
        author=input("Enter Author: ")
        publisher=input("Enter Publisher: ")
        price=float(input("Enter Price: "))
        Exclusive=input("Is Book Exclusive:(1/0) ")
        Stock=int(input("Enter Stock: "))
        Pages=int(input("Enter Number of Pages: "))

        book=Book(cid=cid,name=name,author=author,publisher=publisher,price=price,Exclusive=Exclusive,Stock=Stock,Pages=Pages)
        add_book=dl.AddBook(book)
        if(add_book==True):
            print(book.name + " successfully added.")
        else:
            print( book.name +" not added.Please Try Again.")

    elif(option==2):#delete book
        print("\t\t\t DELETE BOOK \t\t\t")
        name=input("Enter Book name To Be Deleted: ")

        delete_book=dl.DeleteBook(name=name)
        if(delete_book==True):
            print("Book is deleted.")
        else:
            print("Book is not deleted. Please Try Again. ")
            
    elif(option==3):#update book
        print("\t\t\t UPDATE BOOK DETAILS \t\t\t")
        name=input("Enter Book Name to be updated: ")
        cname=input("Enter category name: ")
        author=input("Enter Author: ")
        publisher=input("Enter Publisher: ")
        price=float(input("Enter Price: "))
        Exclusive=input("Is Book Exclusive: ")
        Stock=int(input("Enter Stock: "))
        Pages=int(input("Enter Number of Pages: "))
        category=dl.GetCategory1(cname)
        cid=category[0]
        book=Book(cid=cid,name=name,author=author,publisher=publisher,price=price,Exclusive=Exclusive,Stock=Stock,Pages=Pages)
        update_book=dl.UpdateBook(book)

        if(update_book==True):
             print(book.name + " is updated.")
        else:
             print(book.name + "not updated.Please Try Again")
         
    elif(option==4):#Display Books on basis of categories
        print("\t\t\t VIEW BOOKS \t\t\t")
        cname=input("Enter category name: ")
        category=dl.GetCategory1(cname)
        cid=category[0]
        display_books=dl.GetBooks(cid)

        if(display_books!=None):
            for record in display_books:
                print("Name: "+record[2]+"\t"+"Category: "+cname+"\t"+"Author:"+record[3]+"\t"+"Publisher: "+record[4]+"\t"+"Price: "+str(record[5])+"\t"+"Pages: "+str(record[6])+"\t"+"Exclusive: "+str(record[7])+"\t"+"Stock: "+str(record[8]))
        else:
            print("Books not available.Please try again.")
            
    elif(option==5):#Search Book
        print("\t\t\t SEARCH BOOK \t\t\t")
        name=input("Enter book name: ")
        display_book=dl.GetBook(name)

        if(display_book!=None):
            category=dl.GetCategory2(display_book[1])
            cname=category[1]            
            print("Name: "+display_book[2]+"\t"+"Category: "+cname+"\t"+"Author:"+display_book[3]+"\t"+"Publisher: "+display_book[4]+"\t"+"Price: "+str(display_book[5])+"\t"+"Pages: "+str(display_book[6])+"\t"+"Exclusive: "+str(display_book[7])+"\t"+"Stock: "+str(display_book[8]))
        else:
            print("Book not available.Please try again.")         

    elif(option==6):#Check Fine Collection
        Totalfine=dl.CheckFine()
        print("Total fine collected is: "+str(Totalfine))
        
     

    elif(option==7):#Logout
        return False

    return True
    
        
        
            
def MainMenu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    #code

    option=int(input("Enter Your Choice: "))
    if(option==1):
        username=input("Enter Username: ")
        password=input("Enter password: ")
        usertype=input("Enter Type (L/T/S): ")

        login=Login(username=username,password=password,usertype=usertype)
        dl.AddLogin(login)

    elif(option==2):
        username=input("Username: ")
        password=input("Password: ")

        login=dl.Getlogin(username,password)

        if(login!=None):
            if(login[3]=='T'):
                while TeacherUI():
                    pass                    
            elif(login[3]=='L'):
                while LibrarianUI():
                    pass
            else:
                while StudentUI():
                    pass
                
        else:
            print("Invalid Usename or password")
            return False        
while True:
    MainMenu()
