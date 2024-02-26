
# Import the necessary modules
from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename
import sqlite3

# Create a Flask application instance
app = Flask(__name__)

# Set up the database
conn = sqlite3.connect('products.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, image TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, FOREIGN KEY (product_id) REFERENCES products(id))''')
c.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_name TEXT, customer_email TEXT, customer_address TEXT, total_price REAL, order_date TIMESTAMP)''')
conn.commit()

# Define the home page route
@app.route('/')
def home():
    # Get all products from the database
    products = c.execute('SELECT * FROM products').fetchall()

    # Render the home page with the list of products
    return render_template('home.html', products=products)

# Define the add to cart route
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get the product ID and quantity from the request
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')

    # Add the product to the cart
    c.execute('INSERT INTO cart (product_id, quantity) VALUES (?, ?)', (product_id, quantity))
    conn.commit()

    # Redirect to the cart page
    return redirect(url_for('cart'))

# Define the cart page route
@app.route('/cart')
def cart():
    # Get all items in the cart
    cart_items = c.execute('SELECT * FROM cart').fetchall()

    # Calculate the total price of the items in the cart
    total_price = sum(item[2] * item[3] for item in cart_items)

    # Render the cart page with the list of items and the total price
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Define the update cart quantity route
@app.route('/update_cart_quantity', methods=['POST'])
def update_cart_quantity():
    # Get the product ID and quantity from the request
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')

    # Update the quantity of the product in the cart
    c.execute('UPDATE cart SET quantity = ? WHERE product_id = ?', (quantity, product_id))
    conn.commit()

    # Redirect to the cart page
    return redirect(url_for('cart'))

# Define the remove from cart route
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    # Get the product ID from the request
    product_id = request.form.get('product_id')

    # Remove the product from the cart
    c.execute('DELETE FROM cart WHERE product_id = ?', (product_id,))
    conn.commit()

    # Redirect to the cart page
    return redirect(url_for('cart'))

# Define the checkout page route
@app.route('/checkout')
def checkout():
    # Get all items in the cart
    cart_items = c.execute('SELECT * FROM cart').fetchall()

    # Calculate the total price of the items in the cart
    total_price = sum(item[2] * item[3] for item in cart_items)

    # Render the checkout page with the list of items and the total price
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

# Define the place order route
@app.route('/place_order', methods=['POST'])
def place_order():
    # Get the customer details and order details from the request
    customer_name = request.form.get('customer_name')
    customer_email = request.form.get('customer_email')
    customer_address = request.form.get('customer_address')
    total_price = request.form.get('total_price')

    # Insert the order into the database
    c.execute('INSERT INTO orders (customer_name, customer_email, customer_address, total_price, order_date) VALUES (?, ?, ?, ?, datetime("now"))', (customer_name, customer_email, customer_address, total_price))
    conn.commit()

    # Get the order ID
    order_id = c.lastrowid

    # Empty the cart
    c.execute('DELETE FROM cart')
    conn.commit()

    # Redirect to the confirmation page
    return redirect(url_for('confirmation', order_id=order_id))

# Define the confirmation page route
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
