# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to get the server's hostname
Facter.add('server_hostname') do
  setcode 'hostname'
end

# Configure Nginx with a custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Puppet Managed\nserver {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $server_hostname;
        root   /var/www/html;
        index  index.html index.htm;
    }
}",
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service when the configuration changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
