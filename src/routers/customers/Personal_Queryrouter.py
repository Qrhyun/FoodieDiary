from flask import Blueprint, request, jsonify
from src.services.customers.Personal_Query import (
    query_recent_meal,
    query_remaining_money,
    query_total_spent,
    process_dine_in,
    query_top3_spenders
)
from . import personal_query_app  # 导入 personal_query 蓝图

@personal_query_app.route('/recent_meal', methods=['GET'])
def recent_meal():
    user_id = request.args.get('user_id', type=int)
    results = query_recent_meal(user_id)
    return jsonify(results)

@personal_query_app.route('/remaining_money', methods=['GET'])
def remaining_money():
    user_id = request.args.get('user_id', type=int)
    result = query_remaining_money(user_id)
    return jsonify(result)

@personal_query_app.route('/total_spent', methods=['GET'])
def total_spent():
    user_id = request.args.get('user_id', type=int)
    result = query_total_spent(user_id)
    if result:
        return jsonify([result])
    else:
        return jsonify([])

@personal_query_app.route('/dine_in', methods=['GET'])
def dine_in():
    input_Bid = request.args.get('Bid', type=int)
    input_Vid = request.args.get('Vid', type=int)
    input_Bnum = request.args.get('Bnum', type=int)
    if not input_Bid or not input_Vid or not input_Bnum:
        return jsonify({'error': 'Bid, Vid, and Bnum are required'}), 400
    try:
        process_dine_in(input_Bid, input_Vid, input_Bnum)
        return jsonify({'message': 'Dine-in process completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@personal_query_app.route('/top3_spenders', methods=['GET'])
def top3_spenders():
    try:
        results = query_top3_spenders()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500