#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep -i Allow | cut -d " " -f2-
