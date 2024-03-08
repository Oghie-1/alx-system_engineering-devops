#fixes bad 'phpp' extensions to 'php'


exec { 'fix-wordpress-phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
  require => File['/var/www/html/wp-settings.php'],
}
