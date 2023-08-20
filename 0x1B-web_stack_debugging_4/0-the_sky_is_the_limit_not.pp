# Find out why Nginx is getting many failed requests

exec { 'sed':
  path    => 'usr/bin:/bin',
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 30000\"/g" /etc/default/nginx && service nginx restart',
  returns => [0,1],
}

#exec { 'sed2':
#  path    => 'usr/bin:/bin',
#  command => 'sed -i "s/pid \/run\/nginx.pid;/pid \/run\/nginx.pid;\nworker_rlimit_nofile 4096;/g" /etc/nginx/nginx.conf',
#  returns => [0,1],
#}

#exec { 'service':
#  path    => 'usr/bin:/bin',
#  command => 'service nginx restart',
#  returns => [0,1],
#}
