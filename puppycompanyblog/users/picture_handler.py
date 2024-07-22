
import os
from PIL import Image
from flask import url_for,current_app

def add_profile_pic(pic_upload,username):

    filename = pic_upload.filename
    extension = filename.split('.')[-1]
    storage_filename = str(username) + '.' + extension

    #go to my current app root folder and inside static\profile_pic folder store the file storage_filename
    filepath = os.join(current_app.root_path,'static\profile_pic',storage_filename)

    pic = Image.open(pic_upload)
    pic.thumbnail((200,200))
    pic.save(filepath)
    
    return storage_filename