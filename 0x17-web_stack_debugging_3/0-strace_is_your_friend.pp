# Fixing Apache returning a 500 error


file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
  require => Exec['fixing error'],
}

exec { 'fixing error':
  command  => '/bin/true',
  path     => '/bin:/usr/bin',
  onlyif   => 'test -f /var/www/html/wp-settings.php && grep -q "phpp" /var/www/html/wp-settings.php',
  provider => shell,
}
