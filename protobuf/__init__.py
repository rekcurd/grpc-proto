# coding: utf-8


import sys
import os
import pathlib


root_path = pathlib.Path(os.path.abspath(__file__)).parent
sys.path.append(str(root_path))


from .rekcurd_pb2 import *
from .rekcurd_pb2_grpc import *
