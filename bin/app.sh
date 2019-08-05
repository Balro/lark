#!/usr/bin/env bash
BIN=`dirname $0`
BIN=`cd -P $BIN; pwd`
VPYTHON=$BIN/venv/bin/python3
HOST=localhost
PORT=20002
HOME="$(dirname $0)/.."

start(){
    if [ `status` = "ok" ]; then
        echo "Is already running!"
        exit 1
    fi
    mkdir -p $HOME/logs
    nohup $VPYTHON $HOME/manage.py runserver $HOST:$PORT >> $HOME/logs/start.out 2>&1 &
    try=0
    while [ `status` != "ok" ]; do
        if [ $try -gt 5 ]; then
            echo "Start failed."
            exit
        fi
        echo -n "."
        let try++
        sleep 1s
    done
    echo " started."
}

stop(){
    if [ `status` = "ok" ]; then
        pid=`netstat -anop | grep -w $PORT | awk '{print $7}'`
        pid=${pid%%/*}
        echo "kill $pid" && kill $pid
        try=0
        while [ `status` = "ok" ]; do
            if [ $try -gt 5 ]; then
                echo "Still running, please retry."
                exit
            fi
            echo -n "."
            kill $pid
            let try++
            sleep 1s
        done
        echo "down."
    else
        echo "down."
    fi
}

status() {
    s=`curl $HOST:$PORT/status 2>/dev/null`
    if [ -z "$s" ]; then
        echo "down."
    else
        echo "$s"
    fi
}


case $1 in
    start)
        start
    ;;
    stop)
        stop
    ;;
    status)
        status
    ;;
    *)
        echo "$0 <start|stop|status>"
    ;;
esac
