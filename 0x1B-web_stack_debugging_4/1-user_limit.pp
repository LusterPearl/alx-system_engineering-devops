# raising up limits for user holberton

exec { 'fix limit hard':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  provider => shell
}

# Increase soft file limit holberton user.
exec { 'fix limit soft':
  command   => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  provider  => shell
}
