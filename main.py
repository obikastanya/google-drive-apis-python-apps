from asyncio import selector_events
from dataclasses import fields
from flask import Flask
from g_drive_service import GoogleDriveService

app=Flask(__name__)



@app.get('/gdrive-files')
def getFileListFromGDrive():
    selected_fields="files(id,name,webViewLink)"
    g_drive_service=GoogleDriveService().build()
    list_file=g_drive_service.files().list(fields=selected_fields).execute()
    return {"files":list_file.get("files")}


if __name__=='__main__':
    app.run(debug=True)