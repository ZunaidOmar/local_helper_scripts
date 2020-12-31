from sqlalchemy import create_engine
import urllib
import pandas as pd 






def Data_Import():

   

    quoted = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=ZUNA-LAPTOP;DATABASE=DataLakesDB;Trusted_Connection=yes')
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

    df = pd.read_csv(r"C:\Users\T440P\Downloads\People.csv",engine='python',index_col=False)

    df.to_sql('zuna',schema='dbo',con=engine,if_exists='replace',index=False)
    print('Done with import')


Data_Import()