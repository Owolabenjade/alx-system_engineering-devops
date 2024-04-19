# This manifest kills any process named 'killmenow' using pkill

exec { 'kill-killmenow-process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/bin:/usr/sbin:/bin',
  onlyif      => '/usr/bin/pgrep -f killmenow',
  refreshonly => false,
}

