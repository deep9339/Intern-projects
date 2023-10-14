import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'hall_workers_database.db')

class hall_workers_db:

	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='hall_workers_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE hall_workers_table(
				
				
				name text,
				salary int,
				attendance int,
				days int,
				hall_id int,
				hall_name text
					
				)""")

		conn.commit()
		conn.close()


	@classmethod
	def insert_record(cls,details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO hall_workers_table VALUES (?,?,?,?,?,?)", details)


		conn.commit()
		conn.close()


	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_workers_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_records_by_hall_name(cls,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_workers_table WHERE hall_name = ?", (nam,))
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records

	





