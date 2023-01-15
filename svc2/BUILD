load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
    name = "ws",
    srcs = 
        glob(["src/*.py"])
    ,
    deps = [
        "//libs/proto1:py_grpc_fran_lib",
        "//franlibs/lib1:lib1_lib",
        "//franlibs/lib2:lib2_lib"
    ],
)


py_binary(
  name = "main",

  srcs = ["main.py"],
  deps = [
    ":ws",
  ]
)