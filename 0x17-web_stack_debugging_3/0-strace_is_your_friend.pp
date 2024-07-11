#0-strace_is_your_friend.pp
#Fixes a WordPress 500 error by correcting a filename typo

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
