import mysql.connector

#establish connection
db_connect = mysql.connector.connect(user='root',
                              password='root123',
                              host='127.0.0.1',
                              database='python_sql')
cur = db_connect.cursor()

#read table
cur.execute("SELECT * FROM STUDENT")
for row in cur:
    print(row)

print("\n")
cur.execute("SELECT * FROM STUDENT WHERE MOBILENO REGEXP '98.*'")
for row in cur:
    print(row)

print("\n")
cur.execute("SELECT * FROM STUDENT WHERE MOBILENO REGEXP '0.*0.*0.*'")
for row in cur:
    print(row)
print("\n")

db_connect.commit()
db_connect.close()