# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Replace the default Nginx configuration with our own
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name _;

      location /redirect_me {
        return 301 https://www.example.com/;
      }

      location / {
        add_header 'Content-Type' 'text/html';
        return 200 'Hello World!\n';
      }
    }
  ",
}

# Enable the default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
