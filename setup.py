import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yahfin", # Replace with your own username
    version="0.3.5",
    author="Anil Sardiwal",
    author_email="theonlyanil@gmail.com",
    description="Yahoo Finance Python Wrapper (Unofficial)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theonlyanil/yahfin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.7.7',
)
