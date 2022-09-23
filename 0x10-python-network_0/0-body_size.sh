#!/usr/bin/bash

curl -Si $1 | grep -i Content-lenght | cut -d " " -f2
