from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
# Get requirements from requirements.txt to a list
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    install_requires = f.read().splitlines()


setup(
    name="agent-llm",
    version="1.1.36-beta",
    description="An Artificial Intelligence Automation Platform. AI Instruction management from various providers, has an adaptive memory, and a versatile plugin system with many commands including web browsing. Supports many AI providers and models and growing support every day.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This should match the format of your README
    author="Josh XT",
    author_email="josh@devxt.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=install_requires,
)
