load("@rules_python//python:defs.bzl", "py_binary")


py_binary(
  name = "main",

  srcs = ["main.py"],
  deps = [
    "//libs/lib1",
    "//libs/proto1:py_grpc_lib"
  ]
)