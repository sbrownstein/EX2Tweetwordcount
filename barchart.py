import plotly.plotly as py
import plotly.graph_objs as go

import psycopg2

conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()

data = [go.Bar(
            x=cur.execute("SELECT word FROM tweetwordcount ORDER BY count desc LIMIT 20"),
            y=cur.execute("SELECT count FROM tweetwordcount ORDER BY count desc LIMIT 20")
    )]

py.iplot(data, filename='basic-bar')



