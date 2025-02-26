#!/usr/bin/python3

from flask import Flask, render_template, send_file
from io import BytesIO
import qrcode

# app = Flask(__name__)
# hostapd_conf = "/etc/hostapd/hostapd.conf"
# ssid = ""
# password = ""

def init():
    global ssid, password

    with open(hostapd_conf) as f:
        for line in f.readlines():
            try:
                line = line.strip()
                (key, value) = line.split("=")
                if key == "wpa_passphrase":
                    password = value
                elif key == "ssid":
                    ssid = value
            except ValueError:
                pass

def wifi_sec_str(ssid, password, sec="WPA2"):
    return "WIFI:T:{};S:{};P:{};;".format(sec, ssid, password)

@app.route("/")
def home():
    params = {
        "title": "Wifi settings",
        "ssid": ssid,
        "password": password
    }

    return render_template("index.html", **params)

@app.route("/qrcode_img.png")
def qrcode_img():
    img = qrcode.make(wifi_sec_str(ssid, password))
    stream = BytesIO()
    img.save(stream)
    stream.seek(0)
    return send_file(stream, mimetype='image/png')
