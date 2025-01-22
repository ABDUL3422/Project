from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")
    
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["email"]
        pwd = request.form["password"]
    if name == "admin@sac.com" and pwd == "admin":
    	@app.route("/getStarted/")
    	def gs():
        	return render_template("getStarted.html")
    return render_template("login.html")
                
@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        c_passwd = request.form["c_password"]
        password = request.form["password"]
        # Add logic to handle signup data here
    return render_template("signup.html")
    
@app.route("/home/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
