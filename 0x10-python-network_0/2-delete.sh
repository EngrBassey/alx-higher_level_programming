#!/bin/bash
# Takes in a URL, sends DEL request to the URL, displays the body of the response
curl -sX DELETE "$1"
