load("@rules_python//python:defs.bzl", "py_binary")

package(default_visibility = ["//visibility:public"])


py_library(
    name = "ws",
    srcs = 
        glob(["src/*.py"])
    ,
    deps = [
    "//3rdparty/python:flask"
    ],
)
py_binary(
  name = "main",

  srcs = ["main.py"],
  deps = [
    ":ws"
  ]
)