cmake_minimum_required(VERSION 3.27)
project(CSource C)

set(CMAKE_C_STANDARD 11)
add_compile_options(/Od)
add_executable(CSource main.c
)
