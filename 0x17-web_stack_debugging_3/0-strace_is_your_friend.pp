# Fixing Apache returning a 500 error


exec { 'fixing error':
	provider => 'shell',
	command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
	path => '/bin:/usr/bin',
	onlyif => 'test -f /var/www/html/wp-settings.php',
}
