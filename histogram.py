#!/usr/bin/python

import sys
import psycopg2

def main():
        conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
 
	cur = conn.cursor()

        #check if script got two arguments
        if len(sys.argv)==3:
	     cur.execute("SELECT * FROM tweetwordcount WHERE count>=%s AND count<=%s",(sys.argv[1],sys.argv[2]))
             records = cur.fetchall()
             print(records)
        else:
             print 'This task requires 2 arguments.'
 
if __name__ == "__main__":
	main()
