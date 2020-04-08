import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymathcal",  # Replace with your own username
    version="0.0.1",
    author="Siddhant Nair",
    author_email="sidd14nair@gmail.com",
    description="Complex mathematical functions Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SiddhantNair/pymathcal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
