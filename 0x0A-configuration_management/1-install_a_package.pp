#This code installs Flask version 2.1.0 using pip3

#Ensure pip3 is installed first
package { 'flask':
  ensure  => '2.1.0',
  provider  => 'pip3',
}