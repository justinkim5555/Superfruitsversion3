from flask import Flask, render_template, request, redirect, session, jsonify
import re, random
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key="123"
mysql = connectToMySQL('mydb')

@app.route('/')
def index():
    return render_template("superfruits.html")

@app.route('/productpage')
def product():
    return render_template("productpage.html")

@app.route('/productpage1')
def product1():
    return render_template("productpage1.html")

@app.route('/productpage2')
def product2():
    return render_template("productpage2.html")

@app.route('/adminloginpage')
def adminloginpage():
    return render_template("Adminloginpage.html")

@app.route('/dashboard1')
def dashboard1():
    return render_template("dashboard1.html")

@app.route('/dashboard2_products')
def dashboard2_products():
    return render_template("dashboard2_products.html")

@app.route('/dashboard3_orderID')
def dashboard3_orderID():
    return render_template("dashboard3_orderID.html")




@app.route('/funny_pictures', methods=['POST'])
def funny():
    images = [
                "https://i.ytimg.com/vi/pID_QuyUi98/maxresdefault.jpg",
                "https://3.bp.blogspot.com/-PWh76bHPAYk/WcK7AYAwCEI/AAAAAAABz5E/kGThGaywUTc80vRLwEULRBAmXgWJe_XpgCLcBGAs/s1600/funny-cat-277-01.jpg",
                "http://thumbpress.com/wp-content/uploads/2013/04/Funny-Cat-Pictures-with-Captions-25.jpg",
                "http://fallinpets.com/wp-content/uploads/2016/09/surrender.jpg",
                "https://i.imgflip.com/1y0qsj.jpg",
                "https://boygeniusreport.files.wordpress.com/2015/06/funny-cat.jpg?quality=98&strip=all&w=782"
                "http://thumbpress.com/wp-content/uploads/2013/04/Funny-Cat-Pictures-with-Captions-28.jpg"
            ];
    random.shuffle(images)
    count = request.form['count']
    print('count is', count)

    return render_template("pictures.html", images=images, count=int(count))





























# @app.route('/')
# def index():
#     return render_template("main.html")

####
# @app.route('/ajax_example')
# def ajax_example():

#     query = "SELECT first_name FROM usersFinal WHERE first_name LIKE %(starts_with)s"
#     data = { 'starts_with': request.form['starts_with'] + "%" }

#     users = mysql.query_db(query, data)
#     return jsonify(users=users)

# @app.route('/funny_pictures_api/api')
# def funnyapi():
#     return render_template("json.html")








# #### API JSON for USERS DATA
# @app.route('/users/api_json', methods=['POST'])
# def users_api_json():
#     query = "SELECT first_name FROM usersFinal WHERE first_name LIKE %(starts_with)s"
#     data = { 'starts_with': request.form['starts_with'] + "%" }
#     users = mysql.query_db(query, data)
#     return jsonify(users=users)

# #### API JSON for USERS DATA
# @app.route('/users/api', methods=['POST'])
# def users_api():
#     query = "SELECT first_name FROM usersFinal WHERE first_name LIKE %(starts_with)s"
#     data = { 'starts_with': request.form['starts_with'] + "%" }
#     users = mysql.query_db(query, data)
#     print (users)
#     return render_template("submit.html", users=users)



if __name__=="__main__":
    app.run(debug=True)
