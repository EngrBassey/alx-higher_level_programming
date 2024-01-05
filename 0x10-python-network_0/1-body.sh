#!/bin/bash

# Use curl to send a GET request and display "Route 2" if the status code is 200
curl -sLI $1 -o /dev/null -w '%{http_code}\n' | grep -q 200 && curl -sL $1
