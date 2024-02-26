## Python Flask Expert Assistant

### Problem Statement (Provided by Human):

As a small business owner, I want to create a simple web application where customers can view my product catalog, add items to their shopping cart, and place an order. The application should allow me to manage my product inventory and orders. How can I achieve this using Python Flask?

### Flask Application Design:

### HTML Files:

1. **home.html**:
   - This HTML file serves as the landing page of your website, showcasing your product catalog.
   - It should include a list of products with their names, images, prices, and a button to add them to the cart.

2. **cart.html**:
   - This HTML file displays the items added to the shopping cart.
   - It should allow users to update the quantity of each item, remove items, and proceed to checkout.

3. **checkout.html**:
   - This HTML file is used for the checkout process.
   - It should collect the customer's details and display the order summary for confirmation.

### Routes:

1. **@app.route('/')**:
   - This route handles the landing page of your website.
   - It should render the `home.html` file.

2. **@app.route('/add_to_cart')**:
   - This route handles adding an item to the customer's shopping cart.
   - It should retrieve the product details, update the cart session, and redirect to the cart page.

3. **@app.route('/cart')**:
   - This route displays the items in the customer's shopping cart.
   - It should render the `cart.html` file.

4. **@app.route('/update_cart_quantity')**:
   - This route handles updating the quantity of an item in the cart.
   - It should update the cart session and redirect to the cart page.

5. **@app.route('/remove_from_cart')**:
   - This route handles removing an item from the cart.
   - It should update the cart session and redirect to the cart page.

6. **@app.route('/checkout')**:
   - This route initiates the checkout process.
   - It should render the `checkout.html` file.

7. **@app.route('/place_order')**:
   - This route handles placing the order.
   - It should collect the customer's details, store the order in a database, and redirect to a confirmation page.