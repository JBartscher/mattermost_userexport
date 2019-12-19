# mattermost_userexport

exports all current users of a Mattermost Server into a JSON File which will be placed in the same Directory as the skript

open with cmd or shell or anything that can open and run a python skript. Should work with python 2 and 3. The current API used is the Mattermost v4 API. If you wish to use another API change the API_VERSION variable.
The skript requieres 3 parameters in the following order:

1. You´re Mattermost-Server-URL (e.g: 'https://chat.mattermost.com)
2. You´re Username or Emailadress
3. You´re Password

Example:
```
C:\> python3 'https://chat.mymattermost.com' 'myuser' 'mypassword'
```
It will retrieve max. 2000 Users. If you whish to export more (or less) change the PAGES variable. Iam not aware that Mattermost tracks or even blocks users who try to many connections to the Mattermost API, but iam not intreseted to find it out, so I added a sleep timer (5 Seconds), if you´re in a hurry you can change the timer variable WAIT_SEC to 0.
