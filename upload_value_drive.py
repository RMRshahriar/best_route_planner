from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()  
gauth.LocalWebserverAuth()         
drive = GoogleDrive(gauth) 

override = 1

fileListA = drive.ListFile({'q': "'1CmBCgSt3YbKZjr7W1guCVT1wOTdpqyGz' in parents and trashed=false"}).GetList()
fileListA[0].SetContentString(str(override))
fileListA[0].Upload()

print('UPLOAD  :::::: COMPLETED')