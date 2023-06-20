import pytest
import db_connect
import pandas as pd


@pytest.mark.sanity
def test_6tablecomparecsv():
    #database connection established
    try:
        conn, cur = db_connect.postgre_connect()
        #accesing the cursor and executing the database query
        cur.execute("""select * from customers limit 5;""")
        
        db_data = cur.fetchall()
        #curating all the given column names in varaible
        column_names = ['customerid','firstname','lastname','address1','address2','city','state','zip','country','region','email','phone','creditcardtype','creditcard','creditcardexpiration','username','password','age','income','gender']
        #created a dataframe with column values from database 
        db_dataframe = pd.DataFrame(db_data, columns = column_names)
        #reading the provided csv data
        csv_data = pd.read_csv("./DataInput/Cust_test.csv")
        #created a dataframe with csv data 
        csv_dataframe = pd.DataFrame(csv_data)
        #created assertion for database dataframe and csv dataframe
        assert db_dataframe.sort_index(inplace=True) == csv_dataframe.sort_index(inplace=True),"Difference in Customer table data and Cust csv data"
        
        print("Customer table data is equals to Cust csv file data")
        
        
    except Exception as error:
        print(error)
    #closing all the opne connections established
    finally:
        cur.close()
        # print('cursor closed')
        conn.close()
        # print('connection closed')
        
# test_6tablecomparecsv()
