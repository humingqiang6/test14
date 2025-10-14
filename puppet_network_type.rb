# frozen_string_literal: true

require 'puppet'

Puppet::Type.newtype(:network_config) do
  @doc = 'Custom Puppet type for managing basic network configuration.'

  ensurable

  newparam(:name, namevar: true) do
    desc 'The name of the network interface, e.g., eth0.'
    validate do |value|
      raise ArgumentError, "Invalid interface name: #{value}" unless value =~ /^[a-zA-Z0-9_.:-]+$/
    end
  end

  newproperty(:ipaddress) do
    desc 'The IP address for the interface.'
    validate do |value|
      raise ArgumentError, "Invalid IP address: #{value}" unless value =~ /^(\d{1,3}\.){3}\d{1,3}$/
    end
  end

  newproperty(:netmask) do
    desc 'The netmask for the interface.'
    validate do |value|
      raise ArgumentError, "Invalid netmask: #{value}" unless value =~ /^(\d{1,3}\.){3}\d{1,3}$/
    end
  end

  newproperty(:gateway) do
    desc 'The default gateway for the interface.'
    validate do |value|
      raise ArgumentError, "Invalid gateway: #{value}" unless value =~ /^(\d{1,3}\.){3}\d{1,3}$/
    end
  end

end