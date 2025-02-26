import flask
import os
import qrcodegen
import textwrap

class ShowHotspotSettings(flask.Flask):
    def __init__(self, name, **kwargs):
        if "hostapd_conf" in kwargs:
            self.hostapd_conf = kwargs.pop("hostapd_conf")
        else:
            self.hostapd_conf = None
        super().__init__(name, **kwargs)

    def load_ssid_password(self):
        try:
            with open(self.hostapd_conf) as f:
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
        except IOError as ex:
            self.logger.error(f"Cannot read {self.hostapd_conf}: {ex}")
            return flask.abort(500, "Cannot read configureation")

        return (ssid, password)

    def get_svg(self):
        ssid, password = self.load_ssid_password()
        border = 2

        qr = qrcodegen.QrCode.encode_text(f"WIFI:T:WPA2;S:{ssid};P:{password};;", qrcodegen.QrCode.Ecc.LOW)
        parts = []
        for x in range(qr.get_size()):
            for y in range(qr.get_size()):
                if qr.get_module(x, y):
                    parts.append(f"M{x+border},{y+border}h1v1h-1z")
        return  textwrap.dedent(f"""\
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
                <rect width="100%" height="100%" fill="#FFFFFF"/>
                <path d="{" ".join(parts)}" fill="#000000"/>
            </svg>
            """)

def create_app(**kwargs):
    app = ShowHotspotSettings(__name__, **kwargs)

    app.logger.info("Loading blueprints")
    import showhotspotsettings.web.index
    app.register_blueprint(showhotspotsettings.web.index.bp)

    @app.before_request
    def bfr():
        app.before_request_funcs[None].remove(bfr)
        app.logger.info("First request")

    return app
