from flask import Flask
from flask.ext.cors import CORS
app = Flask(__name__)
cors = CORS(app)
import psycopg2
import logging
from logging.handlers import RotatingFileHandler

@app.route('/<param>', methods=['GET'])
def lookup(param):
	app.logger.info('Info')
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	cur = conn.cursor()
	
	sql = "SELECT distinct value from decoded_lookup where key = %s" % (param)
	
	try:
		cur.execute(sql)
		value = cur.fetchone()
		return value
	except psycopg2.Error, e:
		app.logger.error(e.pgerror)


@app.route('/respondent/<respondent_id>', methods=['POST'])
def respondent(respondent_id):
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	cur = conn.cursor()
	
	sql = "insert into eligible_respondents(respondent_id) values(%s)"
	data = (respondent_id,)
	
	try:
		cur.execute(sql, data)
		conn.commit()
		return "200"
	except psycopg2.Error, e:
		app.logger.error(e.pgerror)


@app.route('/card/<respondent_id>', methods=['POST'])
def card(respondent_id):
	conn = psycopg2.connect("dbname='edjo_lookup' " + \
	                        "user='flask_user' " + \
	                        "host='127.0.0.1' " + \
	                        "password='password'")

	card_id = 0
	
	cur = conn.cursor()
	
	sql = str("select cc.card_id " 
	          "from claimed_cards cc "
	          "where cc.respondent_id = %s ")
	
	data = (respondent_id,)
	
	try:
		cur.execute(sql, data)
		card_id = cur.fetchone()
		if card_id != 0:
			return card_id
	except psycopg2.Error, e:
		app.logger.error(e.pgerror)

	sql = str("select c.card_id "
			  "from cards c "
			  "left join claimed_cards cc on cc.card_id = c.card_id "
			  "where cc.row_id is null "
			  "and %s in (select distinct respondent_id from eligible_respondents) "
			  #"and %s not in (select distinct respondent_id from claimed_cards) "
			  "limit 1")
	
	data = (respondent_id,)
	
	try:
		cur.execute(sql, data)
		card_id = cur.fetchone()
	except psycopg2.Error, e:
		app.logger.error(e.pgerror)

	insert_sql = "insert into claimed_cards(card_id, respondent_id) values(%s, %s)" 
	insert_data = (card_id, respondent_id)
	
	try:
		cur.execute(insert_sql, insert_data)
		conn.commit()
		return card_id
	except psycopg2.Error, e:
		app.logger.error(e.pgerror)

	
	

if __name__ == '__main__':
	handler = RotatingFileHandler('flask.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run()