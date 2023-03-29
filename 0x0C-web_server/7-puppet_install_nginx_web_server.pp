# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80 and return "Hello World!"
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => '
    server {
      listen 80;
      location / {
        return 200 "Hello World!";
      }
    }
  ',
  notify => Service['nginx'],
}

# Enable site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Configure redirection
file { '/etc/nginx/sites-available/redirect':
  ensure => file,
  content => '
    server {
      listen 80;
      location /redirect_me {
        return 301 /;
      }
    }
  ',
  notify => Service['nginx'],
}

# Enable redirection configuration
file { '/etc/nginx/sites-enabled/redirect':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect',
  notify => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
}
