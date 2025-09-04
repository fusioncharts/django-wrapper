from setuptools import setup, find_packages

setup(
    name="fusioncharts_py_wrapper",
    version="1.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "fusioncharts_py_wrapper": [
            "static/fusioncharts_py_wrapper/**/*.js",  # recursive match for js files in js/ and subdirs
        ],
    },
    author="FusionCharts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
