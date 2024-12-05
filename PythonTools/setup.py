import setuptools

with open("/README.md" , "r" , encoding="utf-8") as f:
        more_description = f.read()

setuptools.setup(
    name="PythonTools",
    version='0',
    author="author_name",
    description="project_description",
    url="https://github.com/MattClarke873/PythonPackage/",
    project_urls=""
)