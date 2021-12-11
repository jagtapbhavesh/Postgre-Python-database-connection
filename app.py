import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '14242805'
port_id = 5432
conn = None
cur = None

# try-except block to detect the error easily 
# connect with demo database in pgadmin4
try:
   conn = psycopg2.connect(
      host = hostname,
      dbname = database,
      user = username,
      password = pwd,
      port = port_id)

   # cursor_factor is used to show the output in dictionary name and salary
   cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

   # To create a new table everytime insert statement is changed
   cur.execute('DROP TABLE IF EXISTS employee') 

   #create table employee.
   create_script = '''  CREATE TABLE IF NOT EXISTS employee (
                           id       int PRIMARY KEY,
                           name     varchar(40) NOT NULL,
                           salary   int,
                           dept_id varchar(30)) '''
   # execute the changes to pgadmin4
   cur.execute(create_script)

   # insert script and values 
   insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
   insert_values = [(1, 'James', 12000, 'D1'),(2, 'Raj', 20000, 'D1'),(3, 'Robin', 22000, 'D1')]
   
   # execute the values added to pgadmin4
   for record in insert_values:
      cur.execute(insert_script, record)

   # used update statement to update salaries of employees
   update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
   cur.execute(update_script)

   # delete the data from employee
   delete_script = 'DELETE FROM employee WHERE name = %s'
   delete_record = ('James',)
   cur.execute(delete_script,delete_record)
   
   # select statement to show data in python program.
   cur.execute('SELECT * FROM EMPLOYEE')
   #fetch data from postgre and display in python program
   for record in cur.fetchall():
      # print(record[1], record[2])
      print(record['name'],record['salary'])
 

   # commit is used to commit to pgadmin4
   conn.commit()
except Exception as error:
   print(error)
   # finally is used to close the database.
finally:
 if cur is  None:
    cur.close()
 if conn is  None:
    conn.close()
   