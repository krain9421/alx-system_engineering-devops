# Find out why Apache is returning a 500 error.

exec { 'sed':
  path    => 'usr/bin:/bin',
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.pp',
  returns => [0,1],
}
