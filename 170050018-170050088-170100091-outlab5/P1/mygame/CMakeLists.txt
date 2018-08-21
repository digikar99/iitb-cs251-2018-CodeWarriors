cmake_minimum_required (VERSION 3.5.1)

# Reference: http://derekmolloy.ie/hello-world-introductions-to-cmake/
project (outlab5-p9)

add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic /usr/local/lib/libMyEngineStatic.a)


add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic /usr/local/lib/libMyEngineDynamic.so)
