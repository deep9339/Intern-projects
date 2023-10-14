import sqlite3 as sqlite
import os
dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'hall_database.db')

class hall_db:


	@classmethod
	def create_table(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='hall_table'  ")

		if c.fetchone()[0] == 0 :

			c.execute(""" CREATE TABLE hall_table(

					name text,
					status text,
					single_room_count int,
					double_room_count int,
					single_room_occupancy int,
					double_room_occupancy int,
					single_room_rent real,
					double_room_rent real,
					warden_name text,
					warden_password text,
					warden_salary real,
					mess_manager_name text,
					mess_manager_password text,
					clerk_name int,
					clerk_password text,
					clerk_salary real,
					amenities_charge real

				)""")
		

		conn.commit()
		conn.close()



	@classmethod
	def insert_record(cls,details):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("INSERT INTO hall_table VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", details)


		conn.commit()
		conn.close()


	@classmethod
	def get_all_records(cls):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_table")
		records = c.fetchall()


		conn.commit()
		conn.close()

		return records


	@classmethod
	def get_record_by_name(cls, name_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_table WHERE name = ?", (name_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record



	@classmethod
	def get_record_by_warden_name(cls, wardenname_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_table WHERE warden_name = ?", (wardenname_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record


	@classmethod
	def get_record_by_id(cls, id_):

		conn = sqlite.connect(file)
		c = conn.cursor()


		c.execute("SELECT oid, * FROM hall_table WHERE oid = ?", (id_, ))
		record = c.fetchall()


		conn.commit()
		conn.close()

		return record



	@classmethod
	def update_single_room_count(cls, num, nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET single_room_count = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_double_room_count(cls, num, nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET double_room_count = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_single_room_occupancy(cls, num,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET single_room_occupancy = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()		


	@classmethod
	def update_double_room_occupancy(cls, num,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET double_room_occupancy = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_single_room_rent(cls ,num,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET single_room_rent = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()	


	@classmethod
	def update_double_room_rent(cls, num,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET double_room_rent = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_amenities_charge(cls, num,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET amenities_charge = ?
					WHERE name = ? """, (num,nam))

		conn.commit()
		conn.close()



	@classmethod
	def update_warden_name(cls, war_nam,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET warden_name = ?
					WHERE name = ? """, (war_nam,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_mess_manager_name(cls, mes_nam,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET mess_manager_name = ?
					WHERE name = ? """, (mes_nam,nam))

		conn.commit()
		conn.close()


	@classmethod
	def update_clerk_name(cls, cle_nam,nam):

		conn = sqlite.connect(file)
		c = conn.cursor()

		c.execute("""UPDATE hall_table SET clerk_name = ?
					WHERE name = ? """, (cle_nam,nam))

		conn.commit()
		conn.close()



# hall_db.create_table()
# hall_db.insert_record(('LBS','N', 100,300,0,0,1000,500,'ramesh','suresh','rakesh',100))

#hall_db.update_double_room_occupancy(250,'LBS')

# recordssss = hall_db.get_record_by_id(2)

# print(recordssss)



