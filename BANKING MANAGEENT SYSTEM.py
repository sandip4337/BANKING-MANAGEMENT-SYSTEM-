import mysql.connector
from datetime import datetime


global mydb , cursor
mydb = mysql.connector.connect(host='localhost', database='banking_system', user='root', password='S@ndip4337')
cursor = mydb.cursor()

def clear():
    for _ in range(5):
        print()

def login():

    while True:
        clear()
        uname = input('Enter your name :')
        upass = input('Enter your Password :')
        cursor.execute('select * from login where username="{}" and password ="{}"'.format(uname, upass))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows != 1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            break

def add_account():

    clear()

    adharno = input("enter adhaar no:")

    sql1 = "select count(AADHAR) from customer;"

    cursor.execute(sql1)

    r = cursor.fetchone()

    sql = "select AADHAR from customer;"

    cursor.execute(sql)

    l = []

    for i in range(r[0]):

        a = cursor.fetchone()
        l.append(a[0])

    if adharno in l:

        print("sorry , your account exits:")

    else:

        name = input("enter name:")
        dob = input("enter date of birth (yyyy-mm-dd):")

        conctno = input("enter your contact no:")
        opening_bal = input("enter opening balance")

        print("Select account type")
        print("1. Savings\n 2. Current\n")

        choice = int(input("enter your choice"))
        ac_type = ''

        if choice == 1:
            ac_type = "svg"
        if choice == 2:
            ac_type = "cur"

        sql = 'insert into customer(Name ,DOB , CONT , OPENING_BAL, ACC_TYPE, AADHAR, CUR_BAL, ACNT_STAT) values("' +name+ '" , "' +dob+ '" , "' +conctno+ '" , '+opening_bal+' ,"' +ac_type+ '" , "' +adharno+ '" , '+opening_bal+' ,"open");'

        cursor.execute(sql)

        print('\n\nyour account added successfully')

def delete_ac():

    clear()

    acno = input('Enter customer Account No :')
    sql = 'update customer set ACNT_STAT = "close" where ACC_NO  =' + acno + ';'
    cursor.execute(sql)
    print('\n\n your Account closed successfully')


def check_exist(ac_no):

    sql1 = "select count(ACC_NO) from customer;"

    cursor.execute(sql1)

    r = cursor.fetchone()

    sql = "select ACC_NO from customer;"

    cursor.execute(sql)

    l = []

    for i in range(r[0]):
        a = cursor.fetchone()
        l.append(a[0])

    if int(ac_no) in l:

        return True

    else:

        return False

def update_acno():

    clear()

    acno = input('Enter customer Account No :')

    r = check_exist(acno)

    if r == True:

        print("-------------------")
        print("1. Update Name\n "
              "2. Update Date of Birth\n "
              "3. Update Contact No " )

        c = int(input("choose any of (1/2/3):"))

        if c == 1:

            name = input("enter new name:")

            sql = 'update customer set Name = "' +name+ '" where ACC_NO  =' + acno + ';'

            cursor.execute(sql)

            print("your name is updated successfully")

        elif c == 2:

            dob = input("enter new dob:")

            sql = 'update customer set DOB = "' + dob + '" where ACC_NO  =' + acno + ';'

            cursor.execute(sql)

            print("your dob is updated successfully")

        elif c == 3:

            cont = input("enter new contact no:")

            sql = 'update customer set CONT = "' + cont + '" where ACC_NO  =' + acno + ';'

            cursor.execute(sql)

            print("your contact no is updated successfully")

    else:

        print("your account no does not exits")

def balanace_enquary(acno):

    r = check_exist(acno)

    if r == True:

        sql = 'select CUR_BAL from customer where ACC_NO  =' + acno + ';'

        cursor.execute(sql)

        r = cursor.fetchone()

        list(r)

        return (r[0])


    else:

        print("your account no does not exits")


def account_detail():



    acno = input('Enter customer Account No :')

    r = check_exist(acno)

    if r == True:

        sql = 'select * from customer where ACC_NO  =' + acno + ';'

        cursor.execute(sql)

        r = cursor.fetchone()

        print("your acount details are:", r)


def add_balace():

    clear()

    acno = input('Enter customer Account No :')

    r = check_exist(acno)

    if r == True:

        bal = float(input("How much money you want to ADD:"))

        u = balanace_enquary(acno)

        total = bal + u

        entry_date_time = datetime.now()

        dt_string = entry_date_time.strftime("%Y-%m-%d %H:%M:%S")

        sql = 'insert into transction(ACC_NO,DT_TM,CREDITED,BALANCE) VALUES (' + acno + ' , "' + dt_string + '" , ' + str(
            bal) + ',' + str(int(total)) + ');'

        cursor.execute(sql)

        sql = 'update customer set CUR_BAL = ' + str(int(total)) + ' where ACC_NO  =' + acno + ';'

        cursor.execute(sql)

        print("balance added successfully")

    else:

        print("This accountno does not exists!!")

def withdraw_balance():

    clear()

    acno = input('Enter customer Account No :')

    r = check_exist(acno)

    if r == True:

        bal = float(input("How much money you want to withdraw:"))

        u = balanace_enquary(acno)

        if bal <= u:

            total = u - bal

            entry_date_time = datetime.now()

            dt_string = entry_date_time.strftime("%Y-%m-%d %H:%M:%S")

            sql = 'insert into transction(ACC_NO,DT_TM,DEBITED,BALANCE) VALUES (' + acno + ' , "' + dt_string + '" , ' + str(
                bal) + ',' + str(int(total)) + ');'

            cursor.execute(sql)

            sql = 'update customer set CUR_BAL = ' + str(int(total)) + ' where ACC_NO  =' + acno + ';'

            cursor.execute(sql)

            print("balance withdrawn successfully")

        else:
            print("SORRY! You don't have sufficient money in your account.")

    else:
        print("your account does not exit")


def passbookprint():

    clear()

    acno = input('Enter customer Account No :')

    r = check_exist(acno)

    if r == True:

        sql = 'select * from transction where ACC_NO  =' + acno + ';'

        cursor.execute(sql)

        r = cursor.fetchall()

        print(" ID ACC_NO            YYYY-MM-DD HH-MM-SS            DEBITED  CREDITED  BALANCE")

        for i in r:

            print(i)

    else:
        print("your account does not exit")


def main_menu():

    login()

    while True:
        clear()
        print(' B A N K I N G  M A N A G E M E N T  S Y S T E M ')
        print('*' * 100)
        print("\n1. ADD ACCOUNT")
        print("\n2.  DELETE ACCOUNT")
        print('\n3.  MODIFY ACCOUNT')
        print('\n4.  BALANCE ENQUERY')
        print('\n5.  ACCOUNT DETAILS ')
        print('\n6.  ADD MONEY ')
        print('\n7.  WITHDRAW MONEY ')
        print('\n8.  Passbook Print ')
        print('\n9.  Close application')
        print('\n\n')

        choice = int(input('Enter your choice ...: '))

        if choice == 1:
            add_account()

        if choice == 2:
            delete_ac()

        if choice == 3:
            update_acno()

        if choice == 4:

            a = input('Enter customer Account No :')
            print("Your acccount balance is :",balanace_enquary(a))


        if choice == 5:

            account_detail()

        if choice == 6:

            add_balace()

        if choice == 7:

            withdraw_balance()

        if choice == 8:

            passbookprint()

        if choice == 9:
            break




if __name__ == "__main__":
   main_menu()