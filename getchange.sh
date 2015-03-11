#!/bin/bash
git fetch origin
git merge origin/master
sudo /etc/init.d/apache2 restart