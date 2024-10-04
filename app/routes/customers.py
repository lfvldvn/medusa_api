from flask import request, jsonify
from . import customers_bp
from database import connect_db

# Endpoint para adicionar um cliente
@customers_bp.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        name = request.json['name']
        cpf = request.json['cpf']
        email = request.json['email']
        mobile_phone = request.json['mobile_phone']
        landline_phone = request.json.get('landline_phone')
        gender = request.json.get('gender')
        birthdate = request.json.get('birthdate')
        postal_code = request.json.get('postal_code')
        address = request.json.get('address')
        number = request.json.get('number')
        complement = request.json.get('complement')
        reference = request.json.get('reference')
        neighborhood = request.json.get('neighborhood')
        city = request.json.get('city')
        state = request.json.get('state')

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customer (name, cpf, email, mobile_phone, landline_phone, gender, birthdate, postal_code, address, number, complement, reference, neighborhood, city, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, cpf, email, mobile_phone, landline_phone, gender, birthdate, postal_code, address, number, complement, reference, neighborhood, city, state))
        conn.commit()
        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        conn.close()

# Endpoint para visualizar todos os clientes
@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        customers = cursor.fetchall()

        customer_list = []
        for customer in customers:
            customer_list.append({
                "id": customer[0],
                "name": customer[1],
                "cpf": customer[2],
                "email": customer[3],
                "mobile_phone": customer[4],
                "landline_phone": customer[5],
                "gender": customer[6],
                "birthdate": customer[7],
                "postal_code": customer[8],
                "address": customer[9],
                "number": customer[10],
                "complement": customer[11],
                "reference": customer[12],
                "neighborhood": customer[13],
                "city": customer[14],
                "state": customer[15]
            })

        return jsonify(customer_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()
