from flask import Flask, jsonify, request, render_template, url_for, json
# import packages
from datetime import date
from forms import Request
import pickle


app = Flask(__name__)

# Get configs
app.config.from_object('config.Config')

# creating the date object of today's date
today_date = date.today()
current_year = str(today_date.year)

# Copyright
app_copyright = (" © " + current_year + " | Fraudulent Transactions Detection Service")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    form = Request()

    if form.validate_on_submit():
        # receive payload
        TX_TIME_DAYS = form.TX_TIME_DAYS.data
        CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW = form.CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW.data
        CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW = form.CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW.data
        CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW = form.CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW.data
        TERMINAL_ID_RISK_1DAY_WINDOW = form.TERMINAL_ID_RISK_1DAY_WINDOW.data
        TERMINAL_ID_RISK_7DAY_WINDOW = form.TERMINAL_ID_RISK_7DAY_WINDOW.data
        TERMINAL_ID_RISK_30DAY_WINDOW = form.TERMINAL_ID_RISK_30DAY_WINDOW.data

        payload = {'TX_TIME_DAYS': TX_TIME_DAYS, 'CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW': CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW,
                         'CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW': CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW,
                         'CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW':  CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW, 'TERMINAL_ID_RISK_1DAY_WINDOW': TERMINAL_ID_RISK_1DAY_WINDOW,
                         'TERMINAL_ID_RISK_7DAY_WINDOW': TERMINAL_ID_RISK_7DAY_WINDOW, 'TERMINAL_ID_RISK_30DAY_WINDOW': TERMINAL_ID_RISK_30DAY_WINDOW} # Not Fraud
        sample_payload = {'TX_TIME_DAYS': 0.00, 'CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW': 158.073333,
                         'CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW': 158.073333,
                         'CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW': 158.073333, 'TERMINAL_ID_RISK_1DAY_WINDOW': 0.00,
                         'TERMINAL_ID_RISK_7DAY_WINDOW': 0.00, 'TERMINAL_ID_RISK_30DAY_WINDOW': 0.00} # Fraud

        payload = [list( payload.values())]

        filename = 'rf_model.sav'

        ## Loading Model ( Only Randon Forest Was Saved)
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(payload)
        result = round(result.item())

        # Act on Model Result
        if result == 1:
            response = "Transaction is Fraud"
        else:
            response = "Transaction is Legit"

    return render_template(
        "index.html",
        form=form,
        response=response,
        app_copyright=app_copyright
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", app_copyright=app_copyright), 404

