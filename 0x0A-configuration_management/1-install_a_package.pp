# Install flask from pip3

# Requirements:
# 	Install flask
# 	Version must be 2.1.0

service {'flask':
  name    =>  'flask',
  ensure  =>  '2.1.0',
}
