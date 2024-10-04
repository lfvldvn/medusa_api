from flask import Blueprint

# Criação das Blueprints
customers_bp = Blueprint('customers', __name__)
orders_bp = Blueprint('orders', __name__)
products_bp = Blueprint('products', __name__)
newsletter_bp = Blueprint('newsletter', __name__)

from .customers import *
from .orders import *
from .products import *
from .newsletter import *
