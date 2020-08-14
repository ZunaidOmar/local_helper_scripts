from sqlalchemy import create_engine
import urllib
import pyodbc
import pandas as pd


db_instance_name = r'ZUNA-LAPTOP'
db_name = 'DataLakesDB'
new_db_name = 'Insurance'

def Data_Copy():

    first_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_instance_name+';DATABASE='+db_name+';Trusted_Connection=yes')

    query = "SELECT * FROM Test_data"

    quoted = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_instance_name+';DATABASE='+new_db_name+';Trusted_Connection=yes')
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

    df = pd.read_sql(query,first_conn)

    df.to_sql('Test_data',schema='dbo',con=engine,index=False,if_exists='replace')

    result = engine.execute('SELECT COUNT(*) FROM Test_data')
    result.fetchall()

Data_Copy()