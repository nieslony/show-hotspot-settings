#!/bin/bash

VERSION=0.1
PACKAGE_NAME=show-hotspot-settings
SOURCE="web apache-config LICENSE $PACKAGE_NAME.spec"

mkdir -v dist
tar --transform "s/^/$PACKAGE_NAME-$VERSION\//" -cvzf dist/$PACKAGE_NAME-$VERSION.tar.gz $SOURCE

