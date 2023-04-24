import pytest
import db_connect


@pytest.mark.sanity
def test_3populaterecords():

    #database connection established
    try:
        #database connection established
        conn, cur = db_connect.postgre_connect()
        #accesing the cursor and executing the database query
        cur.execute("""select concat(c.firstname,'_',c.lastname) as customer_fullname ,p.prod_id, p.title, p.price 
                            from public.customers c, public.products p 
                            where c.customerid = p.prod_id
                            group by concat(c.firstname,'_',c.lastname), p.prod_id, p.title, p.price limit 5;""")
        
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
        
test_3populaterecords()