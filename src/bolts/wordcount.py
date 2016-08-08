from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        #self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")

        cur = conn.cursor()

        #start fresh table
        #cur.execute("TRUNCATE TABLE tweetwordcount;")
         
        # If word is new, insert word and set count = 1
        # Else, update table with new count
        if self.counts[word] == 1:
             query = "INSERT INTO tweetwordcount VALUES (%s, 1);"
             cur.execute(query, (word,))
        else: cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s;", (self.counts[word], word))
        
        conn.commit()

        conn.close()


