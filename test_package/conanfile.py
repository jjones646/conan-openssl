import os

from conans.model.conan_file import ConanFile
from conans import CMake


class OpenSSLConanPackageTest(ConanFile):
    version = "0.0.0"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")

    def test(self):
        self.run('cd bin && .{!s}OpenSSLPackageTest'.format(os.sep))
        assert os.path.exists(os.path.join(self.deps_cpp_info["OpenSSL"].rootpath, "LICENSE"))
