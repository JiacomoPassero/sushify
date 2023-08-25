import setuptools
with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sushify",
    version="0.0.1",
    author="me medesimo",
    author_email="282844@studenti.unimore.it",
    description="un predittore di preferenze sui piatti di un menu, pensato per il sushi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JiacomoPassero/sushify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)