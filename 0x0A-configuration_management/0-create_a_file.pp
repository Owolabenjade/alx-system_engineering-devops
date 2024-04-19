# This manifest creates a file at /tmp/school with specific properties

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet\n',  # Ensures the file ends with a new line
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',  # Sets the file permission to 0744
}

