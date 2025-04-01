from db_config import get_db_connection

def query_view_data(view_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetViewData', [view_name])
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results

def query_totalwin_vegpurchases(dish_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('QueryVegPurchases', [dish_id])
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results

def query_top5windows():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetTop5Windows')
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results

def query_top5veg():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetTop5VegByRemark')
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return results