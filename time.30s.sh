#!/bin/bash
date -u +'%H:%M UTC'
echo '---'
echo -n "UTC " ; TZ=":UTC" date +'%l:%M %p'
echo -n "NY (Eastern) " ; TZ=":US/Eastern" date +'%l:%M %p'
echo -n "KS (Central) " ; TZ=":US/Central" date +'%l:%M %p'
echo -n "SF (Pacific) " ; TZ=":US/Pacific" date +'%l:%M %p'
