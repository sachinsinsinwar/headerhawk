from setuptools import setup, find_packages

setup(
    name="headerhawk",
    version="1.0.0",
    author="Sachin Singh",
    author_email="sachinsinsinwar8@gmail.com",
    description="Security Header Analyzer — CLI tool for pentesters, DevOps and developers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sachinsinsinwar/headerhawk",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "headerhawk=cli.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
)
