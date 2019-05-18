from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":  # user entering the page
        return render_template("index.html")

    elif request.method == "POST":  # after user form submission, handle form submission here
        invest_form = request.form.to_dict()
        input_dollar = float(invest_form['input_dollar'])
        # print("user spending ${} with strat {}".format(input_dollar, strat))
        stocksMapping = {
        "e" : ["APPL","ADBE","NSRGY"],
        "g" : ["NFLX","FB","NVDA"], 
        "i" : ["VTI","IXUS","ILTB"],
        "q" : ["LOW","ROST","TJX"],
        "v" : ["WMT","BAC","CLF"]
        }
        strat = []
        if request.form.get("e"):
            strat.append(stocksMapping["e"])
        if request.form.get("g"):
            strat.append(stocksMapping["g"])
        if request.form.get("i"):
            strat.append(stocksMapping["i"])
        if request.form.get("q"):
            strat.append(stocksMapping["q"])
        if request.form.get("v"):
            strat.append(stocksMapping["v"])

        # TODO add return info about stock here


        # things to return to the html, it can be any type
        for i in strat:
            obj = {
            "money":input_dollar, 
            "strat": strat
            }

        # render index with obj
        return render_template("index.html", obj=obj)


app.run(debug=True, port=80)
