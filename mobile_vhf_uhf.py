#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)

    info( '*** Add links\n')
    s13h27 = {'bw':200,'delay':'5'}
    net.addLink(s13, h27, cls=TCLink , **s13h27)
    h26s13 = {'bw':200,'delay':'5'}
    net.addLink(h26, s13, cls=TCLink , **h26s13)
    s13h25 = {'bw':200,'delay':'5'}
    net.addLink(s13, h25, cls=TCLink , **s13h25)
    s12h24 = {'bw':100,'delay':'20'}
    net.addLink(s12, h24, cls=TCLink , **s12h24)
    h23s12 = {'bw':100,'delay':'20'}
    net.addLink(h23, s12, cls=TCLink , **h23s12)
    s12h22 = {'bw':100,'delay':'20'}
    net.addLink(s12, h22, cls=TCLink , **s12h22)
    h21s11 = {'bw':10,'delay':'33'}
    net.addLink(h21, s11, cls=TCLink , **h21s11)
    s11h20 = {'bw':10,'delay':'33'}
    net.addLink(s11, h20, cls=TCLink , **s11h20)
    h19s11 = {'bw':10,'delay':'33'}
    net.addLink(h19, s11, cls=TCLink , **h19s11)
    h18s10 = {'bw':0.12,'delay':'208'}
    net.addLink(h18, s10, cls=TCLink , **h18s10)
    h17s10 = {'bw':0.12,'delay':'208'}
    net.addLink(h17, s10, cls=TCLink , **h17s10)
    s10h16 = {'bw':0.12,'delay':'208'}
    net.addLink(s10, h16, cls=TCLink , **s10h16)
    h15s9 = {'bw':0.04,'delay':'208'}
    net.addLink(h15, s9, cls=TCLink , **h15s9)
    s9h14 = {'bw':0.04,'delay':'208'}
    net.addLink(s9, h14, cls=TCLink , **s9h14)
    h13s9 = {'bw':0.04,'delay':'208'}
    net.addLink(h13, s9, cls=TCLink , **h13s9)
    h12s8 = {'bw':0.02,'delay':'208'}
    net.addLink(h12, s8, cls=TCLink , **h12s8)
    s8h11 = {'bw':0.02,'delay':'208'}
    net.addLink(s8, h11, cls=TCLink , **s8h11)
    h10s8 = {'bw':0.02,'delay':'208'}
    net.addLink(h10, s8, cls=TCLink , **h10s8)
    s7h9 = {'bw':0.04,'delay':'202'}
    net.addLink(s7, h9, cls=TCLink , **s7h9)
    h8s7 = {'bw':0.04,'delay':'202'}
    net.addLink(h8, s7, cls=TCLink , **h8s7)
    s7h7 = {'bw':0.04,'delay':'202'}
    net.addLink(s7, h7, cls=TCLink , **s7h7)
    h6s6 = {'bw':0.04,'delay':'202'}
    net.addLink(h6, s6, cls=TCLink , **h6s6)
    s6h5 = {'bw':0.04,'delay':'202'}
    net.addLink(s6, h5, cls=TCLink , **s6h5)
    h4s6 = {'bw':0.04,'delay':'202'}
    net.addLink(h4, s6, cls=TCLink , **h4s6)
    h1s5 = {'bw':0.04,'delay':'202'}
    net.addLink(h1, s5, cls=TCLink , **h1s5)
    s5h2 = {'bw':0.04,'delay':'202'}
    net.addLink(s5, h2, cls=TCLink , **s5h2)
    h3s5 = {'bw':0.04,'delay':'202'}
    net.addLink(h3, s5, cls=TCLink , **h3s5)
    s5s2 = {'bw':0.2,'delay':'202'}
    net.addLink(s5, s2, cls=TCLink , **s5s2)
    s2s6 = {'bw':0.2,'delay':'202'}
    net.addLink(s2, s6, cls=TCLink , **s2s6)
    s2s7 = {'bw':0.2,'delay':'202'}
    net.addLink(s2, s7, cls=TCLink , **s2s7)
    s1s2 = {'bw':1,'delay':'202'}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    s3s1 = {'bw':1,'delay':'208'}
    net.addLink(s3, s1, cls=TCLink , **s3s1)
    s1s4 = {'bw':1000,'delay':'33'}
    net.addLink(s1, s4, cls=TCLink , **s1s4)
    s8s3 = {'bw':0.1,'delay':'208'}
    net.addLink(s8, s3, cls=TCLink , **s8s3)
    s3s9 = {'bw':0.2,'delay':'208'}
    net.addLink(s3, s9, cls=TCLink , **s3s9)
    s3s10 = {'bw':0.4,'delay':'208'}
    net.addLink(s3, s10, cls=TCLink , **s3s10)
    s4s13 = {'bw':600,'delay':'5'}
    net.addLink(s4, s13, cls=TCLink , **s4s13)
    s12s4 = {'bw':300,'delay':'20'}
    net.addLink(s12, s4, cls=TCLink , **s12s4)
    s4s11 = {'bw':30,'delay':'33'}
    net.addLink(s4, s11, cls=TCLink , **s4s11)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s13').start([c0])
    net.get('s4').start([c0])
    net.get('s11').start([c0])
    net.get('s9').start([c0])
    net.get('s8').start([c0])
    net.get('s2').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s3').start([c0])
    net.get('s12').start([c0])
    net.get('s7').start([c0])
    net.get('s10').start([c0])
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()