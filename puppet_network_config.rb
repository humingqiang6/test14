# Класс Puppet для настройки сети
class network_config {
  # Параметры по умолчанию
  $interface = 'eth0',
  $ip_address = '192.168.1.100',
  $netmask = '255.255.255.0',
  $gateway = '192.168.1.1',
  $dns_servers = ['8.8.8.8', '8.8.4.4']
> {
  # Управление файлом интерфейса (упрощённо)
  file { "/etc/network/interfaces.d/${interface}":
    ensure  => file,
    content => "
# Конфигурация интерфейса ${interface}
auto ${interface}
iface ${interface} inet static
    address ${ip_address}
    netmask ${netmask}
    gateway ${gateway}
    dns-nameservers ${join($dns_servers, ' ')}
",
    require => Package['linux-base'],
  }

  # Перезапуск службы сети для применения изменений
  service { 'networking':
    enable => true,
    ensure => running,
    subscribe => File["/etc/network/interfaces.d/${interface}"], # Перезапуск при изменении файла
  }
}