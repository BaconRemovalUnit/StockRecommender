from flask import Flask, render_template, request
from datetime import datetime, timedelta
import requests
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":  # user entering the page
        return render_template("index.html")

    elif request.method == "POST":  # after user form submission, handle form submission here
        invest_form = request.form.to_dict()
        input_dollar = float(invest_form['input_dollar'])
        # print("user spending ${} with strat {}".format(input_dollar, strat))
        strat = []
        if request.form.get("e"):
            strat.append("e")
        if request.form.get("g"):
            strat.append("g")
        if request.form.get("i"):
            strat.append("i")
        if request.form.get("q"):
            strat.append("q")
        if request.form.get("v"):
            strat.append("v")

        # TODO add return info about stock here
        stocksMapping = {
            "e" : ["APPL","ADBE","NSRGY"],
            "g" : ["NFLX","FB","NVDA"],
            "i" : ["VTI","IXUS","ILTB"],
            "q" : ["LOW","ROST","TJX"],
            "v" : ["WMT","BAC","CLF"],
        }

        seven_days_ago = datetime.now() - timedelta(days=7)
        stocks = []
        hist = []
        for i in strat:
            stocks += stocksMapping[i]

        api_token = "b7676g5wQjdv1EdR9nEnrHLoMrbqNTafYIvomuE9Hn3InTSsYwrDTLbzBdDf"
        hist_api_str = "https://www.worldtradingdata.com/api/v1/history?symbol={}&sort=newest&date_from={}&api_token={}"
        price_api_str = "https://www.worldtradingdata.com/api/v1/stock?symbol={}&api_token={}"

        for stock in stocks:
            request_str = hist_api_str.format(stock,seven_days_ago.date(),api_token)
            try:
                r = requests.get(request_str)
            except requests.exceptions.RequestException as e:
                print("Network error! Please the run program with proper Internet connecetion.")
            pass

            packet = r.json()
            hist.append(packet)






            #print(packet["history"])
        # things to return to the html, it can be any type
        obj = {"money":input_dollar, "strat": strat}

        # render index with obj
        print("Object",hist)
        return render_template("PortfolioChart.html", obj=hist)


app.run(debug=False)
