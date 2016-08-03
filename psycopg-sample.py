#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")


try:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.close()
except:
    print "Could not create tcount"


#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount
            (word TEXT PRIMARY KEY NOT NULL,
             count INT NOT NULL);''')


conn.commit()
conn.close()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()

#Insert
cur.execute("INSERT INTO tweetwordcount (word,count) \
      VALUES ('test', 1)");
conn.commit()

#Update
#Assuming you are passing the tuple (uWord, uCount) as an argument
cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
conn.commit()

#Select
cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
