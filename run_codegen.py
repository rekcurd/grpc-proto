#!/usr/bin/python
# -*- coding: utf-8 -*-

from grpc_tools import protoc
import os

sd = os.path.abspath(os.path.dirname(__file__))
os.chdir(sd)

protoc.main(('', '-I.', '--python_out=../', '--grpc_python_out=../', 'drucker.proto',))
