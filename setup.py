from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xphrase",
    version="1.0.0",
    author="Gerivanc",
    author_email="your-email@example.com",
    description="Expressive phrase generator, strong, modern and minimalist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gerivanc/xphrase",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "xphrase-generate=xphrase:main",
        ],
    },
    include_package_data=True,
)
