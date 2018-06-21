# these should be the only imports you need
import sys
import sqlite3

# write your code here
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return None


def print_customer(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT  Id, CompanyName FROM Customer")

    rows = cur.fetchall()

    print("ID", "Customer")
    for row in rows:
        print(str(row[0]), str(row[1]))


def print_employees(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT  Id, FirstName, LastName FROM Employee")

    rows = cur.fetchall()

    print("ID", "Employee Name")
    for row in rows:
        print(str(row[0]), str(row[1]) +" "+ str(row[2]))

def print_ordersByCID(conn, CID):
    cur = conn.cursor()
    cur.execute('''SELECT OrderDate FROM "Order" WHERE CustomerId=?''',(CID,))

    rows = cur.fetchall()

    print("OrderDate")
    for row in rows:
        print(str(row[0]))

def print_ordersByELM(conn, LN):
    cur = conn.cursor()
    sqlCommand = ('''SELECT OrderDate FROM "Order","Employee" WHERE "Order".EmployeeId="Employee".Id AND "Employee".LastName="''' + str(LN) + '''"''')
    cur.execute(sqlCommand)

    rows = cur.fetchall()

    print("OrderDate")
    for row in rows:
        print(str(row[0]))

def main():
    database = "./Northwind_small.sqlite"

    # create a database connection
    conn = create_connection(database)

    if (len(sys.argv) > 1):
        with conn:
            if sys.argv[1] == "customers":
                 print_customer(conn)
            elif (sys.argv[1] == "employees"):
                print_employees(conn)
            elif (sys.argv[1] == "orders"):
                if (sys.argv[2][0]=="c"):
                    print_ordersByCID(conn, sys.argv[2][5:])
                elif (sys.argv[2][0]=="e"):
                    print_ordersByELM(conn, sys.argv[2][4:])
            else:
                print("Please Enter a correct argument")

    else:
        print("Please Enter a correct argument")


if __name__ == '__main__':
    main()
# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>
