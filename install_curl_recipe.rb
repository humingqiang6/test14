# Recipe to install the 'curl' package

# Use the 'package' resource to manage the installation of the 'curl' package.
# The 'package' resource will use the system's default package manager (e.g., apt, yum).
package 'curl' do
  # The 'package_name' property specifies the name of the package to install.
  # In this case, it's 'curl'.
  package_name 'curl'

  # The 'action' property defines what action to take on the resource.
  # Here, we set it to ':install' to ensure the package is installed.
  action :install
end
