#!/bin/sh
echo 'Content-type: text/plain'
echo ''

/opt/app/post-receive-hook.sh
ln -sf /opt/app/post-receive-hook.sh /var/repo.git/hooks/post-receive

echo "Here is your grain's public id:"
/opt/app/sandstorm/bin/getPublicId "${HTTP_X_SANDSTORM_SESSION_ID}" 2>&1

echo ''


