from src.models.customers import Customer

def query_recent_meal(user_id):
    # 查询最近的一餐
    return Customer.query_recent_meal(user_id)

def query_remaining_money(user_id):
    # 查询剩余金额
    return Customer.query_remaining_money(user_id)

def query_total_spent(user_id):
    # 查询总花费
    return Customer.query_total_spent(user_id)

def process_dine_in(Bid, Vid, Bnum):
    # 处理堂食
    return Customer.process_dine_in(Bid, Vid, Bnum)

def query_top3_spenders():
    # 查询前三名消费最多的用户
    return Customer.query_top3_spenders()