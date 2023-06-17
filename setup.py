from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="llm-hello-world",
    description="Hello world plugin for LLM",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/llm-hello-world",
    project_urls={
        "Issues": "https://github.com/simonw/llm-hello-world/issues",
        "CI": "https://github.com/simonw/llm-hello-world/actions",
        "Changelog": "https://github.com/simonw/llm-hello-world/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=["License :: OSI Approved :: Apache Software License"],
    version=VERSION,
    packages=["llm_hello_world"],
    entry_points={"llm": ["llm_hello_world = llm_hello_world"]},
    install_requires=["llm"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
