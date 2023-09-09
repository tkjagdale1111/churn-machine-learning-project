from flask import Flask, render_template, request, jsonify
from src.pipeline.preediction_pipeline import PredictionPipeline, CustomeClass

application= Flask(__name__)
app=application

@app.route("/",methods = ["GET", "POST"])
def prediction_data():
    if request.method == "GET":
        return render_template("home.html")
    
    else:
        data = CustomeClass(
               Age = int(request.form.get("Age")),
               Gender = int(request.form.get("Gender")),
               Location = int(request.form.get("Location")),
               Subscription_Length_Months = int(request.form.get("Subscription_Length_Months")),
               Monthly_Bill = int(float(request.form.get("Monthly_Bill"))),
               Total_Usage_GB = int(float(request.form.get("Total_Usage_GB")))

        )

    final_data = data.get_data_DataFrame()
    pipeline_prediction = PredictionPipeline()
    pred = pipeline_prediction.predict(final_data)

    result = pred

    if result == 0:
        return render_template("results.html", final_result = "customer churn is{}".format(result) )

    elif result == 1:
            return render_template("results.html", final_result = "custumer churn is:{}".format(result) )
    
if __name__ == "__main__":
     app.run(host = "0.0.0.0", debug = True,port=8080)




    
