# elec5517-assignment1
Our code for our assignment can be found at https://github.com/nicolezyi/elec5517-assignment1.git 

------------------------------------------------------
Setup environment for all tasks: 

There are two options to implement our efficient QoS system. 

Option 1 - Docker image 
1. Download our image, and run our image. This image includes ryu controller, mininet and ofsoftswitch13 vSwitch. 
CLI to download it. 
```
sudo docker pull nicoleyi/ryu-qos-controller
```
2. Use the following command to run the image to make sure you have x11 forwording turn on 
```
docker run -it --privileged -e DISPLAY=$DISPLAY \
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v /lib/modules:/lib/modules \
             nicoleyi/ryu-qos-controller
```

Option 2 - Install Ryu, mininet and ofsoftswitch13 vSwitch manually. 

# CLI to install Ryu in Debian family Linux distro. The rest of instruction is based on Debian family 
$ sudo apt-get install git python-dev python-setuptools python-pip
$ git clone https://github.com/osrg/ryu.git
$ cd ryu
$ sudo pip install .

# CLI to install mininet 
```
sudo apt-get install mininet
```

# Instruction to install ofsoftswitch13 vSwitch. 
https://github.com/CPqD/ofsoftswitch13 


----------------------------------------------------------
Task 1
custom_topo.py is to invoke mininet and setup custom tree topology (3 layer depth and fan out 3 topology) for task 1 and tak 2.
injectRules.sh is used to inject the QoS rules and Meter table for all 13 Switches.

#CLI to turn on controller, vSwitch, start mininet with custom topology and inject the rules
```
ryu-manager ryu.app.rest_qos ryu.app.qos_simple_switch_13
sudo python custom_topo.py
sh injectRules.sh
```


------------------------------------------------------------
Task 2
In task 2, in additon to the QoS implementation, we also implement the traffic monitoring for this QoS network. 

We also include a sample test results here: port_statistics_sample.txt
```
ryu-manager ryu.app.rest_qos ryu.app.qos_simple_switch_13 traffic_monitor_all.py
sudo python custom_topo.py
sh injectRules.sh
```

------------------------------------------------------------
Task 3
Mobile_vhf_uhf.py is the Python script for task three. 

Run "sudo python task.py" after login to Mininet to create the topology with specified configuration.

