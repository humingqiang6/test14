# Класс Puppet для настройки сети
class NetworkConfig
  def initialize(interface_name, ip_address, netmask, gateway)
    @interface_name = interface_name
    @ip_address = ip_address
    @netmask = netmask
    @gateway = gateway
  end

  def generate_puppet_manifest
    manifest = <<~MANIFEST
      # Манифест Puppet для настройки сетевого интерфейса #{@interface_name}
      file { '/etc/network/interfaces.d/ifcfg-#{@interface_name}':
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        mode    => '0644',
        content => template('network/ifcfg.erb'),
      }

      # Пример содержимого шаблона ifcfg.erb:
      # DEVICE="#{@interface_name}"
      # BOOTPROTO="static"
      # IPADDR="#{@ip_address}"
      # NETMASK="#{@netmask}"
      # GATEWAY="#{@gateway}"
      # ONBOOT="yes"
    MANIFEST
    return manifest
  end

  def apply_config
    puts "Генерация манифеста Puppet для интерфейса #{@interface_name}..."
    manifest_content = generate_puppet_manifest
    # В реальной реализации здесь будет вызов Puppet apply
    puts manifest_content
    puts "Конфигурация Puppet сгенерирована."
  end
end

# Пример использования
if __FILE__ == $0
  config = NetworkConfig.new('eth0', '192.168.1.10', '255.255.255.0', '192.168.1.1')
  config.apply_config
end