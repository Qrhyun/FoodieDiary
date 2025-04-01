from db_config import get_db_connection

def query_recent_meal(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('QueryRecentMeal', [user_id])
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results

def query_remaining_money(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetRemainingMoney', [user_id])
    result = []
    for res in cursor.stored_results():
        result.extend(res.fetchall())
    cursor.close()
    conn.close()
    return result

def query_total_spent(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT GetTotalSpent(%s) AS total_spent', (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def process_dine_in(input_Bid, input_Vid, input_Bnum):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.callproc('DineInProcess', [input_Bid, input_Vid, input_Bnum])
    conn.commit()
    cursor.close()
    conn.close()

def query_top3_spenders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetTop3SpendersInLast30Days')
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results