#!/bin/bash
# takes in a URL, sends a request to that UR
url=$1
result=$(curl -I "$url" | grep -i Content-Length | awk '{print $2}')
echo "$result"
