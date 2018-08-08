#!/usr/bin/bash
echo "[drucker-grpc-proto run_codegen.sh START]"

cd `dirname $0`

python -m grpc.tools.protoc -I/usr/local/include -I. --python_out=../ --grpc_python_out=../ drucker.proto
