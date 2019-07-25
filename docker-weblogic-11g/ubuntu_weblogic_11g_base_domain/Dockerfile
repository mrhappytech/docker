# LICENSE MIT License 2019
#
# ----------------------------------------------------------------------------------
# Base Domain for Oracle Weblogic 11g (wls1036) Docker Image
# ----------------------------------------------------------------------------------
#
# This image contains basic domain with Admin server.
# It can also create managed servers and start them automatically.
#
# Inspiration taken from:
#   https://github.com/gibaholms/docker
#   https://github.com/playniuniu/docker-weblogic-domain
#
# ----------------------------------------------------------------------------------
# created by: Vaclav Sramek <vaclav.sramek@gmail.com>
# ----------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------
# How to Install
# ----------------------------------------------------------------------------------
#
# 1) you will need ubuntu_weblogic_11g Docker image.
#
# 2) prepare weblogic configuration files:
#	create-managed-server.py, create-managed-server.sh, create-wls-domain.py,
#     wait-for-admin-server.sh 
#
# 3) run command: docker build -t ubuntu_weblogic_11g_base_domain .
#
# ----------------------------------------------------------------------------------
# How to run it
# ----------------------------------------------------------------------------------
#
# 1) Create bridge network
#		docker network create -d bridge weblogic
#
# 2) Run AdminServer   (name=wlsadmin is used inside scripts later !!!)
#		docker run -d -p 7001:7001 --net weblogic --name=wlsadmin ubuntu_weblogic_11g_base_domain
#
# 3) create Managed servers:
#		docker run -d --net weblogic -p 7101:7101 -e MS_NAME=managed1 ubuntu_weblogic_11g_base_domain create-managed-server.sh
#
#		docker run -d --net weblogic -p 7102:7102 -e MS_NAME=managed2 ubuntu_weblogic_11g_base_domain create-managed-server.sh
#
#	or just use docker-compose and it will start automatically.
#
#
# 4) use browser with url: 
# 			http://192.168.99.100:7001/console/
#			http://127.0.0.1:7001/console/
# ----------------------------------------------------------------------------------

# Pull base image
# ---------------
FROM ubuntu_weblogic_11g

# WLS Configuration - Domain
# -------------------------------
ENV DOMAIN_NAME "base_domain"
ENV DOMAIN_HOME /user01/oracle/weblogic/user_projects/domains/${DOMAIN_NAME}
ENV CLUSTER_NAME "DockerCluster"

# WLS Configuration - Admin server
# -------------------------------
ENV ADMIN_HOST "wlsadmin"
ENV ADMIN_PORT 7001
ENV NODE_MANAGER_PORT 5556
ENV ADMIN_PASSWORD "welcome01"

# WLS Configuration - Managed servers
# -------------------------------
#ENV MANAGED_1_NAME "managed1"
#ENV MANAGED_1_PORT 7101
#ENV MANAGED_2_NAME "managed2"
#ENV MANAGED_2_PORT 7102
ENV MANAGED_MEM_ARGS "-Xms1024m -Xmx1024m -XX:MaxPermSize=512m"
ENV MANAGED_LOGGING "-Dweblogic.log.Log4jLoggingEnabled=true"

# Add files required to build this image
COPY scripts/* /user01/oracle/

# Root commands
USER root
RUN echo ". /user01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /root/.bashrc && \
    echo "export PATH=$PATH:/user01/oracle/weblogic/wlserver_10.3/common/bin:/user01/oracle/weblogic/user_projects/domains/base_domain/bin" >> /root/.bashrc

# Configuration of WLS Domain
USER oracle
WORKDIR /user01/oracle/weblogic
RUN /user01/oracle/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /user01/oracle/create-wls-domain.py && \
    mkdir -p /user01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security && \
    echo "username=weblogic" > /user01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \ 
    echo "password=$ADMIN_PASSWORD" >> /user01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
    echo ". /user01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /user01/oracle/.bashrc && \ 
    sed -i -e 's/^WLS_USER=.*/WLS_USER=\"weblogic\"/' /user01/oracle/weblogic/user_projects/domains/base_domain/bin/startManagedWebLogic.sh && \
    sed -i -e 's/^WLS_PW=.*/WLS_PW=\"${ADMIN_PASSWORD}\"/' /user01/oracle/weblogic/user_projects/domains/base_domain/bin/startManagedWebLogic.sh && \
    echo "export PATH=$PATH:/user01/oracle/weblogic/wlserver_10.3/common/bin:/user01/oracle/weblogic/user_projects/domains/base_domain/bin" >> /user01/oracle/.bashrc
	
# Expose Node Manager default port, and also default http/https ports for admin console
EXPOSE $NODE_MANAGER_PORT $ADMIN_PORT 

# Final setup
WORKDIR /user01/oracle

ENV PATH $PATH:/user01/oracle/weblogic/wlserver_10.3/common/bin:/user01/oracle/weblogic/user_projects/domains/base_domain/bin:/user01/oracle

# Define default command to start bash. 
CMD ["startWebLogic.sh"]