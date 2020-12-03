import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_18_1")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "myvacsc423", "c07121", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()
def testQuery():
	cursor.execute("""
    SELECT *
    FROM EMPLOYEE
    """)

def QueryOne():
	cursor.execute("""
    SELECT * 
    FROM REQUIREMENT 
    WHERE numofEqpt > = 2
    """)

def QueryTwo():
	cursor.execute("""
    SELECT *
    FROM EQUIPMENT
    ORDER BY COSTOFEQPT ASC
    """)

def QueryThree():
	cursor.execute("""
    SELECT *
    FROM EQUIPMENT
    WHERE COSTOFEQPT < 100
    """)

def QueryFour():
	cursor.execute("""
    SELECT clientNo, cleanDays, startTime, endTime 
    FROM REQUIREMENT
    ORDER BY ClientNo
    """)

def QueryFive():
	cursor.execute("""
    SELECT fName, lName, telNo
    FROM EMPLOYEE
    """)

def QuerySix():
	cursor.execute("""
    CREATE TABLE NORMALBOOKING
    AS (SELECT name, ADDRESS,TELNO, cleanDays, startTime, endTime
    FROM REQUIREMENT, CLIENTS
    WHERE CLIENTS.clientNo = REQUIREMENT.clientNo
    AND numofeqpt = 0)
    """)

def QuerySeven():
	cursor.execute("""
    CREATE TABLE SPECIALBOOKING
    AS (SELECT name, ADDRESS,TELNO, cleanDays, startTime, endTime
    FROM REQUIREMENT, CLIENTS
    WHERE CLIENTS.clientNo = REQUIREMENT.clientNo
    AND numofeqpt >= 1)
    """)

print("The query choices are: ")
print("1. Display all Requirements using at least two special equipment")
print("2. Display Equipment in Order by Price. LOWEST TO HIGHEST")
print("3. Display Equipment and Equipment infro that costs less than $100  (QueryThree)")
print("4. Display the ClientNo, cleaning Days, start time and end time for each Requirement. Order by ClientNo")
print("5. List all staff first last names and telephone numbers. (QueryFive)")

print("     ")


query = int(input("Enter your query [the number]: "))

if query == 0:
	print("     ")
	testQuery()
	print("     ")
elif query == 1:
	print("     ")
	QueryOne()
	print("     ")
elif query == 2:
	print("     ")
	QueryTwo()
	print("     ")
elif query == 3:
	print("     ")
	QueryThree()
	print("     ")
elif query == 4:
	print("     ")
	QueryFour()
	print("     ")
elif query == 5:
	print("     ")
	QueryFive()
	print("     ")



# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
#print(df.columns)
# print(df['FIRST_NAME']) # example to extract a column

