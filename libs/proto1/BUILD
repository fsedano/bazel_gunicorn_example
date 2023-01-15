load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "user_proto",
    srcs = ["user.proto"],
    deps = ["@com_google_protobuf//:any_proto"],
)

python_grpc_library(
    name = "py_grpc_fran_lib",
    protos = [":user_proto"]
)
