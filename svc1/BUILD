load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_k8s//k8s:object.bzl", "k8s_object")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@io_bazel_rules_docker//lang:image.bzl", "app_layer")



package(default_visibility = ["//visibility:public"])



py_library(
    name = "ws",
    srcs = 
        glob(["src/*.py"])
    ,
    deps = [
    "//3rdparty/python:flask",
        "//libs/proto1:py_grpc_fran_lib",
        "//franlibs/lib1:lib1_lib"
    ],
)
py_binary(
  name = "main",

  srcs = ["main.py"],
  deps = [
    
    ":ws"
  ]
)

container_image(
    name = "symlinked_buildpack_deps",
    base = "@python_container//image",
    symlinks = {
        "/usr/bin/python": "/usr/local/bin/python",
    },
)

app_layer(
    name = "my_py3_image",
    base = "@python_container//image",
    binary = ":my_py3_binary",
    create_empty_workspace_dir = True,
    entrypoint = ["/usr/bin/python3"]
)
py_binary( 
  name = "my_py3_binary",
  main = "main.py",
  srcs = ["main.py"],
  deps = [
    ":ws",
  ],
)

py3_image(
  name = "main_image",
  main = "main.py",
  srcs = ["main.py"],
     base = ":symlinked_buildpack_deps",
  deps = [
    ":ws",
  ],
     # base =  "@python_container//image",
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