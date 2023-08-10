# Find out why Apache is returning a 500 error.

exec { 'sed':
	path	=> 'usr/bin:/bin'
