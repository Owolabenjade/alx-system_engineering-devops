# Puppet manifest to install and configure Nginx with a 'Hello World!' page and a redirection

class nginx_setup {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Template content for Nginx site configuration
define nginx::config {
  file { "/etc/nginx/sites-enabled/${name}":
    ensure  => link,
    target  => "/etc/nginx/sites-available/${name}",
    require => File["/etc/nginx/sites-available/${name}"],
    notify  => Service['nginx'],
  }
}

nginx_setup { 'default': }

# Define the template separately or inline here using 'content'
file { 'nginx/default.erb':
  content => '
server {
  listen 80;
  server_name _;

  location /redirect_me {
    return 301 https://www.example.com;
  }

  location / {
    root /var/www/html;
    index index.html;
  }

  error_page 404 /404.html;
  location = /404.html {
    root /var/www/html;
    internal;
  }
}',
  before => Nginx::Config['default'],
}

nginx::config { 'default': }

