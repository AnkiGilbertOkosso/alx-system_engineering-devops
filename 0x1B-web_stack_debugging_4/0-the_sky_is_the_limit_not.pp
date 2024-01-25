# Fix problem of high traffic of requests

exec {'rep':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'res':
  provider => shell,
  command  => 'sudo service nginx restart',
}