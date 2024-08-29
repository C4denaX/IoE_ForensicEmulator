from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, Host
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_ioe_topology():
    # Inicializar la red
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)

    # Añadir controlador
    net.addController('c0')

    # Crear nodos de la Topología OT
    gw_ics = net.addHost('gw_ics', ip='172.17.0.1/24')
    modbus1 = net.addHost('modbus1', ip='172.17.0.2/24')
    opcua1 = net.addHost('opcua1', ip='172.17.0.3/24')
    s7comm1 = net.addHost('s7comm1', ip='172.17.0.4/24')

    # Crear nodos de la Topología IoT
    mqtt1 = net.addHost('mqtt1', ip='172.18.0.1/24')
    matter1 = net.addHost('matter1', ip='172.18.0.2/24')
    ext_service = net.addHost('ext_service', ip='172.18.0.3/24')

    # Crear nodos de la Topología IT
    http_client1 = net.addHost('http_client1', ip='172.19.0.1/24')

    # Crear switches para cada topología
    sw_ot = net.addSwitch('sw_ot')
    sw_iot = net.addSwitch('sw_iot')
    sw_it = net.addSwitch('sw_it')

    # Conectar los nodos a sus respectivos switches
    net.addLink(gw_ics, sw_ot)
    net.addLink(modbus1, sw_ot)
    net.addLink(opcua1, sw_ot)
    net.addLink(s7comm1, sw_ot)

    net.addLink(mqtt1, sw_iot)
    net.addLink(matter1, sw_iot)
    net.addLink(ext_service, sw_iot)

    net.addLink(http_client1, sw_it)

    # Interconectar switches para simular la red IoE
    net.addLink(sw_ot, sw_iot)
    net.addLink(sw_iot, sw_it)

    # Iniciar la red
    net.start()

    # Lanzar la CLI de Mininet para interacción
    CLI(net)

    # Detener la red
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_ioe_topology()
