#!/bin/bash
# takes in a URL, sends a request to that UR
curl -Is "$1" | grep -i Content-Length | awk '{print $2}'
