#fix "phpp" in setting.php
exec { 'fix-file':
  command => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
