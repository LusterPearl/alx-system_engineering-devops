# Increase request limit in nginx.configuratio
exec { 'increase_request_limit':
  command => 'sed -i "s/worker_connections\s*\(.*\);/worker_connections 4096;/g" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin',
  onlyif  => 'grep -q "worker_connections 4096;" /etc/nginx/nginx.conf',
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['increase_request_limit'],
}
