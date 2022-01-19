import requests
import sys
import jwt
import datetime
import uuid

#prerequisite values
connectedAppClientId = ""
connectedAppSecretId = ""
connectedAppSecretKey = ""

#email address for TOL; username for Tableau Server
username= ""

#TOL or Tableau server name. SSL is highly recommeded
tableauservername =""

#JS API3.0 library
js_api='tableau.embedding.3.0.0.min.js'

#public facing url from TOL/ Tableau server 
viz_dash_url = tableauservername + ""


token = jwt.encode(
{
    'iss': connectedAppClientId,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
    'jti': str(uuid.uuid4()),
    'aud': 'tableau',
    'sub': username,
    'scp': ['tableau:views:embed']
    },
    connectedAppSecretKey,
    algorithm = 'HS256',
    headers = {
    'kid': connectedAppSecretId,
    'iss': connectedAppClientId
    }
)
print(token)

print()
print ("""
<!DOCTYPE html>
<html>

<head>
    <title>Welcome to APJ ConnectedApp Demo</title>
    <script type="module" src="https://embedding.tableauusercontent.com/tableau.embedding.3.0.0.min.js"></script>

    <body>
        <tableau-viz id="tableauViz"
        src='%s'
        token="%s"
        toolbar='hidden'
        iframeSizedToWindow='true'
        >
        </tableau-viz>
    </body>
</html>
""" %(viz_dash_url,token))
