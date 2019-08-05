#!/usr/bin/env bash
LARK_HOME=`dirname $0`
OUTDIR="$LARK_HOME/out/lark"

rm -rf $LARK_HOME/out/* && mkdir $OUTDIR

cp -r $LARK_HOME/apps $OUTDIR/
cp -r $LARK_HOME/bin $OUTDIR/
cp -r $LARK_HOME/conf $OUTDIR/
cp -r $LARK_HOME/templates $OUTDIR/
cp -r $LARK_HOME/manage.py $OUTDIR/
cp -r $LARK_HOME/requirements.txt $OUTDIR/
cp -r $LARK_HOME/install.sh $OUTDIR/

cd $LARK_HOME/out/
tar zcvf lark.tar.gz lark
