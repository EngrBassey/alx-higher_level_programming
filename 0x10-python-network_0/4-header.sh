#!/bin/bash
# Use curl to send a GET request with a custom header and display the body
curl -s -H "X-School-User-Id: 98" "$1"
