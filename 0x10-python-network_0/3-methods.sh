#!/bin/bash

# Use curl to send an OPTIONS request and display allowed methods
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
