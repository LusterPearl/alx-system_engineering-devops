# Install Nginx package
class { 'nginx':
  ensure => 'installed',
}

# Get the hostname
$hostname = $facts['networking']['hostname']

# Create a custom HTTP response header
file { '/etc/nginx/sites-available/custom_header':
  ensure  => 'file',
  content => "add_header X-Served-By ${hostname};",
}

# Symbolic link to enable the site
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom_header',
}

# Restart Nginx for changes to take effect
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
