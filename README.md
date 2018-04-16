# mattermost_userexport

exports all users into a JSON File whic will be placed in the same Directory as the skript

open with cmd or shell or anything that can open run a python skript. Should work with python 2 and 3. The current API used is the Mattermost v4 API.
The skript requieres 3 parameters in the following order: 
1. You´re Mattermost-Server-URL (e.g: 'https://chat.mattermost.com)
2. You´re Username or Emailadress
3. You´re Password

Example:
```
C:\> python3 'https://chat.mattermost.com' 'myuser' 'mypassword'
```
It will retrieve max. 2000 Users. If you whish to export more (or less) change the PAGES variable. Iam not aware that Mattermost tracks or even blocks Users who try to many connections to the Mattermost API, but iam not intreseted to find it out, so I added a sleep timer (5 Seconds), if you´re in a hurry you can change the wait timer Variable WAIT_SEC to 0.
