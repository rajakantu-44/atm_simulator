from flask import Flask,render_template,request

app=Flask(__name__)
balance=0
@app.route("/",methods=["GET","POST"])
def home():
    global balance
    output = ""
    if request.method=="POST":
        choice=request.form["choice"]
        if choice=="1":
            output=f"Current Balance=₹{balance}"
        elif choice=="2":
            amount=int(request.form["amount"])
            balance+=amount
            output=f"Amount Deposited Successfully! and Your current Balance:₹{balance}"
                       
        elif choice=="3":
            amount=int(request.form["amount"])
            balance-=amount
            if balance==0:
                output=f"Your Account Balance is Zero"
            else:
                output=f"₹{amount} Withdrawn Successfully and Your Current Balance:₹{balance} "          
                
    return render_template("index.html",output=output)
if __name__=="__main__":
    app.run(debug=True)    
            
        