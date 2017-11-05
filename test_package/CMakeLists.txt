project( OpenSSLConanPackageTest )
cmake_minimum_required( VERSION  3.0 )
include( "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake" )
conan_basic_setup( TARGETS )

add_executable( OpenSSLPackageTest
    md5.cpp
)
target_link_libraries( OpenSSLPackageTest
    PRIVATE  CONAN_PKG::OpenSSL
)
