# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from setuptools import setup
from setupconfig.datamng import DataManager


def main():

    long_description = open("README.md", encoding="utf-8").read()

    dm = DataManager()
    pkg_name, version, packages, package_data = dm.get_selected_data()

    setup(
        name=pkg_name,
        version=version,
        url="https://github.com/numediart/vsensebox-data",
        license="GPL-3.0-or-later",
        description="Dynamic data packager for the supported detector/tracker of VSenseBox.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=packages,
        package_data=package_data,
        include_package_data=True,
        author="Ratha SIV",
        maintainer="rathaROG",
        install_requires=None,
        python_requires=">=3.9",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Software Development",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ],
    )

if __name__ == "__main__":
    main()
