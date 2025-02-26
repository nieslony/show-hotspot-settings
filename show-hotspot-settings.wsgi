import argparse
import sys
import os

#sys.path.insert(0, os.path.dirname(__file__))
from shothotspotsettings.web import create_app

def main():
    parser = argparse.ArgumentParser(description="Show hotspot credentials on website")
    parser.add_argument("--environment", "-e",
                        help="Flask environment",
                        default="production",
                        choices=["production", "development"]
                        )
    parser.add_argument("--config", "-c",
                        help="Position of hostapd.conf",
                        default="/etc/hostapd/hostapd.conf"
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
    if "config" in args:
        os.environ["CONFIG_PATH"] = args.config

    app = create_app()
    app.logger.info("Created app from min function")
    app.run(host=args.listen, port=args.port)

if __name__ == "__main__":
    print("main")
    # run from command line
    main()
else:
    # run from wsgi
    my_dir = f"{os.path.dirname(__file__)}"

    args = {
        "static_folder": f"{my_dir}/static",
        "template_folder": f"{my_dir}/templates",
        }

    application = create_app(**args)
    application.default_config_path = f"{my_dir}/rpmindex.yml"
