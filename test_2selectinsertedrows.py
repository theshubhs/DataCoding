import db_connect
import pytest

@pytest.mark.sanity
def test_2selectinsertedrows():
    try:
        
        #database connection established
        conn, cur = db_connect.postgre_connect()
        #accesing the cursor and executing the database query
        cur.execute("SELECT * FROM customers order by customerid desc limit 5;")
        #formatting the data fetched from database in table structure 
        colnames = [desc[0] for desc in cur.description]
        rowdict = []
        for row in cur.fetchall():
            newdict = {}
            for name, val in zip(colnames, row):
                newdict[name] = val
            rowdict.append(newdict)

        for row in rowdict:
            print(row)
    
    except Exception as error:
        print(error)
        
    
    #closing all the opne connections established   
    finally:
        cur.close()
        # print('cursor closed')
        conn.close()
        # print('connection closed')
    

# test_2selectinsertedrows()
