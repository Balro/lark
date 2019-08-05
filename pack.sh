#!/usr/bin/env bash
LARK_HOME=`dirname $0`
OUTDIR="$LARK_HOME/out/lark"

rm -rf $LARK_HOME/out/* && mkdir $OUTDIR

cp -r $LARK_HOME/apps $LARK_HOME/bin $LARK_HOME/conf $LARK_HOME/templates $LARK_HOME/manage.py $LARK_HOME/requirements.txt $OUTDIR/

cd $LARK_HOME/out/
tar zcvf lark.tar.gz lark
