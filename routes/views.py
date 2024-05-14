from flask import Blueprint,render_template,Response
from utils.classifier import Predictor
from utils.cookie import Cookie
import json

views = Blueprint('/',__name__)
predictor = Predictor()
cookie = Cookie()

@views.route("/")
def home():
    return render_template('home.html')

@views.route("scan/")
def scan():
    return render_template('scan.html', predictor=predictor, cookie=cookie)

@views.route('video/')
def video():
    return Response(predictor.main(), mimetype='multipart/x-mixed-replace; boundary=frame')

@views.route('data/')
def data():
    print(cookie.name)
    cookie.setLabel(predictor.label)
    return json.dumps({
        "predictor":{
            "percent": "{:.0%}".format(float(predictor.percent)),
            "time_pred": "{:.2} ms".format(float(predictor.time_predict)),
            "time_pros": "{:.2} ms".format(float(predictor.time_pross))
        },
        "cookie":{
            "name": cookie.name,
            "description":cookie.description,
            "sugar":cookie.sugar,
            "fat":cookie.fat,
            "for":cookie.forP
        }
    })
    # return Response(predictor.getLabel(), mimetype='text/plain')
