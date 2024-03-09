# Puppet manifest for a configuration file in the server
# execute 'apt-get update'
exec { 'apt-update':
	command => '/usr/bin/apt-get update',
}

# install nginx package
package { 'nginx':
	require => Exec['apt-update'],
	ensure  => installed,
}

# creating directories 
$static_dirs = [
	'/data',                      '/data/web_static',  
	'/data/web_static/releases',  '/data/web_static/shared',
	'/data/web_static/releases/test',
]

file { $static_dirs:
	ensure => directory,
	owner  => 'ubuntu',
	group  => 'ubuntu',
}

# hello world HTML file
file { '/var/www/htmlindex.html':
	ensure  => file,
	content => 'Hello World!',
	require => Package['nginx'],
}

# content of the test file
file { '/data/web_static/releases/test/index.html':
	ensure  => file,
	content => '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t\
	Holberton School\n\t</body>\n</html>',
	require => File[$static_dirs],
}

# create a sympbolic link
file { '/data/web_static/current':
	ensure  => link,
	target  => '/data/web_static/releases/test/'
	require => File[$static_dirs],
}

# replacing lines for the redirection
exec { 'Redirection':
	provider => shell,
	command  => 'sudo sed -i "s#server_name _;#server_name _;\n        location /redirect_me {\n                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n        }#" /etc/nginx/sites-available/default ; sudo service nginx restart',
}

# adding a new location
exec { 'Location':
	provider => shell,
	command  => 'text="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" ; sudo sed -i "/^\tlocation \/ {/i\\ \t$text" /etc/nginx/sites-available/default ; sudo service nginx restart',
}

