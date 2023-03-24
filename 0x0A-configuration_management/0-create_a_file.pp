# Creates a file school in the directory tmp that contains text 'I love puppet'

file { '/tmp/school':
  content => 'I love puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}
