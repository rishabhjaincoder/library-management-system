
#Database Models

class Category:
	def __init__(self,cid=None,name=None,desc=None):
		self.cid=cid
		self.name=name
		self.description=desc

class Book:
	def __init__(self,id=None,cid=None,name=None,author=None,publisher=None,price=None,Exclusive=None,Stock=None,Pages=None):
		self.id=id
		self.cid=cid
		self.name=name
		self.author=author
		self.publisher=publisher
		self.price=price
		self.Exclusive=Exclusive
		self.Stock=Stock
		self.Pages=Pages

class Student:
	def __init__(self,id=None,name=None,course=None,email=None,phone=None,address=None):
		self.id=id
		self.name=name
		self.course=course
		self.email=email
		self.phone=phone
		self.address=address

class Teacher:
	def __init__(self,id=None,empid=None,name=None,dept=None):
		self.id=id
		self.empid=empid
		self.name=name
		self.dept=dept
		

class Login:
        def __init__(self,username=None,password=None,usertype=None):
                self.username=username
                self.password=password
                self.usertype=usertype


class IssuedRegister:
        def __init__(self,id=None,bid=None,issuerid=None,issuertype=None,issueddate=None):
                self.id=id
                self.bid=bid
                self.issuerid=issuerid
                self.issuertype=issuertype
                self.issueddate=issueddate

class ReturnedRegister:
        def __init__(self,id=None,bid=None,issuerid=None,issuertype=None,returneddate=None,fine=None):
                self.id=id
                self.bid=bid
                self.issuerid=issuerid
                self.issuertype=issuertype
                self.returneddate=returneddate
                self.fine=fine
        

                
