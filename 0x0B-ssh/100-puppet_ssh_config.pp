# Client onfiguration file (w/Puppet)

file { "/root/.ssh":
  ensure => "directory",
  mode   => "0700",
}

file { '/root/.ssh/school':
  ensure => 'file',
  source => '/home/theodore/.ssh/school',
  mode   => '0600',
}
