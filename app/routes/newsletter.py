from flask import request, jsonify
from . import newsletter_bp
from database import connect_db

# Endpoint para adicionar uma inscrição na newsletter
@newsletter_bp.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json.get('phone')
        source_id = request.json['source_id']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO newsletter (name, email, phone, source_id)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, source_id))
        conn.commit()

        return jsonify({"message": "Inscrição na newsletter realizada com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        conn.close()

# Endpoint para visualizar todas as inscrições na newsletter
@newsletter_bp.route('/subscribers', methods=['GET'])
def get_subscribers():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM newsletter")
        subscribers = cursor.fetchall()

        subscriber_list = []
        for subscriber in subscribers:
            subscriber_list.append({
                "id": subscriber[0],
                "name": subscriber[1],
                "email": subscriber[2],
                "phone": subscriber[3],
                "source_id": subscriber[4],
            })

        return jsonify(subscriber_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()
