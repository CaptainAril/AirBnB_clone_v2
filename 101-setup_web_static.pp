# Configures Nginx web server
package { 'nginx':
    ensure  => installed,
}

file { ['/data/', '/data/web_static/', '/data/web_static/releases/', '/data/web_static/shared/', '/data/web_static/releases/test']:
    ensure  => 'directory',
}

file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => '<html>
                    <head>
                    </head>
                    <body>
                        Holberton School!
                    </body>
                </html>',
}

file { '/data/web_static/current/':
    ensure => 'link',
    target => '/data/web_static/releases/test',
}

exec { 'chown -R ubuntu:ubuntu /data/':
    path    => '/usr/bin/:/usr/local/bin/:/bin/'
}

exec { 'config':
    environment => ['data=\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n'],
    command     => 'sed -i "39i $data" /etc/nginx/sites-enabled/default',
    path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}

service { 'nginx':
    ensure  => 'running'
}
