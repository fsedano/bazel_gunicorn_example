from franlibs.lib1.src.lib1 import  FunLib1
from franlibs.lib2.src.datos2 import F2
#from libs.lib1 import Datos
import grpc
import libs.proto1.user_pb2
import libs.proto1.user_pb2_grpc
import sys
print("Hola\n")
#print(f"d={Datos()}")
#print(f"La suma es {FunLib1(2,3)}")
print(f"F is {F2()}")

print("*** PATH ***")
for el in sys.path:
    print(el)