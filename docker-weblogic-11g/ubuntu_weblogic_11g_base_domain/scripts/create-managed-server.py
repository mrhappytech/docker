# Managed server to be created inside the Docker image for WLS
# ==============================================
import os
import socket
import string

hostname = socket.gethostname()

# WLS Configuration (will get preferably from env)
# -------------------------------

# AdminServer details
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")
admin_username = os.environ.get('ADMIN_USERNAME', 'weblogic')
admin_password = os.environ.get('ADMIN_PASSWORD', 'welcome01')
admin_host     = os.environ.get('ADMIN_HOST', 'wlsadmin')
admin_port     = os.environ.get('ADMIN_PORT', '7001')

# ManagedServer details
msinternal = socket.gethostbyname(hostname)
msname = os.environ.get('MS_NAME', 'ManagedServer')
mshost = os.environ.get('MS_HOST', msinternal)
msport = os.environ.get('MS_PORT', '7101')
memargs = os.environ.get('MANAGED_MEM_ARGS', '-Xms1024m -Xmx1024m -XX:MaxPermSize=512m')

# This is obsolete - params are taken from Docker run command
#managed1_name = os.environ.get("MANAGED_1_NAME", "managed1")
#managed1_port = int(os.environ.get("MANAGED_1_PORT", "7101"))
#managed2_name = os.environ.get("MANAGED_2_NAME", "managed2")
#managed2_port = int(os.environ.get("MANAGED_2_PORT", "7102"))
#managed_memory_args = os.environ.get("MANAGED_MEM_ARGS", "")
#managed_logging = os.environ.get("MANAGED_LOGGING", "") #-Dweblogic.log.Log4jLoggingEnabled=true

print 'Configuring managed server:'
print 'admin_host: '+admin_host
print 'hostname: '+hostname
print 'msinternal: '+msinternal

print 'msname: '+msname
print 'mshost: '+mshost
print 'msport: '+msport
print 'memargs: '+memargs

# Connect to the AdminServer
# ==========================
connect(admin_username, admin_password, url='t3://' + admin_host + ':' + admin_port, adminServerName='AdminServer')

# Create a ManagedServer
# ======================
edit()
startEdit(waitTimeInMillis=-1, exclusive="true")

cd('/')
cmo.createServer(msname)

cd('/Servers/' + msname)
cmo.setCluster(getMBean('/Clusters/%s' % cluster_name))

# Default Channel for ManagedServer
# ---------------------------------
cmo.setListenAddress(msinternal)
cmo.setListenPort(int(msport))
cmo.setListenPortEnabled(true)
cmo.setExternalDNSName(mshost)

# Disable SSL for this ManagedServer
# ----------------------------------
cd('/Servers/%s/SSL/%s' % (msname, msname))
cmo.setEnabled(false)

# Custom Startup Parameters because NodeManager writes wrong AdminURL in startup.properties
# -----------------------------------------------------------------------------------------
cd('/Servers/%s/ServerStart/%s' % (msname, msname))
arguments = '-Djava.security.egd=file:/dev/./urandom -Dweblogic.Name=%s -Dweblogic.management.server=http://%s:%s %s' % (msname, admin_host, admin_port, memargs)
cmo.setArguments(arguments)

save()
activate(block="true")

# Exit
# =========
exit()