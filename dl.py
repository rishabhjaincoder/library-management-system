
#Data Logic File

#Global Variables and Modules
import MySQLdb
from models import Category
from models import Book

con=MySQLdb.connect('localhost',user='root',password='')
con.select_db('lms')
cur=con.cursor()

#Category Table--------------------------------------------------------------------------

def AddCategory(category):
	query="INSERT INTO CATEGORY(name,description) values(%s,%s)"
	result=cur.execute(query,(category.name,category.description))
	con.commit()
	if(result>0):
		return True
	else:
		return False



def DeleteCategory(cid):
	query="DELETE FROM CATEGORY WHERE ID="+cid
	result=cur.execute(query)
	con.commit()
	if(result>0):
		return True
	else:
		return False


def UpdateCategory(category):
	query="UPDATE CATEGORY SET NAME=%s, DESCRIPTION=%s  WHERE ID=%s"
	result=cur.execute(query,(category.name,category.description,category.cid))
	con.commit()
	if(result>0):
		return True
	else:
		return False


def GetCategories():
	query="SELECT * FROM CATEGORY"
	result=cur.execute(query)
	data=cur.fetchall()
	categories=[]
	for record in data:
		c=Category(record[0],record[1],record[2])
		categories.append(c)

	return categories


def GetCategory(cid):
	query="SELECT * FROM CATEGORY WHERE ID="+cid
	result=cur.execute(query)
	data=cur.fetchone()
	c=Category(record[0],record[1],record[2])
	return c

def GetCategory1(cname):
	query=("SELECT * FROM CATEGORY WHERE name='"+cname+"'")
	result=cur.execute(query)
	record=cur.fetchone()
	return record

def GetCategory2(cid):
	query=("SELECT * FROM CATEGORY WHERE id='"+str(cid)+"'")
	result=cur.execute(query)
	record=cur.fetchone()
	return record

# Book Table---------------------------------------------------------------------

def AddBook(book):
	query="INSERT INTO books(cid,name,author,publisher,price,Exclusive,Stock,Pages)values(%s,%s,%s,%s,%s,%s,%s,%s)"
	result=cur.execute(query,(book.cid,book.name,book.author,book.publisher,book.price,book.Exclusive,book.Stock,book.Pages))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def DeleteBook(name):
	query="DELETE FROM books WHERE name='"+name+"'"
	result=cur.execute(query)
	con.commit()
	if(result>0):
		return True
	else:
		return False

def UpdateBook(book):
	query="UPDATE books SET cid=%s,name=%s, author=%s ,publisher=%s,price=%s,Exclusive=%s,Stock=%s,pages=%s WHERE name=%s"
	result=cur.execute(query,(book.cid,book.name,book.author,book.publisher,book.price,book.Exclusive,book.Stock,book.Pages,book.name))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def GetBooks(cid):
	query="SELECT * FROM books WHERE cid='"+str(cid)+"'"
	result=cur.execute(query)
	data=cur.fetchall()
	showbooks=[]
	for record in data:
		c=[record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]]
		showbooks.append(c)

	return showbooks


def GetBook(name):
	query="SELECT * FROM books WHERE name='"+name+"'"
	result=cur.execute(query)
	data=cur.fetchone()
	return data

def UpdateStock(name,stock):
	query="UPDATE books SET Stock=%s WHERE name=%s"
	result=cur.execute(query,(stock,name))
	con.commit()
	if(result>0):
		return True
	else:
		return False        
        
#login table-------------------------------------------------------------------------------

def AddLogin(login):
	query="INSERT INTO login(username,password,usertype) values(%s,%s,%s)"
	result=cur.execute(query,(login.username,login.password,login.usertype))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def Getlogin(username,password):
	query=("SELECT * FROM login WHERE username=%s and password=%s")
	result=cur.execute(query,(username,password))
	record=cur.fetchone()
	return record	

#-----------Student Table---------------------------------------------------------------------

def AddStudent(student):
	query="INSERT INTO student(name,course,email,phone,address)values(%s,%s,%s,%s,%s)"
	result=cur.execute(query,(student.name,student.course,student.email,student.phone,student.address))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def UpdateStudent(id,student):
	query="UPDATE student SET name=%s, course=%s ,email=%s,phone=%s,address=%s WHERE id=%s"
	result=cur.execute(query,(student.name,student.course,student.email,student.phone,student.address,id))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def GetStudent(name,o_email):
	query="SELECT * FROM student WHERE name=%s and email=%s"
	result=cur.execute(query,(name,o_email))
	data=cur.fetchone()
	return(data) 
	
#-----------Teacher Table---------------------------------------------------------------------

def AddTeacher(teacher):
	query="INSERT INTO teacher(empid,name,dept)values(%s,%s,%s)"
	result=cur.execute(query,(teacher.empid,teacher.name,teacher.dept))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def UpdateTeacher(id,teacher):
	query="UPDATE teacher SET empid=%s, name=%s, dept=%s  WHERE id=%s"
	result=cur.execute(query,(teacher.empid,teacher.name,teacher.dept,id))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def GetTeacher(name,o_empid):
	query="SELECT * FROM teacher WHERE name=%s and empid=%s"
	result=cur.execute(query,(name,o_empid))
	data=cur.fetchone()
	return(data) 
#Issuedregister---------------------------------------------------------------------------------------

def AddIssued(issuedregister):
	query="INSERT INTO issuedregister(bid,issuerid,issuertype,issueddate)values(%s,%s,%s,%s)"
	result=cur.execute(query,(issuedregister.bid,issuedregister.issuerid,issuedregister.issuertype,issuedregister.issueddate))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def GetIssued(id,type):
	query="SELECT * FROM issuedregister WHERE issuerid=%s and issuertype=%s"
	result=cur.execute(query,(id,type))
	data=cur.fetchall()
	showbooks=[]
	for record in data:
		issue=Issued_1(record[1])
		c=[issue[2],record[4]]
		showbooks.append(c)
                
	return(showbooks)

def Issued_1(id):
	query="SELECT * FROM books WHERE id=%s"
	result1=cur.execute(query,(id,))
	issue=cur.fetchone()
	return(issue)        

def GetIssued1(bid,issuerid):
	query="SELECT * FROM issuedregister WHERE bid=%s and issuerid=%s"
	result1=cur.execute(query,(bid,issuerid))
	issue=cur.fetchone()
	return(issue[4])

def DeleteIssued(bid,issuerid):
	query="DELETE FROM issuedregister WHERE bid=%s and issuerid=%s"
	result=cur.execute(query,(bid,issuerid))
	con.commit()
	if(result>0):
		return True
	else:
		return False
#Returnedregister---------------------------------------------------------------------------------------

def AddReturned(returnedregister):
	query="INSERT INTO returnedregister(bid,issuerid,issuertype,returneddate,fine)values(%s,%s,%s,%s,%s)"
	result=cur.execute(query,(returnedregister.bid,returnedregister.issuerid,returnedregister.issuertype,returnedregister.returneddate,returnedregister.fine))
	con.commit()
	if(result>0):
		return True
	else:
		return False

def CheckFine():
        query="SELECT * FROM returnedregister"
        result=cur.execute(query)
        con.commit()
        data=cur.fetchall()
        total_fine=0
        for record in data:
                total_fine=total_fine+record[5]
        return total_fine        
