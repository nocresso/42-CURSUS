#!/bin/bash

ifconfig -a | grep -Eo '([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}'
