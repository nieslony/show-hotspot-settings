#!/usr/bin/python3

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from showhotspotsettings.web import create_app

DEF_HOSTAPD_CONF = "/etc/hostapd/hostapd.conf"

def main():
    parser = argparse.ArgumentParser(description="Show hotspot credentials on website")
    parser.add_argument("--environment", "-e",
                        help="Flask environment",
                        default="production",
                        choices=["production", "development"]
                        )
    parser.add_argument("--config", "-c",
                        help="Position of hostapd.conf",
                        default=DEF_HOSTAPD_CONF
                        )
    parser.add_argument("--listen", "-l",
                        help="Listen on given IP address",
                        default="localhost"
                        )
    parser.add_argument("--port", "-p",
                        help="TCP to listen on",
                        default=5000,
                        type=int,
                        )
    args = parser.parse_args()

    os.environ["FLASK_ENV"] = args.environment
    app = create_app(hostapd_conf=args.config)
    app.logger.setLevel("INFO")
    app.logger.info("Created app from main function")
    app.run(host=args.listen, port=args.port)

if __name__ == "__main__":
    # run from command line
    main()
else:
    # run from wsgi
    my_dir = f"{os.path.dirname(__file__)}"

    args = {
        "static_folder": f"{my_dir}/static",
        "template_folder": f"{my_dir}/templates",
        "hostapd_conf": DEF_HOSTAPD_CONF
        }

    application = create_app(**args)
