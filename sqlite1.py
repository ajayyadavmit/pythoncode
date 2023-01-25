
# import sqlite3
# conn = sqlite3.connect("test.db")

# # <<< CREATE TABLE >> 

# # query_createAddress = ''' create table address ( location varchar(22), city varchar(22))
# # '''
# # conn.execute(query_createAddress)
# # conn.execute(''' 
# # create table student(
# #     std_id INT,  std_name VARCHAR(22), std_course VARCHAR(44)
# # )
# # ''')

# # <<<  INSERT QUERY WITH VALUES  >>>

# # insert1 = '''
# # insert into address(location, city) values("23Basdgmati", "324Kathmandu")
# # '''
# # conn.execute(insert1)
# # conn.commit()
# # conn.close()

# # << SELECT QUERY >>> 
# # data = conn.execute('select * from address limit 2,3')
# data = conn.execute('select * from address limit 2,3')

# print("LOCATION", "\t", "CITY")
# for value in data: 
#     print(value[0], "    "  , value[1])
# print(data)

# insert2 = ''' insert into student(std_id, std_name, std_course)  values(18, "raj", "php")'''
# conn.execute(insert2)
# conn.commit()
# data2 = conn.execute('select * from student')
# for value2 in data2: 
#     print(value2)

# # st_id = (input("Enter the student id to DELETE"))
# # print(st_id)
# # conn.execute('Delete from student where std_id = ' +st_id)

# data4 = input("Enter the student name ")
# data5 = conn.execute('select * from student where std_name = "+data4+" ' )
# for value in data5:
#     print(value)
# # conn.commit()

# # data3 = conn.execute('select * from student')
# # for value2 in data3: 
# #     print(value2)

# conn.close()

# '''

# Datatypes in Mysql 
# NUMBER
#     INT  >> INTEGER NO FOR STORE (LENGTH 11 DIGITS )
#     BIGINT  >> LENGTH 20 DIGITS 

# STRING 
#     VARCHAR >> STORE ALPHA NUMERICE TYPES >> LENGTH 0 TO 255 
#     TEXT  >> O TO 6000 
#     LONGTEXT  >> 6000 TO UPPER ( LIKE PARAGRAPH FORMS )


# DATE  >> yyyy -mm -dd
# DATETIME >>  YYYY-MM-DD HH-MM-SS 

# TIMESTAMP >> CURRENT TIME STORE (FORMAT IS SIMILAR TO DATETIME)

# TINYINT >> DATA IN 3 CHARACTERS NUMBERS 

# TIME >> HH-MM-SS 

# YEAR >> YYYY
# '''


# print("helos ajay")

# import sys

# print(dir(sys))

# a = sys.stdout.write(" >>> New Line >>>>")

# print(a)

import sqlite3
import os 
print(dir(sqlite3))
print(os.getcwd())
print(os.listdir())

conn= sqlite3.connect("test2.db")
# query = ''' create table history ( code int autoincreament,subject_name varchar(22), marks int ) '''

# conn.execute(query)

# query2 = ''' insert into history(subject_name, marks)  values( "english", 55) '''
# value = conn.execute(query2)

# query3 = ''' select * from history where code = 5 '''

# qw = conn.execute(query3)

# conn.commit()
# for i in qw: 
#     print(i)

# conn.close()

print(os.getcwd())
print(os.listdir())
# os.chdir('../..')
print(os.getcwd())

print(os.path.isfile("NSDEVIL Template"))
print(os.path.isdir('GSE.png'))

