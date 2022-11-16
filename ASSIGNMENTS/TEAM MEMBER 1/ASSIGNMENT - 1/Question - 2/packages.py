from flask import Flask,render_template,request,redirect,url_for,abort
app=Flask( __name__ )
@app.route("/") 
def home():
 return render_template("register.html")
@app.route("/register",methods=["POST","GET"])
def register():
 if request.method=="POST": 
  username=request.form.get('username') 
 email=request.form.get('email') 
 phone=request.form.get('phone')
 if username=="admin":
   return redirect(url_for("admin_page"))
   return render_template("home.html",username=username,email=email,phone=phone)
@app.route("/admin") 
def admin_page():
 return render_template("admin.html")
@app.route("/validate",methods=["POST","GET"]) 
def validate_admin():
 if request.method=="POST": 
  password=request.form.get('password') 
 if(password=="abcd"):
  return render_template("admindashboard.html") 
 else:
  abort(403)
if __name__ == ' __main__ ': 
 app.run(debug=True)