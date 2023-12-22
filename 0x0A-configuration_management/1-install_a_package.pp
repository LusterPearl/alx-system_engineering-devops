# Puppet manifest to install Flask package using pip3
# Define the package resource
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install-pip3'],
}

# Ensure pip3 is installed (use Exec as a workaround for simplicity)
exec { 'install-pip3':
  command => 'apt-get install -y python3-pip',
  path    => '/usr/bin',
  creates => '/usr/bin/pip3,
}
