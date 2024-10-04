from flask import Flask
from routes.customers import customers_bp
from routes.orders import orders_bp
from routes.products import products_bp
from routes.newsletter import newsletter_bp
from database import create_db

app = Flask(__name__)

# Criar o banco de dados e as tabelas
create_db()

# Registrando as Blueprints
app.register_blueprint(customers_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(products_bp)
app.register_blueprint(newsletter_bp)

if __name__ == '__main__':
    app.run(debug=True)
