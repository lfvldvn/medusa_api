# app/schemas.py

customer_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "cpf": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "mobile_phone": {"type": "string"},
        "landline_phone": {"type": "string"},
        "gender": {"type": "string"},
        "birthdate": {"type": "string", "format": "date"},
        "postal_code": {"type": "string"},
        "address": {"type": "string"},
        "number": {"type": "string"},
        "complement": {"type": "string"},
        "reference": {"type": "string"},
        "neighborhood": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
    },
    "required": ["name", "cpf", "email", "mobile_phone"]
}

order_schema = {
    "type": "object",
    "properties": {
        "transaction_id": {"type": "string"},
        "transaction_total": {"type": "number"},
        "customer_email": {"type": "string", "format": "email"},
    },
    "required": ["transaction_id", "transaction_total", "customer_email"]
}
