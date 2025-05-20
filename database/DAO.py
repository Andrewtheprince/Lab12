from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO:

    @staticmethod
    def getAllNazioni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT r.Country
                    FROM go_retailers r
                    group by r.Country
                    order by r.Country asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers(nazione):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT *
                    FROM go_retailers r
                    where r.Country = %s """
        cursor.execute(query, (nazione,))
        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select gds1.retailer_code as retailer1, gds2.retailer_code as retailer2, count(*) as tot
                    from (  select gds.Retailer_code, gds.Product_number
                            from go_daily_sales gds 
                            where YEAR(gds.Date) = %s
                            group by gds.Retailer_code, gds.Product_number ) gds1, 
                            (select gds.Retailer_code, gds.Product_number
                            from go_daily_sales gds 
							where YEAR(gds.Date) = %s
							group by gds.Retailer_code, gds.Product_number) gds2
                    where gds1.product_number = gds2.product_number and gds1.retailer_code != gds2.retailer_code
                    group by gds1.retailer_code, gds2.retailer_code"""
        cursor.execute(query, (anno,anno,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result