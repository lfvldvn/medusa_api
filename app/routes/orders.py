from flask import request, jsonify
from . import orders_bp
from datetime import datetime
from database import connect_db

# Endpoint para adicionar um pedido
@orders_bp.route('/add_order', methods=['POST'])
def add_order():
    try:
        transaction_id = request.json['transaction_id']
        transaction_total = request.json['transaction_total']
        order_date = datetime.now().isoformat()
        customer_email = request.json['customer_email']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO orders (transaction_id, transaction_total, order_date, customer_email)
            VALUES (?, ?, ?, ?)
        ''', (transaction_id, transaction_total, order_date, customer_email))
        conn.commit()

        return jsonify({"message": "Pedido adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        conn.close()

# Endpoint para visualizar todos os pedidos
@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        orders_list = []
        for order in orders:
            orders_list.append({
                "id": order[0],
                "transaction_id": order[1],
                "transaction_total": order[2],
                "customer_email": order[3],
                "order_date": order[4],
            })

        return jsonify(orders_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()
