#!/bin/bash


# Setting the name of the mediawiki server
sudo echo "ServerName localhost" > /etc/apache2/httpd.conf

# Reconfiguring the apache.conf file to set the alias of our mediawiki
sudo cp apache.conf /etc/mediawiki/apache.conf

echo "This is the end of configuration"
	

