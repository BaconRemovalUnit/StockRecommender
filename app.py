from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":  # user entering the page
        return render_template("index.html")

    elif request.method == "POST":  # after user form submission, handle form submission here
        invest_form = request.form.to_dict()
        input_dollar = float(invest_form['input_dollar'])
        strat = invest_form['strat']
        print("user spending ${} with strat {}".format(input_dollar, strat))

        # TODO add return info about stock here
        stocksMapping = {
        "e" : ["APPL","ADBE","NSRGY"],
        "g" : ["NFLX","FB","NVDA"], 
        "i" : ["VTI","IXUS","ILTB"],
        "q" : ["LOW","ROST","TJX"],
        "v" : ["WMT","BAC","CLF"],
        };

        # things to return to the html, it can be any type
        obj = {"money":input_dollar, "strat": strat}

        # render index with obj
        return render_template("index.html", obj=obj)


app.run(debug=True, port=80)
