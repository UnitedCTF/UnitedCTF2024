cmake_minimum_required(VERSION 3.25)
project(UnitedSlots)

find_package(Boost 1.74 COMPONENTS program_options REQUIRED)

add_executable(UnitedSlots1 unitedslots1.cpp)
add_executable(UnitedSlots2 unitedslots2.cpp)

target_link_libraries(UnitedSlots1 Boost::program_options)
target_link_libraries(UnitedSlots2 Boost::program_options)
