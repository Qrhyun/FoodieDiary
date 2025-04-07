# src/models/windows/WindowQuerymodel.py
from ...extensions import db

class Window(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Window ID, primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # Window name, unique and not nullable

    @staticmethod
    def query_view_data(view_name):
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('GetViewData', [view_name])
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def query_totalwin_vegpurchases(dish_id):
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('QueryVegPurchases', [dish_id])
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def query_top5windows():
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('GetTop5Windows')
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def query_top5veg():
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('GetTop5VegByRemark')
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results