import pymysql
import json
from decouple import config


class Connection():

    def connect(query):
        try:
            con = pymysql.connect(
                host=config('DB_HOST'),
                port=int(config('DB_PORT')), 
                user=config('DB_USER'), 
                password=config('DB_PASS'), 
                database=config('DB_DATABASE')
            )
            
            response = con.cursor()
            response.execute(query)
            row_headers=[x[0] for x in response.description]
            rv = response.fetchall()
            json_data=[]
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))

            return json_data
            
        except Exception as e:
            print('error', e)
        finally:
            con.close()