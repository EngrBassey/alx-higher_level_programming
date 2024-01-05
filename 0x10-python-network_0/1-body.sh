#!/bin/bash

#Display only body of 200 status code
curl -sLI $1 -o /dev/null -w '%{http_code}\n' | grep -q 200 && curl -sL $1
