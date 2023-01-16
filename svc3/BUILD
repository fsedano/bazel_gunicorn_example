load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")



py_binary(
  name = "server",
  main = "main.py",
  srcs = ["main.py"],
  deps = [
    "//libs/proto1:py_grpc_fran_lib",
  ]
)

py3_image(
  name = "server_image",
  main = "main.py",
  srcs = ["main.py"],
  deps = [
    "//libs/proto1:py_grpc_fran_lib",
  ]
)
