load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    sha256 = "48a838a6e1983e4884b26812b2c748a35ad284fd339eb8e2a6f3adf95307fbcd",
    strip_prefix = "rules_python-0.16.2",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.16.2.tar.gz",
)


load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:pip.bzl", "pip_parse")
# Create a central repo that knows about the dependencies needed from
# requirements_lock.txt.
pip_parse(
   name = "my_deps",
   requirements_lock = "//3rdparty/python:requirements_lock.txt",
   #requirements_lock = "//:requirements_lock.txt"
)
# Load the starlark macro which will define your dependencies.
load("@my_deps//:requirements.bzl", "install_deps")
# Call it to define repos for your requirements.
install_deps()
