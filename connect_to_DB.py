#!/usr/bin/python

import MySQLdb

cnx = MySQLdb.connect (host="localhost", user="root", passwd="*****", db="first_DB")

cur = cnx.cursor()

cnt = 2
repeat = 'y'
table_array  = []
def get_table():
	index = 1	
	get_db = "USE first_DB"
	cur.execute(get_db)
	cur.execute("SHOW TABLES")
	tables = cur.fetchall()
	print("            Avalible tables\n")
	for tab in tables:
		print('%d' ": ") %index, tab[0]
		index = index +1
		table_array.append(tab[0])
        #print(table_array)
	return(table_array)

def table_list_switch(val):
	print(val)

	if val > 3:
		print("Entry is Invalid")
	else:
		switcher = {1:"Favorites",2:"cars",3:"people"}
		return switcher.get(val)
	#print switcher.get(val)

while (repeat == 'y'):

	select_value = int(raw_input("1: Add data to the database\n2: Get data from the database\n"))
	avl_tables = get_table()
	#index = 1
	#tab_index = 0

	#table_avl = int(raw_input("Availible tables\n "))
	aval_Column = []

	if select_value == 1:
		cnt = cnt + 1
		table = int(raw_input("Enter the table you want to add data to: "))
		table_val = table_list_switch(table)
		#print(table_val)
		print("You selected the %s table"%table_val)
		
		#cur.execute("SHOW columns FROM %s"%table_val)
		cur.execute("desc %s" %table_val)
		columns = cur.fetchall()
		for column in columns:
			#print column[0]+" ",
		        aval_Column.append(column[0])
		
		column_len = len(aval_Column)
		#print aval_Column 
		#print ("First Coulnm in table is: %s" %aval_Column[1])
		
		columns = "|  ".join(column[0] for column in columns)
		print columns
		print "__________________"

		cur.execute("SELECT * FROM %s"%table_val)
		field = cur.fetchall()
#		print len(field)
		#result = cnx.query("""SELECT * FROM %s limit 1 """%table_val)
		#print ("the value of result is: %s" %result)
		if len(field)==0:
			print("the table is empty")
			add_rec = raw_input("Would you like to add a record y/n?")
			if add_rec == "y":
				for rec in range(1,column_len):
					recVal = raw_input("Enter a record for %s in table %s:  " %(aval_Column[rec],table_val))
				
		else:
			for rows in field:
				print rows[0],"|", rows[1] ,"|",rows[2]
 

		rec_num = int(raw_input("Enter the number of records/rows: "))

		if rec_num == 1:
			rec1 = raw_input("Enter your record: ")
			sql = "INSERT INTO cars VALUES(null, '%s')" %rec1
			print("here")
			print(cnt)
			print(rec1)
			cur.execute(sql)
			cnx.commit()
		elif rec_num == 2:
			rec2 = raw_input("Enter your first record: ")
			rec2_2 = raw_input("Enter your second record: ")
			sql = "INSERT INTO cars VALUES(null, '%s', '%s')" %(rec2,rec2_2)
			cur.execute(sql)
			cnx.commit()
	else:
		rd_table_data=raw_input("What table do you want: ")
		rd_colum_data=int(raw_input("What row number do you want: "))

		cur.execute("SELECT * FROM %s"%rd_table_data)
		for row in cur.fetchall():
			print row[rd_colum_data]

        repeat = raw_input("Do you want to add another record: ")


#sql = "INSERT INTO cars VALUES(1, 'Mazda', 'MAZDA 3')"

#number_of_rows = cur.execute(sql)
#cnx.commit()

#cur.execute("SELECT * FROM cars")

#print ("You are here")


#for row in cur.fetchall():
#	print row[0]
#	print row[1]
#	print row[2]

#numrows = cur.rowcount
#row = cur.fetchone()
#print ("fetch works")
#print row[1]
#
#for x in range(0, numrows):
#	row = cur.fetchone()
#	print row[0]
#        print ("Made it this far")

cnx.close()
