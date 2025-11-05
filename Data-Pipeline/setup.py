from setuptools import find_packages, setup #type: ignore

setup(
    name="Data_Pipeline",
    packages=find_packages(exclude=["Data_Pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
