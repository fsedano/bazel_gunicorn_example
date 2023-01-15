load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_k8s//k8s:object.bzl", "k8s_object")

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

#container_image(
#    name = "app",
    # References container_pull from WORKSPACE (above)
#    base = "@java_base//image",
#    files = [":main.py"],
#    cmd = ["ls"]
#)

py3_image(
  name = "main_image",
  main = "main.py",
  srcs = ["main.py"],
  deps = [
    ":ws"
  ]
)

k8s_object(
    name = "main_k8s",
    kind = "deployment",
    template = ":deployment.yaml",
    cluster = "default",
    images = {
        "fsedano/k8stest:null" : ":main_image"
    },
)