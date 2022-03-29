import pymysql
import json


class Connection():

    def connect(query):
        try:
            con = pymysql.connect(
                host='3.130.126.210',
                port=3309, 
                user= 'pruebas', 
                password='VGbt3Day5R', 
                database='habi_db'
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