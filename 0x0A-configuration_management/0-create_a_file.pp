#This code creates a file at /tmp/school with specific properties

file { '/tmp/school':
  ensure  => file,
  content  => 'I love Puppet\n',  #the file ends with a new line
  owner  => 'www-data',
  group   => 'www-data',
  mode    => '0744',  #file permission to 0744
}

