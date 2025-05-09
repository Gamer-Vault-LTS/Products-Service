from flask import Flask, g, jsonify
from routes import Product, ShoppingCart
from flask_cors import CORS
from utils.db import get_db



app = Flask(__name__)
CORS(app)
app.register_blueprint(Product.product_route)   
app.register_blueprint(ShoppingCart.shoppingcart_route)    


@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.before_request
def before_request():
    g.db = next(get_db())

@app.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    