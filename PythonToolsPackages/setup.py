import setuptools

with open("/README.md" , "r" , encoding="utf-8") as f:
        more_description = f.read()

setuptools.setup(
    name="PythonTools",
    version='0.0',
    author="Matt Clarke",
    description="Tools for General shortcuts",
    url="https://github.com/MattClarke873/PythonPackage/",
    project_urls={
    "Bug Tracker": "https://github.com/MattClarke873/PythonPackage/issues"
    },
    packages=['PythonTools']

)