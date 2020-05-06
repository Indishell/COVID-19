from boxsdk import OAuth2, Client

import webbrowser

auth = OAuth2(
    client_id = 'pjvn8nkk5fweprfzncpyn3dg48mtgj2q',
    client_secret = 'dpIGDwbTq9WYw0VlX3Ri6CtVKGawP4pS',
    access_token = '4moIYaYoIkL47G3eM6Lzwrp6nIOAoBU8',
)
client = Client(auth)
user = client.user().get()

print("Login :  {} and User Name : {} and User Mobile : {}".format(user.login, user.name, user.phone))
folder_id = '111881680762'
fileName = client.folder(folder_id).upload('C:\\Users\\dell\\Desktop\\OOPS.pdf')
print('File "{0}" uploaded to Box with file ID  {1}'.format(fileName.name, fileName.id))

def viewSharedLink(file_id):
    
    url = client.file(file_id).get_shared_link()
    webbrowser.open(url, new=2)

def getSharedLink(file_id):
    url = client.file(file_id).get_shared_link()
    return "The file shared link URL is {0}".format(url)

file_id = '661659166400'
downloadURL = client.file(file_id).get_download_url()
webbrowser.open(downloadURL, new=2)

print('File is currenty being Downloaded...')

print(getSharedLink(file_id))
viewSharedLink(file_id)

