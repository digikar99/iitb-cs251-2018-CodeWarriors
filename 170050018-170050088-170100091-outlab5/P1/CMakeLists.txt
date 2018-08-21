cmake_minimum_required (VERSION 3.5.1)

# Reference: http://derekmolloy.ie/hello-world-introductions-to-cmake/
project (outlab5-p8)
add_executable(helloworld helloworld.cpp)
add_executable(usespthread usespthread.cpp)

# Reference: https://stackoverflow.com/questions/1620918/cmake-and-libpthread
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(usespthread Threads::Threads)

file(GLOB shared_lib "myengine/myengine.cpp")
add_library(MyEngineDynamic SHARED ${shared_lib})
install(TARGETS MyEngineDynamic DESTINATION /usr/local/lib)

file(GLOB static_lib "myengine/myengine.cpp")
add_library(MyEngineStatic STATIC ${static_lib})
install(TARGETS MyEngineStatic  DESTINATION /usr/local/lib)

install(FILES "myengine/myengine.hpp" DESTINATION /usr/local/include)
