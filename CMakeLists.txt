cmake_minimum_required(VERSION 3.5)

project(image_view)


# ROS2 Flags
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rmw_implementation REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(tf2_eigen REQUIRED)
find_package(image_geometry REQUIRED)
find_package(image_transport REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(stereo_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(OpenCV REQUIRED)
find_package(Boost REQUIRED COMPONENTS signals system filesystem)
find_package(GTK2)
find_package(std_srvs REQUIRED)
add_definitions(-DHAVE_GTK)
include_directories(${GTK2_INCLUDE_DIRS})

if(cv_bridge_VERSION VERSION_GREATER "1.12.0")
  add_compile_options(-std=c++11)
endif()



add_executable(image_view src/image_view.cpp)
ament_target_dependencies(image_view
  image_transport
  image_geometry
  cv_bridge
  message_filters
  rclcpp
  stereo_msgs
  sensor_msgs
  rmw_implementation
  cv_bridge
  OpenCV
  Boost
)

add_executable(stereo_view src/stereo_view.cpp)
ament_target_dependencies(stereo_view
  image_transport
  image_geometry
  cv_bridge
  message_filters
  rclcpp
  stereo_msgs
  sensor_msgs
  rmw_implementation
  cv_bridge
  OpenCV
  Boost
)

add_executable(extract_images src/extract_images.cpp)
ament_target_dependencies(extract_images
  image_transport
  image_geometry
  cv_bridge
  message_filters
  rclcpp
  stereo_msgs
  sensor_msgs
  rmw_implementation
  cv_bridge
  OpenCV
  Boost
)

add_executable(image_saver src/image_saver.cpp)
ament_target_dependencies(image_saver
  image_transport
  image_geometry
  cv_bridge
  std_srvs
  message_filters
  rclcpp
  stereo_msgs
  sensor_msgs
  rmw_implementation
  cv_bridge
  OpenCV
  Boost
)

add_executable(video_recorder src/video_recorder.cpp)
ament_target_dependencies(video_recorder
  image_transport
  image_geometry
  cv_bridge
  std_srvs
  rclcpp
  sensor_msgs
  rmw_implementation
  cv_bridge
  OpenCV
  Boost
)

install(TARGETS 
        image_view
        stereo_view
        extract_images
        image_saver
        video_recorder
        DESTINATION lib/${PROJECT_NAME})      
ament_package()