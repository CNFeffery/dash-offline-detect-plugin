from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
setup(
    name="dash-offline-detect-plugin",
    version="0.1.2",
    install_requires=[
        "dash>=3.0.4",
    ],
    packages=["dash_offline_detect_plugin"],
    author="CNFeffery",
    author_email="fefferypzy@gmail.com",
    description="Offline detect plugin for Dash applications using Dash Hooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CNFeffery/dash-offline-detect-plugin",
)
