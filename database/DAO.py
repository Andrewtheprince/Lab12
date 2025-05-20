from database.DB_connect import DBConnect


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