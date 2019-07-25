# LICENSE MIT License 2019
#
# ----------------------------------------------------------------------------------
# Oracle Weblogic 11g (wls1036) Docker Image
# ----------------------------------------------------------------------------------
#
# This image DOES NOT contain a Weblogic domain! 
# It contains just Weblogic installation.
#
# ----------------------------------------------------------------------------------
# created by: Vaclav Sramek <vaclav.sramek@gmail.com>
# ----------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------
# How to Install
# ----------------------------------------------------------------------------------
#
# 1) you will need ubuntu_java_jdk7u80 Docker image.
#
# 2) download wls1036_generic.jar from Oracle and place it into directory with 
#    this Dockerfile.
#
# 3) prepare weblogic configuration file wls-silent.xml
#
# 4) run command: docker build -t ubuntu_weblogic_11g .
#
# ----------------------------------------------------------------------------------

# Use previously prepared image
FROM ubuntu_java_jdk7u80

# Set environment variables
ENV WEBLOGIC_PACKAGE wls1036_generic.jar
ENV WEBLOGIC_CONFIG wls-silent.xml

# Prepare user directory and create oracle user
RUN mkdir /user01 && \
    chmod a+xr /user01 && \
    useradd -b /user01 -m -s /bin/bash oracle 

# Copy packages
COPY $WEBLOGIC_PACKAGE /user01/
COPY $WEBLOGIC_CONFIG /user01/

# Change the open file limits in /etc/security/limits.conf
RUN sed -i '/.*EOF/d' /etc/security/limits.conf && \
    echo "* soft nofile 16384" >> /etc/security/limits.conf && \ 
    echo "* hard nofile 16384" >> /etc/security/limits.conf && \ 
    echo "# EOF"  >> /etc/security/limits.conf

# Change the kernel parameters that need changing.
RUN echo "net.core.rmem_max=4192608" > /user01/oracle/.sysctl.conf && \
    echo "net.core.wmem_max=4192608" >> /user01/oracle/.sysctl.conf && \ 
    sysctl -e -p /user01/oracle/.sysctl.conf

# Adjust file permissions, go to /user01 as user 'oracle' to proceed with WLS installation
RUN chown oracle:oracle -R /user01
WORKDIR /user01
USER oracle

# Installation of WebLogic 
RUN java -jar $WEBLOGIC_PACKAGE -mode=silent -silent_xml=/user01/wls-silent.xml && \ 
	rm $WEBLOGIC_PACKAGE /user01/wls-silent.xml 

WORKDIR /user01/oracle/

ENV PATH $PATH:/user01/oracle/weblogic/oracle_common/common/bin

# Define default command to start bash. 
CMD ["bash"]