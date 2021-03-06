from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='helloworld',
    version='0.0.1',
    author="JTap159",
    author_email="engjat94@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtap159/helloworld",
    packages=find_packages(),  # needs a folder with __init__()
    # py_modules=["helloworld"], # use if you only have modules
    # package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    }
)
