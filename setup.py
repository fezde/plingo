import re

from setuptools import setup

with open("src/plingo/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Plingo",
    version=version,
    install_requires=[
        "numpy==1.19.1",
        "opencv-python==4.4.0.42",
        "progressbar2==3.53.1",
    ],
    extras_require={},
)
