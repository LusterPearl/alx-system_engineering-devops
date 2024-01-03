# Setup New Ubuntu server


exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}
package {'nginx':
  ensure => 'installed',
}

exec {'Hello_world':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
  require  => Package['nginx'],
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.github.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
