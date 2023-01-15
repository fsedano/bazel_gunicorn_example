import grpc
import libs.proto1.user_pb2 as user_pb2
import libs.proto1.user_pb2_grpc as user_pb2_grpc

from concurrent import futures

import logging
logging.basicConfig(level=logging.INFO)

class Server():
    def Get(self, request, context):
        logging.info("Got GET")
        return user_pb2.User(Name="pepe")
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserSvcServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()