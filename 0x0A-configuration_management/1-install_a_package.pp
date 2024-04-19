# This manifest installs Flask version 2.1.0 using pip3

# Ensure pip3 is installed first
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep Flask==2.1.0',
  require => Package['python3-pip'],  # Ensures pip3 is installed before attempting to install Flask
}

