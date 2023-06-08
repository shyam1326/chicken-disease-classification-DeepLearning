import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="cnn_classifier",
    version="0.0.1",
    author="Shyam1326",
    author_email="shshyam96@gmail.com",
    description="A small package for classifying chicken diseases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Shyam1326/chicken-disease-classification-DeepLearning",
    project_urls={
        "Bug Tracker": f"https://github.com/Shyam1326/chicken-disease-classification-DeepLearning"
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


