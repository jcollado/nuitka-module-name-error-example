#!/usr/bin/env python
"""MissionBio viral_transduction package."""

import os

from setuptools import find_namespace_packages, setup


setup(
    name="company.project_name",
    version="0.0.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
)
