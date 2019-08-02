#!/usr/bin/env bash
BIN=`dirname $0`
BIN=`cd -P $BIN; pwd`

PYTHON_BIN=$1
VPYTHON=$BIN/venv

if [[ ! "`$PYTHON_BIN --version 2>&1`" =~ ^"Python 3.6."[0-9]+$ ]]; then
    echo "need python3.6"
    exit 1
fi

$PYTHON_BIN -m venv $VPYTHON

$VPYTHON/bin/pip install -r $BIN/../requirements.txt
