# frozen_string_literal: true

require 'puppet'

Puppet::Type.newtype(:network_interface) do
  @doc = 'Manages network interfaces.'

  ensurable

  newparam(:name, namevar: true) do
    desc 'The name of the network interface (e.g., eth0).'
  end

  newproperty(:ipaddress) do
    desc 'The IP address for the interface.'
    validate do |value|
      # Basic validation for IPv4 format
      unless value =~ Resolv::IPv4::Regex
        raise ArgumentError, "Invalid IP address: #{value}"
      end
    end
  end

  newproperty(:netmask) do
    desc 'The netmask for the interface.'
    validate do |value|
      # Basic validation for IPv4 format
      unless value =~ Resolv::IPv4::Regex
        raise ArgumentError, "Invalid netmask: #{value}"
      end
    end
  end

  newproperty(:gateway) do
    desc 'The default gateway for the interface.'
    validate do |value|
      # Basic validation for IPv4 format
      unless value =~ Resolv::IPv4::Regex
        raise ArgumentError, "Invalid gateway: #{value}"
      end
    end
  end

  newproperty(:dns) do
    desc 'The DNS server address.'
    validate do |value|
      # Basic validation for IPv4 format
      unless value =~ Resolv::IPv4::Regex
        raise ArgumentError, "Invalid DNS server: #{value}"
      end
    end
  end
end
