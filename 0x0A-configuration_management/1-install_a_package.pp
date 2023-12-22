# Puppet manifest to install Flask package using pip3
# Define the package resource
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'echo_flask_version':
  command => '/bin/echo "flask --version" | /usr/bin/python3',
  path    => ['/usr/bin', '/bin'],
  require => Package['Flask'],
}
