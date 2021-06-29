#!C:\Users\vkadervel\AppData\Local\Programs\Python\Python38\python.exe

import requests
import sys
  
# replace these with configData  
tableauServer = 'http://ec2amaz-hgqugje/'  
tableauUsername = '???'  
workbookView = 'Superstore/Overview'
workbookView2 = 'Superstore/CommissionModel'  
worksheetSuffix = '.csv'  
  
# getting trusted authentication for Tableau  
# see http://onlinehelp.tableau.com/current/server/en-us/trusted_auth.htm  
# for details on how to set up   
# verify the tableau server version 2020.1 or above
  
wgserverURL = tableauServer + 'trusted/'  
r = requests.post(wgserverURL, data={'username': tableauUsername})  
  
# status_code has the response code, text has the ticket string  
if r.status_code == 200:  
    if r.text != '-1':  
        ticketID = r.text  
    else:  
        print("Tableau Server could not issue trusted ticket, for more information see \n")
        # print("ProgramData\Tableau\Tableau Server\data\tabsvc\logs\wgserver\production*.log and \n ...ProgramData\Tableau\")
        # print("Tableau Server\data\tabsvc\logs\vizqlserver\vizql*.log \nAlso check http://onlinehelp.tableau.com/current/server/en-us/trusted_auth_trouble_1return.htm")  
        sys.exit()  
else:  
    print('Could not get trusted ticket with status code',str(r.status_code))  
  
url = wgserverURL + ticketID + '/views/' + workbookView
print(url)  

print("Content-Type: text/html")
print()
print ("""
<html>

<head>
    <title>Basic Embed</title>

    <script type="text/javascript"
	    src="%sjavascripts/api/tableau-2.min.js"></script>
    <script type="text/javascript">
        function initViz() {
            var containerDiv = document.getElementById("vizContainer"),
                url = "%s",
                options = {
                    hideTabs: true,
                    onFirstInteractive: function () {
                        console.log("Run this code when the viz has finished loading.");
                    }
                };

            var viz = new tableau.Viz(containerDiv, url, options);
            // Create a viz object and embed it in the container div.
        }
    </script>
</head>

<body onload="initViz();">
    <div id="vizContainer" style="width:800px; height:700px;"></div>
</body>

</html>
""" %(tableauServer,url))




