# Create a manifest that kills a process named killmenow.

# Requirements:
# 	Must use the exec resource
# 	Must use pkill

exec {'pkill':
  command =>  'pkill killmenow',
  cwd     =>  '/usr/bin/bash',
}
