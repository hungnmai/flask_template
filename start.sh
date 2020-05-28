#!/usr/bin/env bash
uwsgi --socket 0.0.0.0:8080 --protocol=http -w wsgi:app --threads=1 --processes=16