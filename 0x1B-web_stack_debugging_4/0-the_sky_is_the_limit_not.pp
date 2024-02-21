# change the nginx file limit
exec { 'Change nginx limit':
  command  => 'sed -i "s/15/4096/g" /etc/default/nginx && service nginx restart',
  provider => shell,
  path     => '/usr/sbin:/usr/bin:/sbin:/bin',
  unless   => 'grep -q "4096" /etc/default/nginx',
}
