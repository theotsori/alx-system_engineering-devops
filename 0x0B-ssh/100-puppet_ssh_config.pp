# Client onfiguration file (w/Puppet)

file { '/home/theodore/.ssh/config':
  ensure => 'file',
  mode   => '0600',
  content => "
Host *
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
"
}
