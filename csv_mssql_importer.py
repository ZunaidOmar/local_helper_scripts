from sqlalchemy import create_engine
import urllib
import pandas as pd 


db_instance_name = r'ZUNA-LAPTOP'
db_name = 'DataLakesDB'
folderpath = "C:\\Users\\T440P\\Downloads\\"


def Data_Import():

    csv_name = folderpath+"testdata.csv"
    table_name = "tbluserdata"

    quoted = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_instance_name+';db_name='+db_name+';Trusted_Connection=yes')
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

    df = pd.read_csv(csv_name,engine='python',index_col=False)

    df.to_sql(table_name,schema='dbo',con=engine,if_exists='replace',index=False)
    print('Done with import')


Data_Import()