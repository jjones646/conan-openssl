[![Join the chat at https://gitter.im/lasote/conan-openssl](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/lasote/conan-openssl?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# conan-openssl

[Conan](https://conan.io) package for OpenSSL library

## Build packages

Only necessary if you don't want to use the pre-compiled binaries, and you want to build your own packages from source.

Download conan client from [conan.io](https://conan.io) and run:

    $ conan create user/channel

## Upload packages to server

    $ conan upload OpenSSL/1.0.2-m@user/channel --all

## Reuse the packages

### Basic setup

    $ conan install OpenSSL/1.0.2-m@user/channel

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    # Using the latest semver compatible package here
    OpenSSL/[~=1.0.2-]@user/channel

    [options]
    OpenSSL:shared=false # true
    # Take a look for all available options in conanfile.py

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all its dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
