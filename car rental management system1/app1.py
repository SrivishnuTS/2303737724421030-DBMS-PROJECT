from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'sri'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9865'  # Your MySQL password here
app.config['MYSQL_DB'] = 'db3'  # Your database name here
mysql = MySQL(app)



# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display available cars
@app.route('/cars')
def cars():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cars")  # Query to fetch car data
    car_info = cur.fetchall()
    cur.close()
    return render_template('homepage.html', cars=car_info)  # Render cars info

# Route to search cars by ID
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['car_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM cars WHERE id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('homepage.html', cars=search_results)

# Route to insert a new car
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        car_id = request.form['car_id']
        model = request.form['model']
        brand = request.form['brand']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cars (id, model, brand, price) VALUES (%s, %s, %s, %s)", (car_id, model, brand, price))
        mysql.connection.commit()
        return redirect(url_for('cars'))

# Route to delete a car
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cars WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cars'))

# Route to edit car details (Display the Edit Form)
@app.route('/edit/<string:id_data>', methods=['GET'])
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cars WHERE id=%s", (id_data,))
    car = cur.fetchone()  # Fetch the car details to edit
    cur.close()
    return render_template('edit_car.html', car=car)

# Route to handle the update of car details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        car_id = request.form['car_id']
        model = request.form['model']
        brand = request.form['brand']
        price = request.form['price']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE cars SET model=%s, brand=%s, price=%s WHERE id=%s", (model, brand, price, car_id))
        mysql.connection.commit()
        return redirect(url_for('cars'))  # Redirect back to the car list page

if __name__ == "__main__":
    app.run(debug=True)
