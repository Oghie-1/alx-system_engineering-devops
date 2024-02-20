#  fixes typo ext error to php in the wp-file


exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/bin',
}
