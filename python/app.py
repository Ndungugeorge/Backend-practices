from flask import Flask, render_template
from babel import numbers, dates
from datetime import date, datetime

app = Flask(__name__)

@app.route("/")
def index():
    US_num = numbers.format_decimal(1.234, locale= 'en_US')
    se_num = numbers.format_decimal(1.234, locale= 'sv_SE')
    d = date(2024,11,5)

    us_date = dates.format_date(d, locale ='en_US')

    dt = datetime(2024,5,7,3,55,34,50)
    us_datetime = dates.format_datetime(dt,locale='en_US')
    
    results = {'US_num': US_num, 'se_num' : se_num, 'us_date':us_date, 'us_dt' : us_datetime}
    return render_template("index.html",result = results)

if __name__ == '__main__':
    app.run(debug = True)