from setuptools import setup, find_packages

setup(
    name="python_gt_client",
    version="0.1.0",
    author="TackTech",
    description=(
        "Python client for the Mieza GTO service "
        "(generated from OpenAPI)."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tacktech-ai/tacktech",
    packages=find_packages(),
    install_requires=[
        "attrs>=23.1.0",
        "httpx>=0.24.1",
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.1",
)
