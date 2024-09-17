""" 
Fix permissions for WordPress files and directories 
"""

# Define a file resource to set permissions for WordPress
file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Ensure Apache can read the WordPress files
file { '/var/www/html/wordpress/wp-config.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Restart Apache to apply changes
exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => File['/var/www/html/wordpress/wp-config.php'],
}
