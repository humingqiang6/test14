# Класс Puppet для настройки сети
class network_config {
  # Параметры для настройки интерфейса
  $interface_name = 'eth0' # Имя интерфейса
  $ip_address = '192.168.1.10' # IP-адрес
  $netmask = '255.255.255.0' # Маска подсети
  $gateway = '192.168.1.1' # Шлюз по умолчанию

  # Ресурс для управления сетевым интерфейсом
  # В реальной реализации Puppet можно использовать модули вендоров (например, puppetlabs-network)
  # или ресурсы типа `file` для редактирования файлов конфигурации ОС.
  file { "/etc/network/interfaces.d/${interface_name}":
    ensure  => file,
    content => "
# Конфигурация интерфейса, управляемая Puppet
auto ${interface_name}
iface ${interface_name} inet static
    address ${ip_address}
    netmask ${netmask}
    gateway ${gateway}
",
    require => Package['linux-base'], # Зависимость от базового пакета
  }

  # Пример ресурса для управления маршрутом по умолчанию
  exec { "set_default_route_${interface_name}":
    command     => "/sbin/ip route add default via ${gateway} dev ${interface_name}",
    # Условие для выполнения команды только если маршрут отсутствует
    # В реальной практике требует более тщательной проверки
    onlyif      => "/bin/echo 'Checking route...'",
    subscribe   => File["/etc/network/interfaces.d/${interface_name}"], # Выполнять при изменении файла
    require     => File["/etc/network/interfaces.d/${interface_name}"],
  }
}