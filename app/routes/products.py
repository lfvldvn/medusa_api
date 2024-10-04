from flask import request, jsonify
from . import products_bp
from database import connect_db

# Endpoint para adicionar um produto
@products_bp.route('/add_product', methods=['POST'])
def add_product():
    try:
        product_id = request.json['product_id']
        product_name = request.json['product_name']
        price = request.json['price']
        brand = request.json.get('brand')
        category = request.json.get('category')
        subcategory = request.json.get('subcategory')

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (product_id, product_name, price, brand, category, subcategory)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (product_id, product_name, price, brand, category, subcategory))
        conn.commit()

        return jsonify({"message": "Produto adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        conn.close()

# Endpoint para visualizar todos os produtos
@products_bp.route('/products', methods=['GET'])
def get_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        product_list = []
        for product in products:
            product_list.append({
                "id": product[0],
                "product_id": product[1],
                "product_name": product[2],
                "price": product[3],
                "brand": product[4],
                "category": product[5],
                "subcategory": product[6],
            })

        return jsonify(product_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()

