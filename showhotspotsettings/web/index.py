#!/usr/bin/python3

import flask
bp = flask.Blueprint("index", __name__)

def wifi_sec_str(ssid, password, sec="WPA2"):
    return "WIFI:T:{};S:{};P:{};;".format(sec, ssid, password)

@bp.route("/")
def home():
    app = flask.current_app
    ssid, password = app.load_ssid_password()
    params = {
        "title": "Wifi settings",
        "ssid": ssid,
        "password": password
    }

    return flask.render_template("index.html", **params)

@bp.route("/qrcode.svg")
def qrcode():
    app = flask.current_app
    return flask.Response(app.get_svg(),  mimetype='image/svg+xml')
    # img = qrcode.make(wifi_sec_str(ssid, password))
    # stream = BytesIO()
    # img.save(stream)
    # stream.seek(0)
    # return send_file(stream, mimetype='image/png')
