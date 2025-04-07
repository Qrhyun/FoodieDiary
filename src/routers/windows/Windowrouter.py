from flask import Blueprint, request, jsonify
from src.models.windows.Windowmodel import Window
from . import window_app  # 导入 window 蓝图

@window_app.route('/view_data', methods=['GET'])
def view_data():
    view_name = request.args.get('view_name')
    if not view_name:
        return jsonify({'error': 'view_name is required'}), 400
    try:
        results = Window.query_view_data(view_name)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/totalwin_vegpurchases', methods=['GET'])
def totalwin_vegpurchases():
    dish_id = request.args.get('dish_id', type=int)
    if not dish_id:
        return jsonify({'error': 'dish_id is required'}), 400
    try:
        results = Window.query_totalwin_vegpurchases(dish_id)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/gettop5windows', methods=['GET'])
def gettop5windows():
    try:
        results = Window.query_top5windows()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/gettop5veg', methods=['GET'])
def gettop5veg():
    try:
        results = Window.query_top5veg()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500