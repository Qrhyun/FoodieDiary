# src/models/Personal_Querymodel.py
from ...extensions import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Customer ID, primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # Customer name, unique and not nullable
    balance = db.Column(db.Float, nullable=False)  # Customer balance, not nullable

    @staticmethod
    def query_recent_meal(user_id):
        # Query the most recent meal for the user
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('QueryRecentMeal', [user_id])
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def query_remaining_money(user_id):
        # Query the remaining money for the user
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('GetRemainingMoney', [user_id])
        result = []
        for res in cursor.stored_results():
            result.extend(res.fetchall())
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def query_total_spent(user_id):
        # Query the total amount spent by the user
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT GetTotalSpent(%s) AS total_spent', (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def process_dine_in(Bid, Vid, Bnum):
        # Process dine-in for the user
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('DineInProcess', [Bid, Vid, Bnum])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query_top3_spenders():
        # Query the top 3 spenders in the last 30 days
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('GetTop3SpendersInLast30Days')
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        cursor.close()
        conn.close()
        return results