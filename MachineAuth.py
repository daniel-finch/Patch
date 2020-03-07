import requests
from requests_ntlm3 import HttpNtlmAuth

#Ask for user information
domain = raw_input("Enter Domain Name: ")
userName = raw_input("Enter Username: ")
password = raw_input("Enter Password: ")
serverName = raw_input("Enter server URL: ")
serverPort = raw_input("Enter Server Port: ")

#Format to correct domain name (With two backslash)
domainUser = domain + r'\\' + userName

#Send request to HTTPs URL for authentication
requests.post('https://{0}:{1}/st/console/api/v1.0/machinegroups'.format(serverName, serverPort), auth=HttpNtlmAuth(domainUser, password))

#Test user authentication

authTest = requests.get('https://'+serverName+':'+serverPort+'/st/console/api/v1.0/machinegroups')

print ("Machine status:" +authTest)


#End of program
