FROM tiryoh/ros2-desktop-vnc:galactic
LABEL maintainer="zeidk<zeid.kootbally@nist.gov>"
RUN . /opt/ros/galactic/local_setup.sh && \
    apt-get update && \
    mkdir -p ~/ariac_ws/src && \
    cd ~/ariac_ws && \
    git clone https://github.com/zeidk/ARIAC2023Docker.git src/ariac && \
    rosdep update --include-eol-distros && \
    rosdep install --from-paths src -y -i --rosdistro galactic && \
    sudo apt install python3-colcon-common-extensions && \
    colcon build
ENV USER ubuntu