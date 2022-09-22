from importlib.resources import Package
import os
from pathlib import Path

package_name="deep_Classifier"

list_of_files=[
    ".github\workflows\.gitkeep",
    f"src\{package_name}\__init__.py",
    f"src\{package_name}\components\__init__.py",
    f"src\{package_name}\utils\__init__.py",
    f"src\{package_name}\config\__init__.py",
    f"src\{package_name}\pipeline\__init__.py",
    f"src\{package_name}\entity\__init__.py",
    f"src\{package_name}\constants\__init__.py",
    "configs\configs.yaml"
    "dvc.yaml"
    "params.yaml"
    "init_setup.sh"
    "requirnments.txt"
    "requirnments_dev.txt"
    "setup.py"
    "setup.cfg"
    "pyproject.toml"
    "tox.ini"
    "research/trials.ipynb"
]

