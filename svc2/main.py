from franlibs.lib1.src.lib1 import  FunLib1
from franlibs.lib2.src.datos2 import F2
#from libs.lib1 import Datos
import grpc
import libs.proto1.user_pb2 as user_pb2
import libs.proto1.user_pb2_grpc as user_pb2_grpc
import logging
logging.basicConfig(level=logging.INFO)

def get_user(stub):
    response = stub.Get(user_pb2.RequestId(Id=1))
    logging.info(f"Response={response.Name}")

with grpc.insecure_channel('localhost:50051') as channel:
    stub = user_pb2_grpc.UserSvcStub(channel)
    get_user(stub)
    