from flask import Flask
app = Flask(__name__)
import psycopg2

@app.route('/<param>')
def lookup(param):
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	cur = conn.cursor()
	
	sql = "SELECT distinct value from decoded_lookup where key = %s" % (param)
	
	cur.execute(sql)
	
	value = cur.fetchone()

	return value

if __name__ == '__main__':
	app.run()