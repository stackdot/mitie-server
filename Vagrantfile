Vagrant.configure("2") do |config|
  config.vm.box = "chef/centos-7.0"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP. Make sure this IP doesn't exist on your local network.
  config.vm.network :private_network, ip: "192.168.99.98"

  # forward server ip to 5888
  config.vm.network "forwarded_port", guest: 8888, host: 5888

  # Note: necessary to always run provisioning script, due to fact that
  # Docker service has to be restarted *after*  synced folders are mounted
  # in order to mount those same volumes into a Docker container:
  # https://github.com/docker/docker/issues/4213
  config.vm.provision :shell, 
    privileged: true,
    run: "always",
    path: "provision.sh"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end
end