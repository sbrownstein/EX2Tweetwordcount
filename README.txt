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



