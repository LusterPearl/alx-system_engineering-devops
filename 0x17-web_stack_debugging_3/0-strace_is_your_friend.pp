# Puppet manifest to fix Apache 500 error using puppet
exec { 'fix-apache':
command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
path => ['/bin', '/usr/bin'],
}
