import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'login_database.db')

class login_db:


	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='login_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE login_table(

					username text,
					password text,
					unique_id int

				)""")

		conn.commit()
		conn.close()



	@classmethod
	def insert_record(cls, details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO login_table VALUES (?,?,?)", details)


		conn.commit()
		conn.close()



	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT * FROM login_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records



	@classmethod
	def get_record_by_username(cls, username_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT * FROM login_table WHERE username = ?", (username_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record


