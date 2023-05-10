# Using strace to determine the cause of the 500 error returned by Apache
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
