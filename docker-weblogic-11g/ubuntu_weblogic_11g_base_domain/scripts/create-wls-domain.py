# Default domain 'base_domain' to be created inside the Docker image for WLS
# ==============================================

# WLS Configuration (will get preferably from env)
# -------------------------------
domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")
admin_port = int(os.environ.get("ADMIN_PORT", "7001"))
admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome01")

# Open default domain template
# ======================
readTemplate("/user01/oracle/weblogic/wlserver_10.3/common/templates/domains/wls.jar")

set('Name', domain_name)
setOption('DomainName', domain_name)

# Configure the Administration Server and SSL port.
# =========================================================
cd('/Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', admin_port)
set('LoginTimeoutMillis', 30000)

# Define the user password for weblogic
# =====================================
cd('/Security/%s/User/weblogic' % domain_name)
cmo.setPassword(admin_pass)

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode','prod')

# Define a WebLogic Cluster
# =========================
cd('/')
create(cluster_name, 'Cluster')

cd('/Clusters/%s' % cluster_name)
cmo.setClusterMessagingMode('unicast')

domain_path = '/user01/oracle/weblogic/user_projects/domains/%s' % domain_name

writeDomain(domain_path)
closeTemplate()

# Exit WLST
# =========
exit()