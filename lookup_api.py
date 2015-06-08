from flask import Flask
from flask.ext.cors import CORS
app = Flask(__name__)
cors = CORS(app)
import psycopg2

@app.route('/<param>', methods=['GET'])
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
	
@app.route('/respondent/<respondent_id>', methods=['POST'])
def respondent(respondent_id):
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	cur = conn.cursor()
	
	sql = "insert into eligible_respondents(respondent_id) values(%s)" % (respondent_id)
	
	return cur.execute(sql)

@app.route('/card/<respondent_id>', methods=['POST'])
def card(respondent_id):
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	cur = conn.cursor()
	
	sql = str("select c.card_id "
			  "from cards c "
			  "left join claimed_cards cc on cc.card_id = c.card_id "
			  "where cc.row_id is null "
			  "and %s in (select distinct respondent_id from elibible_respondents)" % (respondent_id) +
			  "limit 1")
			  
	cur.execute(sql)
	
	card_id = cur.fetchone()
	
	insert_sql = "insert into claimed_cards(card_id, respondent_id) values(%s, %s)" % (card_id, respondent_id)
	
	cur.execute(insert_sql)
	

if __name__ == '__main__':
	app.run()