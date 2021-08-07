import mariadb as mc
import sys


try:
    mydb = mc.connect(
        host = "localhost",
        user = "root",
        password = "don",
        port = 3306,
        database = "super",
    )
except mc.Error as e:
    print("coulnot connect to db")
    sys.exit(1)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS inventory(ID INT AUTO_INCREMENT PRIMARY KEY,\
    item VARCHAR(100),\
    description VARCHAR(100),\
    unit_price VARCHAR(100),\
    quantity VARCHAR(100) )"
    )

mycursor.execute("CREATE TABLE IF NOT EXISTS sale(ID INT AUTO_INCREMENT PRIMARY KEY,\
    item VARCHAR(100),\
    description VARCHAR(100),\
    unit_price VARCHAR(100),\
    customer VARCHAR(100),\
    payment VARCHAR(100),\
    amount_due VARCHAR(100),\
    total VARCHAR(100),\
    date VARCHAR(100),\
    quantity VARCHAR(100) )"
    )
