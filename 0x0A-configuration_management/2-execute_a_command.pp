# Puppet manifest to kill a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  path        => ['/bin', '/usr/bin'],
}

# Trigger the exec resource only if the process needs to be killed
if $::osfamily == 'Debian' {
  notify { 'Kill killmenow process':
    require => Exec['killmenow'],
  }
}
