import sqlite3

db = sqlite3.connect("phoneBook.db")


def getInput():
    while True:
        print("""
                1. Add number
                2. Delete number
                3. Edit number
                4. List number
                5. Exit
            """)

        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter the name : ")
            phoneNumber = int(input("Enter the number : "))
            insertData(name, phoneNumber)

        elif choice == 2:
            id = int(input("Enter the id : "))
            deleteData(id)

        elif choice == 3:
            id = int(input("Enter the id : "))
            name = input("Enter the name : ")
            phoneNumber = int(input("Enter the new number : "))

            updateData(name, phoneNumber, id)

        elif choice == 4:
            listUser()

        elif choice == 5:
            exit()

        else:
            print("Invalid selection")




def insertData(name, phoneNumber):
    query = "INSERT INTO phoneBook (NAME, NUMBER) VALUES (?, ?);"
    db.execute(query, (name, phoneNumber))
    db.commit()
    print("Data added successfully")


def deleteData(id):
    query = f"DELETE FROM phoneBook WHERE ID = {id};"
    db.execute(query)
    db.commit()
    print("Data deleted successfully")


def updateData(name, phoneNumber, id):
    query = "UPDATE phoneBook SET NAME = ?, NUMBER = ? WHERE ID = ?;"
    db.execute(query, (name, phoneNumber, id))
    db.commit()
    print("Data updated successfully")

def listUser():
    print("Your data\n")
    query = "SELECT * FROM phoneBook;"
    res = db.execute(query)
    for i in res:
        print(i)
    db.commit()



def main():
    getInput()

main()