# 引入所有的service
# 引入登录和注册的service
from .authservice import register_user, login_user, update_user_password, delete_user
# 引入customers的service
from .customers.Personal_Query import query_recent_meal, query_remaining_money, query_total_spent, process_dine_in, query_top3_spenders
# 引入windows的service
from .windows.Window import query_view_data, query_totalwin_vegpurchases, query_top5windows, query_top5veg