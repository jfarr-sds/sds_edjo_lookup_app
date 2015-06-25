import psycopg2


conn = psycopg2.connect("dbname='edjo_lookup' " + \
						"user='flask_user' " + \
						"host='127.0.0.1' " + \
						"password='password'")
						
cur = conn.cursor()

cur.execute("SELECT * from decoded_lookup limit 10")

rows = cur.fetchall()

print rows[0]

