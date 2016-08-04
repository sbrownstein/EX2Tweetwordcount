from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

conn = psycopg2.connect(database="Tcount", user="w205", password="", host="localhost", port="5432")

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
      
        # From psycopg-sample, create db
        try:
             cur = conn.cursor()
             cur.execute("CREATE DATABASE Tcount")
             cur.close()
             conn.commit()
             conn.close()
        except:
             print "Could not create Tcount"​
 
        # From psycopg-sample, create cursor and table
        cur = conn.cursor()
        cur.execute('''CREATE TABLE Tweetwordcount
             (word TEXT PRIMARY KEY     NOT NULL,
             count INT     NOT NULL);''')
        conn.commit()
        
        # If word is new, insert word and count
        # Else, update table with new count
        if self.counts[word] == 1:
             cur.execute("INSERT INTO Tweetwordcount (word, count) \
                   VALUES (%s, 1)", (word))
        else: cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (word, self.counts[word])

        conn.commit()

        conn.close()


