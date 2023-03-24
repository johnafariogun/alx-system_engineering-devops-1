# checks if a package flask is installed and if not installs it using pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 list | grep Flask',
}
