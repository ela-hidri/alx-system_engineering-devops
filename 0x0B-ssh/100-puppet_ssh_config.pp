#changes to our configuration file 

file_line { 'use_private_key':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => 'true',
}
file_line { 'no_psw':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => 'true',
}
