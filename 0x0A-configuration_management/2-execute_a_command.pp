# This code kills any process && works together with the 'killmenow' file already provided using pkill

exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  provider  => 'shell',
  returns ==> [0, 1],
}

