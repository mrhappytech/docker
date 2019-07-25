#!/bin/bash

# do before: $ dos2unix.exe create-managed-server.sh if you are working from Windows!

# Wait for AdminServer to become available 
/user01/oracle/wait-for-admin-server.sh

# Add ManagedServer to the AdminServer only if first execution
if [ ! -f .create-managed.flag ]; then
    wlst.sh -skipWLSModuleScanning /user01/oracle/create-managed-server.py
    touch .create-managed.flag
fi

echo "starting Managed server"

#/user01/oracle/weblogic/user_projects/domains/base_domain/bin/startManagedWebLogic.sh ${MS_NAME:-ManagedServer} http://${ADMIN_HOST}:${ADMIN_PORT}/
${DOMAIN_HOME}/bin/startManagedWebLogic.sh ${MS_NAME:-ManagedServer} http://${ADMIN_HOST}:${ADMIN_PORT}/