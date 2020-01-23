#!/bin/sh
echo 'Content-type: text/plain'
echo ''
echo 'Publishing refs/heads/master...'
exec 2>&1
cd /var/repo.git
echo 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
     'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
     'refs/heads/master' | /opt/app/post-receive-hook.sh
ln -sf /opt/app/post-receive-hook.sh hooks/post-receive


echo ''


