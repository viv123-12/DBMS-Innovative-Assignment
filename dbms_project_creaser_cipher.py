# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:08:32 2022

@author: vivek
"""

import cx_Oracle


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
                password_enc = encrypt(password, 4)
                cursor.execute("select password from signup where (password ='" +
                               password_enc+"'And username='"+username+"')")
                result = cursor.fetchone()
                #print("Decrypted password:",decrypt(result,password))
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
            print("Want to create table:")
            print("1.yes")
            i = int(input())
            if(i==1): 
               cursor.execute(
                    "create table signup(username varchar2(20) primary key, password varchar2(15))")
            
            user_name = input("Enter the user name:")
            password = input("Enter the password:")
            password_enc = encrypt(password, 4)
            message = 'amit@123' #encrypted message
            LETTERS = 'qcyjjuvw'
            cursor.execute("insert into signup values('" +
                           user_name+"','"+password_enc+"')")
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
            print("Want to create table:")
            print("1.yes")
            i = int(input())
            if(i==1): 
                cursor.execute(
                    "create table Account(Account_no varchar2(10) primary key, Account_type varchar2(30) not null,Balance varchar2(10) not null)")
                cursor.execute("create table Customer(cust_id varchar2(20) primary key, Name varchar2(25) not null, Phone varchar2(10) not null, Account_no varchar2(10) ,Address varchar2(50) not null,username varchar2(20),FOREIGN KEY (username) REFERENCES signup(username),FOREIGN KEY (Account_no) REFERENCES Account(Account_no))")

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

    def encrypt(text, s):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr((ord(char) + s+65) % 26 + 65)
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s + 97) % 26 + 97)
        return result
    def decrypt(LETTERS,message):
        for key in range(len(LETTERS)):
           translated = ''
           for symbol in message:
              if symbol in LETTERS:
                 num = LETTERS.find(symbol)
                 num = num - key
                 if num < 0:
                    num = num + len(LETTERS)
                 translated = translated + LETTERS[num]
              else:
                 translated = translated + symbol
        return translated

manu()
