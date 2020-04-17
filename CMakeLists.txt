cmake_minimum_required(VERSION 3.0.0)
project(findpoint VERSION 0.1.0)

find_package(OpenCV 3.4.10 REQUIRED)

aux_source_directory(forest SRC_LIST)
include_directories(forest)

add_executable(findpoint main.cpp ${SRC_LIST})

target_link_libraries(findpoint ${OpenCV_LIBS} )
