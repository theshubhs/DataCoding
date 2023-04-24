from db_config import read_postgre_config
import psycopg2


def postgre_connect():
    
    postgredbconfig = read_postgre_config()
    conn= None
    cur= None

    try:
        conn = psycopg2.connect(**postgredbconfig)

        cur = conn.cursor()
        
        return conn, cur
  

    except Exception as error:
        print(error)


# postgre_connect()
