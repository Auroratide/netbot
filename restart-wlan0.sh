#!/bin/bash
# check if a wlan0 if exists
if echo `/sbin/ifconfig` | grep -q wlan0; then
  #check if there is IP Address
  if echo `/sbin/ifconfig wlan0` | grep -q "inet addr"; then
    exit 0
  fi
  echo restarting wlan0
  /sbin/modprobe -r 8192cu
fi
/sbin/modprobe 8192cu
exit 0
