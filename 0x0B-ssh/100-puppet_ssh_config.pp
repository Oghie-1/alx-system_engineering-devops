# Puppet Manifest to configure SSH client

file_line { 'Turn off passwd auth':
    path => './2-ssh_config',  # path to the ssh server config file
    line => 'PasswordAuthentication no', # Configuring to refuse password authentication 
    ensure => present,
}

file_line {
    path => './2-ssh_config', # path to SSH client config
    line => 'IdentifyFile ~/.ssh/school', # Configuring the identity file
    ensure => present
}