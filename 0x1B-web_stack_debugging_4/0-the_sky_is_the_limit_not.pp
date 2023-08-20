# Find out why Nginx is getting many failed requests

exec { 'sed':
  path    => 'usr/bin:/bin',
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g" /etc/default/nginx',
  returns => [0,1],
}

exec { 'service':
  path    => 'usr/bin:/bin',
  command => 'service nginx restart',
  returns => [0,1],
}
