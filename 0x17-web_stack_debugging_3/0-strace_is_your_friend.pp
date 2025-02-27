# Fixes an Apache 500 error by correcting a typo in a PHP file
# Based on strace analysis showing a file not found error in wp-settings.php

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}