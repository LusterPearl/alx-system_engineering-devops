# Puppet manifest to configure SSH client

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# SSH client configuration file\n\nHost *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
