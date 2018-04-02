#!/bin/bash

gunicorn app.websockets:app -b 0.0.0.0:8080 --workers 1 --log-level warning --log-file logs/gunicorn-errors.log --access-logfile logs/gunicorn-access.log  --name websockets -p app.pid -D
