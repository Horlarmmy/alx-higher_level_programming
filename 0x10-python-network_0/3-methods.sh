#!/bin/bash
# script that list all available method in a server
curl -sI --head "$1" | grep "Allow:" | cut -d " " -f 2-
