#!/usr/bin/env bash
gunicorn api.routers:app -w 2 --preload --reload -t 30 --bind 0.0.0.0:8080