FROM tiryoh/ros2-desktop-vnc:galactic
LABEL maintainer="zeidk<zeid.kootbally@gmail.com>"
RUN . /opt/ros/galactic/local_setup.sh && \
    apt-get update && \
    mkdir -p ~/ariac_ws/src && \
    cd ~/ariac_ws && \
    git clone https://github.com/zeidk/ARIAC2023Docker.git src/ariac && \
    sudo apt install python3-rosdep -y && \
    sudo apt-get install terminator -y && \
    rosdep update --include-eol-distros && \
    rosdep install --from-paths src -y -i --rosdistro galactic && \
    sudo apt install python3-colcon-common-extensions && \
    colcon build --parallel-workers 2
ENV INSIDE_DOCKER ok
ENV USER ubuntu