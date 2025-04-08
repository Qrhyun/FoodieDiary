from flask import Blueprint, request, jsonify
from src.services.windows.Window import (
    query_view_data,
    query_totalwin_vegpurchases,
    query_top5windows,
    query_top5veg
)
from . import window_app  # 导入 window 蓝图

@window_app.route('/query_view_data', methods=['GET'])
def view_data():
    view_name = request.args.get('view_name')
    if not view_name:
        return jsonify({'error': 'view_name is required'}), 400
    try:
        results = query_view_data(view_name)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/query_totalwin_vegpurchases', methods=['GET'])
def totalwin_vegpurchases():
    dish_id = request.args.get('dish_id', type=int)
    if not dish_id:
        return jsonify({'error': 'dish_id is required'}), 400
    try:
        results = query_totalwin_vegpurchases(dish_id)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/query_top5windows', methods=['GET'])
def top5windows():
    try:
        results = query_top5windows()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@window_app.route('/query_top5veg', methods=['GET'])
def top5veg():
    try:
        results = query_top5veg()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500