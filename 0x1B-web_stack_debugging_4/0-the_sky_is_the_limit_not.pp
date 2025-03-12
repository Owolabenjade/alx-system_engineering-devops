# Fixes Nginx to handle high loads of concurrent requests
# Increases the ULIMIT and adjusts Nginx worker settings

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sed -i "s/worker_processes 4;/worker_processes auto;/g" /etc/nginx/nginx.conf && sed -i "/worker_connections/c\\worker_connections 4096;" /etc/nginx/nginx.conf && service nginx restart',
  path    => '/usr/local/bin/:/bin/:/usr/bin/'
}