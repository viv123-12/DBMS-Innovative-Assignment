# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:08:32 2022

@author: vivek
"""

import cx_Oracle
import math


try:
    con = cx_Oracle.connect('system/vivek@localhost:1521/xe')
except cx_Oracle.DatabaseError as e:
    print('There is problem with Oracle', e)
else:
    def manu():
        print("1.Sign up for new account:")
        print("2.sign in:")
        print("3.new account:")
        i = int(input("Select the choice:"))
        #signup for new account
        if (i == 1):
            signup()
            
            
            # log in and get the information from the id
        elif(i == 2):
            try:
                cursor = con.cursor()
                username = input("Enter your username:")
                password = input("Enter password:")
                password_enc=encrypt(public,password)
                enc=''
                for i in range(len(password_enc)):
                    enc=enc+str(password_enc[i])+','
                name = enc[:-1]
                print("Encrypted data",name)
                cursor.execute("select password from signup where (password ='" +
                               name+"'And username='"+username+"')")
                result = cursor.fetchone()
                if result == None:
                    print("No match is there!")
                   # print("Decrypted password:",decrypt(private,name))
                else:
                   cursor.execute("select * from customer where username='"+username+"'")
                   customer = cursor.fetchone()
                   print("Customer details are:")
                   print(customer)
            except cx_Oracle.DatabaseError as e:
                print("There are problem with Oracle", e)
            else:
                con.commit()
            finally:
                if cursor:
                    cursor.close()
                if con:
                    con.close()

        elif (i == 3):
            newaccout()
    # sign up for new registration

    def signup():
        try:
            cursor = con.cursor()
            #cursor.execute(
             #   "create table signup(username varchar2(20) primary key, password varchar2(15))")
            user_name = input("Enter the user name:")
            password = input("Enter the password:")
            password_enc=encrypt(public,password)
            enc=''
            for i in range(len(password_enc)):
                enc=enc+str(password_enc[i])+','
            name = enc[:-1]
            cursor.execute("insert into signup values('" +
                           user_name+"','"+name+"')")
            print("Table printed successfully")
        except cx_Oracle.DatabaseError as e:
            print("There are problem with Oracle", e)
        else:
            con.commit()
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def newaccout():
        try:
            cursor = con.cursor()
            Account_no = input("Enter the account number:")
            print("select the account type:")
            i = int(input("1.saving\n2.Current\n"))
            if(i == 1):
                Account_type = "Saving"
            else:
                Account_type = "Current"
            Balance = int(input("Intial balance is:"))
            if(Balance < 1000):
                print("You are not eligible:")
                quit()
            balance = str(Balance)
           # cursor.execute(
           #     "create table Account(Account_no varchar2(10) primary key, Account_type varchar2(30) not null,Balance varchar2(10) not null)")
           # cursor.execute("create table Customer(cust_id varchar2(20) primary key, Name varchar2(25) not null, Phone varchar2(10) not null, Account_no varchar2(10) ,Address varchar2(50) not null,username varchar2(20),FOREIGN KEY (username) REFERENCES signup(username),FOREIGN KEY (Account_no) REFERENCES Account(Account_no))")

            cust_id = input("Enter the cust_id:")
            username=input("Enter the user name here:")
            Name = input("Enter the Name of account holder:")
            Phone = input("Enter the Phone:")
            Address = input("Enter the address here:")
            cursor.execute("insert into Account values('" +
                           Account_no+"','"+Account_type+"','"+balance+"')")
            cursor.execute("insert into Customer values('"+cust_id +
                           "','"+Name+"','"+Phone+"','"+Account_no+"','"+Address+"','"+username+"')")

            print("Data entered successfully")

        except cx_Oracle.DatabaseError as e:
            print("There are problems with Oracle", e)
        else:
            con.commit()
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

  
   
   #Encryption
  
    def encrypt(pub_key,n_text):
       e,n=pub_key
       x=[]
       m=0
       for i in n_text:
           if(i.isupper()):
               m = ord(i)-65
               c=(m**e)%n
               x.append(c)
           elif(i.islower()):               
               m= ord(i)-97
               c=(m**e)%n
               x.append(c)
           elif(i.isspace()):
               spc=400
               x.append(400)
       return x
        
    
   #Decryption
  
    def decrypt(priv_key,c_text):
       d,n=priv_key
       txt=c_text.split(',')
       x=''
       m=0
       for i in txt:
           if(i=='400'):
               x+=' '
           else:
               m=(int(i)**d)%n
               m+=65
               c=chr(m)
               x+=c
       return x
    
 
  


p = 7
q = 11
#RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n = p * q
print("RSA Modulus(n) is:",n)
 
#Eulers Toitent

r= (p-1)*(q-1)
#print("Eulers Toitent(r) is:",r)
#print("*****************************************************")
 
#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
     while(r!=0):
        e,r=r,e%r
     return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
       
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
 

for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("The value of e is:",e)
print("*****************************************************")
 

print("EUCLID'S ALGORITHM:")
eugcd(e,r)
print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
print("*****************************************************")
print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e,r)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("The value of d is:",d)
print("*****************************************************")
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("*****************************************************")
manu()
