# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error using strace debugging

# Execute command to fix the issue
exec { 'Fix typo in filename':
  command => 'sudo sed -i "s/.phpp/-php/" /var/www/html/wp-settings.php',
  provider => shell,
}
