# Find out why Nginx is getting many failed requests

exec { 'fix--for-nginx':
  path    => 'usr/bin:/bin',
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 30000\"/g" /etc/default/nginx; sudo service nginx restart',
  returns => 0,
}
