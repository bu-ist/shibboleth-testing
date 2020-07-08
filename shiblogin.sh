#!/bin/sh -x
#
echo "$@"
if [ "x$1" = "xdevcontainer" ]; then
  while sleep 1000; do
    echo "sleeping"
  done
fi
sleep 5
/root/shiblogin.py "$@"