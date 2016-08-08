Samantha Brownstein
UC Berkeley School of Information, MIDS Program
W205 Storing and Retrieving Data: Summer 2016
Exercise 2: Real Time Data Processing Using Apache Storm
Last Updated: August 8, 2016


Instructions for running this application:

Step 1. Clear existing table contents

     a. As user w205, log into postgres. psql --host=localhost --username=w205 --password --dbname=tcount
     b. Delete existing tweetwordcount table contents. TRUNCATE TABLE tweetwordcount;
     c. Disconnect from postgres. \q

Step 2. Run the EX2Tweetwordcount project

     a. cd EX2Tweetwordcount/
     b. sparse run
     c. Cancel application after allowing it to run for desired amount of time. CTRL+C

Step 3. Run queries

     a. To find the number of occurrences of a specific word in the stream, run the finalresults script.
        python finalresults.py <word>
     b. For a list of all words in the stream and their total count of occurrences, run the finalresults
        script with no argument. python finalresults.py
     c. For a list of all words with counts between two integers k1 and k2, run the histogram.py script.
        python histogram.py k1 k2





