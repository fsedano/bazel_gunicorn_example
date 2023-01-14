load("@rules_python//python:defs.bzl", "py_library")
load("@my_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

exports_files(["requirements_lock.txt"])
py_library(
    name = "flask",
    deps = [
        requirement("Flask"),
        requirement("Jinja2"),
        requirement("Werkzeug"),
        requirement("itsdangerous"),
        requirement("click"),
        requirement("MarkupSafe"),
        requirement("gunicorn"),
        requirement("setuptools"),
        requirement("pytest"),
    ],
)

py_library(
    name = "unittest",
    deps = [
        requirement("pytest"),
    ],
)


