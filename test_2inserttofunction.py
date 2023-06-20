import pytest
import db_connect

@pytest.mark.sanity
def test_1inserttofunction():
    try:
        #database connection established
        conn, cur = db_connect.postgre_connect()

        #calling procedure for inserting records
        insert1 = cur.callproc('new_customer', ('TOMG','AUSTIN7','sector1','AB','seattle','RO',10008,'US1',1,'test6@test.com','10101010101',206,'00000000000012','2023/10','user100008','aaaaaaaa8',27,25000,'M'))
        insert2 = cur.callproc('new_customer', ('TOMH','AUSTIN8','sector1','AB','seattle','RO',10009,'US1',1,'test7@test.com','10101010102',207,'00000000000013','2023/10','user100009','aaaaaaaa9',27,25000,'M'))
        insert3 = cur.callproc('new_customer', ('TOMI','AUSTIN9','sector1','AB','seattle','RO',10010,'US1',1,'test8@test.com','10101010103',208,'00000000000014','2023/10','user100010','aaaaaaa10',27,25000,'M'))
        insert4 = cur.callproc('new_customer', ('TOMJ','AUSTIN10','sector1','AB','seattle','RO',10011,'US1',1,'test9@test.com','10101010104',209,'00000000000015','2023/10','user100011','aaaaaaa11',27,25000,'M'))
        insert5 = cur.callproc('new_customer', ('TOMK','AUSTIN11','sector1','AB','seattle','RO',10012,'US1',1,'test10@test.com','10101010105',210,'00000000000016','2023/10','user100012','aaaaaaa12',27,25000,'M'))
        
        
        insertall = [insert1,insert2,insert3,insert4,insert5]
        
        for x in insertall:
            x = cur.fetchall()
        
        print("RECORDS INSERTED USING new_customer FUNCTION")
        
        conn.commit()

        
    except Exception as error:
        print(error)
    
    #closing all the opne connections established
    finally:
        cur.close()
        # print('cursor closed')
        conn.close()
        # print('connection closed')
        
# test_1inserttofunction()
