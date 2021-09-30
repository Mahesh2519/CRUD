import psycopg2


print("Welocme to  CRUD Python_project made by Mahesh Dedge!\n")
print("Please choose one of the following opertion by Entering corresponding number: ")
print("1. Addition in the postgresql DB\n 2. Update postgres DB\n 3.Delete postgresql DB\n")

conn = psycopg2.connect(host="localhost",
                        database="py_project",
                        user="postgres",
                        password="qwerty@12345",
                        port="5432")


curr = conn.cursor()

curr.execute("SELECT * FROM CRUD")

crud = curr.fetchall()

for r in crud:
    print("id: ",r[0])
    print("Name: ",r[1])
    print("Surname: ",r[2], "\n")
#print(crud)

opertion = {1:"Addition", 2:"Update", 3:"Delete"}
optionChoice = int(input("Opertion required: "))
print("you've selected: ",opertion[optionChoice],".")

if optionChoice == 1:
    name = input('Enter first name: ')
    surname = input('Enter surname: ')

    curr.execute("INSERT INTO CRUD (name, surname) VALUES (%s,%s)",(name, surname))

    print("Data Added successfully!")

if optionChoice == 2:
    name = input('Enter First Name: ')
    surname = input('Enter Surname: ')
    id = input('Enter Serial Number')

    curr.execute("UPDATE CRUD SET name=%s, surname=%s WHERE sno=%s",(name,surname, id))
    print("update successful..!")

if optionChoice == 3:
    id = input('Enter Serial Number')

    curr.execute("DELETE FROM CRUD WHERE sno={}".format(id))
    print("Delete successful..!")


conn.commit()

curr.execute("SELECT * FROM CRUD")

crud = curr.fetchall()

print(crud)

conn.close()

print("Connection Closed.")
