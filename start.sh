#!/usr/bin/env bash
gunicorn api.routers:app -w 2 --preload --reload -t 30 --bind 127.0.0.1:8080