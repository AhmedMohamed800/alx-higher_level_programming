#!/bin/bash
# takes in a URL, sends a request to that UR
curl -s -X GET "$1" -L
