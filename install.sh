#!/usr/bin/env bash
LARK_HOME=`dirname $0`
LARK_HOME=`cd -P $LARK_HOME; pwd`

PYTHON_BIN=$1
VPYTHON=$LARK_HOME/bin/venv

if [[ ! "`$PYTHON_BIN --version 2>&1`" =~ ^"Python 3.6."[0-9]+$ ]]; then
    echo "need python3.6"
    exit 1
fi

$PYTHON_BIN -m venv $VPYTHON

$VPYTHON/bin/pip install -r $LARK_HOME/requirements.txt
