#!/bin/sh

gunicorn -b 0.0.0.0:8000 manage:app --reload
