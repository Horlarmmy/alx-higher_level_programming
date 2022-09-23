#!/bin/bash
# script that list all available method in a server
curl -s --head "$1" | grep "Allow:" | cut -d " " -f 2-4
