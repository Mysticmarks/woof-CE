#!/bin/sh
# Wrapper to run build stages via plugins.

if [ ! -f ./WOOFMERGEVARS ] ; then
        echo "run merge2out"
        exit 1
fi

python3 plugin_runner.py "$@"
