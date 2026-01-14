from setuptools import setup, find_packages

setup(
    name="glueprint",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "pyfiglet>=0.8.0",
    ],
    entry_points={
        "console_scripts": [
            "glueprint=glueprint.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
