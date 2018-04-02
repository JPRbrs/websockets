#!/bin/bash
echo "Restarting app..."

kill -HUP `cat app.pid`
