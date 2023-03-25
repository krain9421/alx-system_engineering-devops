# Create a manifest that kills a process named killmenow.

# Requirements:
# 	Must use the exec resource
# 	Must use pkill

exec {'killmenow':
  command =>  'pkill killmenow',
  path    =>  '/usr/bin',
}
