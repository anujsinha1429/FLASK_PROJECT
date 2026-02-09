from flask import Flask, render_template,request,redirect,url_for,flash

app=Flask(__name__)
app.secret_key = "your_secret_key_here"

# @app.route("/")
# def home():
#     return render_template("feedback.html")

# @app.route("/feedback",methods=["POST","GET"])
# def feedback():
#     if request.method=="POST":
#         name=request.form.get("name")
#         message=request.form.get("message")
#         # return f"Thank you {name} for your feedback: {message}"

#         return render_template("thankyou.html",name=name,message=message)
    
#     return render_template("feedback.html")

# if __name__=="__main__":
#     app.run(debug=True)

@app.route("/",methods=["GET","POST"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        message=request.form.get("message")
        if not name:
            flash("name is required!")
            return redirect(url_for("feedback"))
        flash(f"Hello, {name}! your form has been submitted successfully.")
        # return redirect(url_for("thankyou"))
        return render_template("thankyou.html", msg=message)
    return render_template("feedback.html")


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")