load("@rules_python//python:defs.bzl", "py_binary", "py_library")


py_binary(
  name = "server",
  main = "main.py",
  srcs = ["main.py"],
  deps = [
    "//libs/proto1:py_grpc_fran_lib",
  ]
)