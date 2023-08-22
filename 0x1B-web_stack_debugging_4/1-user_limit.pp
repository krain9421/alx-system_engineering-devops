# Fix problem with OS configuration of holberton user

exec { 'fix--OS--config':
  path    => 'usr/bin:/bin',
  command => 'sudo sed -i "s/5/30000/g" /etc/security/limits.conf; sudo sed -i "s/4/10000/g" /etc/security/limits.conf',
  returns => 0,
}
