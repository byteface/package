setup(
    name="package test",
    version="1.0.0",
    description="test packaging a server and browser launcher",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/byteface/package",
    author="@byteface",
    author_email="byteface@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "tkinter", "websockets", "domonic", "sanic"
    ]
)