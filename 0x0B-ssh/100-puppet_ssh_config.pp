# Make changes to a configuration file.
# SSH client configuration must be configured to use
# the private key ~/.ssh/school

# SSH client config must be configured to refuse
# authentication using a password

exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
