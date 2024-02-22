# raising up limits for user holberton
# configuration to login to holberton

exec { 'correct-hard':
  command  => 'sudo sed -i \'s/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { 'correct-soft':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { 'change-os-configuration-for-holberton-user':
  command  => 'sysctl -p',
  provider => shell,
}
