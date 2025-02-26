#!/bin/bash

VERSION=0.2.3
PACKAGE_NAME=show-hotspot-settings
SOURCE="showhotspotsettings apache-config setup.py $PACKAGE_NAME.wsgi LICENSE README.md $PACKAGE_NAME.spec"

mkdir -v dist
tar --transform "s/^/$PACKAGE_NAME-$VERSION\//" -cvzf dist/$PACKAGE_NAME-$VERSION.tar.gz $SOURCE
