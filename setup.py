import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

def build(name, version, descritpion, packages, install_requires = []):
    setuptools.setup(
        name=name,
        version=version,
        author="Zarlo",
        author_email="5899@zarlo.dev",
        descritpion=descritpion,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/user-of-linux/package-manager",
        classifiers=[
            "Programming Language :: Python :: 3"
        ],
        packages=packages,
        install_requires=install_requires,
        zip_safe=False,
        include_package_data=True
    )

build("uol-package-manager", "0.1.0", "uol package manager", ["uol_package_manager"])