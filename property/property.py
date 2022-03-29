from database.connection import Connection
from .utils import STATUS
from .filters import Filters


class Property():

    def get_properties(year:int, city:str, status:str):
        params = ""

        if year is not None:
            year = f""" AND p.year = {year}"""
            params += year
        
        if city is not None:
            city = city.lower()
            city = f""" AND p.city like '%{city}%'"""
            params += city

        if status is not None:
            status = status.lower()
            status = f""" AND s.name like '%{status}%'"""
            params += status
        
        sql = f"""SELECT 
            p.id, 
            p.address, 
            p.city, 
            s.name, 
            p.price,
            p.description
            FROM property p
            left join status_history sh on sh.property_id = p.id
            left join status s on s.id = sh.status_id
            where s.id in ({STATUS['pre_venta']},{STATUS['en_venta']},{STATUS['vendido']})
            AND sh.update_date = (
                SELECT MAX(shmax.update_date) 
                FROM status_history shmax 
                WHERE shmax.property_id = sh.property_id
            )
            {params}
            GROUP BY sh.property_id"""

        return Connection.connect(sql)