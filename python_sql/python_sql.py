import mysql.connector
cnx = mysql.connector.connect(user='root',
                              password='root123',
                              host='127.0.0.1',
                              database='python_sql')

cur = cnx.cursor()
#create table
cur.execute("""CREATE TABLE STUDENT(
            ROLLNO INT,
            NAME VARCHAR(20),
            MOBILENO VARCHAR(20)
);""")

#insert records
records=[
            [1,'ram','9965021078'],
            [2,'ramu','9965021070'],
            [3,'ramesh','9865031078'],
            [4,'rashmi','9800021077']
]
for rollno, name, mobileno in records:
    query = "INSERT INTO STUDENT VALUES(" +\
            str(rollno) + ","+\
            repr(name) +","+\
            repr(mobileno)+");"
    print(query)
    cur.execute(query)

cnx.commit()
cnx.close()