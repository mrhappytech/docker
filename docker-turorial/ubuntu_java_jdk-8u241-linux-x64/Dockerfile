# LICENSE MIT License 2020
#
# ----------------------------------------------------------------------------------
# Ubuntu with Java JDK (8u241) Docker Image
# ----------------------------------------------------------------------------------
#
# This image contains Ubuntu image plus sudo, ping, vim, nano, less.
# It has installed Java JDK 8u241 (jdk-8u241-linux-x64).
#
# ----------------------------------------------------------------------------------
# created by: Vaclav Sramek <vaclav.sramek@gmail.com>
# ----------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------
# How to Install
# ----------------------------------------------------------------------------------
# 1) download jdk-8u241-linux-x64.tar.gz (Oracle Java SE Development Kit 8 for Linux x64)
#	from Oracle and place it into directory with this Dockerfile.
#
# 2) run command: docker build -t ubuntu_java_jdk8u241 .
#
# ---------------------------------------------------------------------------------- 

# Download base image ubuntu latest
FROM ubuntu:latest

# Update Ubuntu Software repository
RUN apt-get update

# Install basic tools
RUN apt install --assume-yes sudo
RUN apt install --assume-yes iputils-ping
RUN apt install --assume-yes vim
RUN apt install --assume-yes nano
RUN apt install --assume-yes less

# Set environment variables
ENV JAVA_INSTALL_DIR /opt/java
ENV JAVA_ARCHIVE jdk-8u241-linux-x64.tar.gz

# Create needed directories
ENV DOWNLOAD_DIR /tmp/install
RUN mkdir -p "${DOWNLOAD_DIR}"
RUN mkdir -p "${JAVA_INSTALL_DIR}"

# copy tar.gz into tmp directory
COPY ${JAVA_ARCHIVE} ${DOWNLOAD_DIR}

# unpack it
RUN tar -xzf "${DOWNLOAD_DIR}/${JAVA_ARCHIVE}" -C ${DOWNLOAD_DIR}

# delete install file
RUN rm -f "${DOWNLOAD_DIR}/${JAVA_ARCHIVE}"

# move unpacked java into target directory
RUN mv "${DOWNLOAD_DIR}/jdk1.8.0_241" "${JAVA_INSTALL_DIR}"

# set up Linux environment
RUN echo "JAVA_HOME=/opt/java/jdk1.8.0_241" >> /etc/profile
RUN echo "JRE_HOME=/opt/java/jdk1.8.0_241" >> /etc/profile
RUN echo "PATH=$PATH:$JRE_HOME/bin:$JAVA_HOME/bin" >> /etc/profile
RUN echo "export JAVA_HOME" >> /etc/profile
RUN echo "export JRE_HOME" >> /etc/profile
RUN echo "export PATH" >> /etc/profile

RUN update-alternatives --install "/usr/bin/java" "java" "/opt/java/jdk1.8.0_241/bin/java" 1
RUN update-alternatives --install "/usr/bin/javac" "javac" "/opt/java/jdk1.8.0_241/bin/javac" 1
RUN update-alternatives --install "/usr/bin/javaws" "javaws" "/opt/java/jdk1.8.0_241/bin/javaws" 1
RUN update-alternatives --set java /opt/java/jdk1.8.0_241/bin/java
RUN update-alternatives --set javac /opt/java/jdk1.8.0_241/bin/javac
RUN update-alternatives --set javaws /opt/java/jdk1.8.0_241/bin/javaws 

# Define default command to start bash
CMD ["bash"]