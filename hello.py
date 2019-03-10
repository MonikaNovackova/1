from flask import Flask, render_template, request, url_for

app=Flask("MyApp")

@app.route("/")
def helloW():
    return "Hello world"

@app.route("/signup2", methods=["POST"])
def returnhome():
    form_data=request.form
    v_email=form_data["email"]

    return render_template("tonka.html",v_email=v_email)



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print form_data["email"]
    return "All ok. Your email is:"+ form_data["email"]

@app.route("/signup3", methods=["POST"])
def returnhome2():
    form_data=request.form
    v_email=form_data["email"]
    return v_email


print("test")

@app.route('/index')
@app.route('/')
def index():
    return 'you are in the index page'

app.run(debug=True)