#!/bin/bash
<<<<<<< HEAD

size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
echo "$size"
=======
# Script that takes in a URL, sends a request and displays the size of the body of the response
curl -sI $1 | awk '/Content-Length/ {print $2}' | tr -d '\r'        
>>>>>>> 721b57f84e1a29b51419b007804e356d01fd7de8
