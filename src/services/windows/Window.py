from src.models.windows import Window

def query_view_data(view_name):
    # Query view data
    return Window.query_view_data(view_name)

def query_totalwin_vegpurchases(dish_id):
    # Query total vegetable purchases for a dish
    return Window.query_totalwin_vegpurchases(dish_id)

def query_top5windows():
    # Query top 5 windows
    return Window.query_top5windows()

def query_top5veg():
    # Query top 5 vegetables by remark
    return Window.query_top5veg()