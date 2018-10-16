#!/usr/bin/bash
echo "[drucker-grpc-proto run_codegen.sh START]"

cd `dirname $0`

python -m grpc.tools.protoc -I. --python_out=./protobuf --grpc_python_out=./protobuf drucker.proto
