# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { 'nginx': }

# Define a custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
            root /var/www/html;
            index index.html index.htm;
        }

        # Custom HTTP response header
        add_header X-Served-By $hostname;
    }
  ",
  notify  => Service['nginx'],
}

# Create a sample HTML file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the default site
file { '/etc/nginx/sites-enabled/000-default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
