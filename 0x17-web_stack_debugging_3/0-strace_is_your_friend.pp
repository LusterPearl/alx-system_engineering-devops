# fix Apache 500 error and corrects a typo in wordpress settings
exec { 'fix-apache':
command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
path => ['/bin', '/usr/bin'],
}
