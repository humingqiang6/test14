# Класс Puppet для настройки сети
class NetworkConfig
  # Конструктор класса
  def initialize(interface_name, ip_address, netmask, gateway)
    @interface_name = interface_name
    @ip_address = ip_address
    @netmask = netmask
    @gateway = gateway
  end

  # Метод для генерации конфигурации интерфейса (упрощённый пример)
  def generate_interface_config
    config = {
      name: @interface_name,
      ip: @ip_address,
      netmask: @netmask,
      gateway: @gateway
    }
    return config
  end

  # Метод для применения конфигурации (заглушка)
  def apply_config
    puts "Применение конфигурации для интерфейса #{@interface_name}:"
    puts "  IP: #{@ip_address}"
    puts "  Маска: #{@netmask}"
    puts "  Шлюз: #{@gateway}"
    # Здесь будет логика для реального изменения настроек сети
    puts "Конфигурация применена (симуляция)."
  end
end

# Пример использования
if __FILE__ == $0
  # Создание экземпляра класса
  my_network = NetworkConfig.new("eth0", "192.168.1.100", "255.255.255.0", "192.168.1.1")
  # Генерация и вывод конфигурации
  puts my_network.generate_interface_config
  # Применение конфигурации
  my_network.apply_config
end