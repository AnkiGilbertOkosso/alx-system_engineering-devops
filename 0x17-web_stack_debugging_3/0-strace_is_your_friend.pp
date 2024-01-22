# Fix 500 error when a GET HTTP method is requested to an Apache web server

exec {'repl':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
