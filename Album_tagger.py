import urllib2
import os
import eyeD3
import json
import imghdr
import Image

#tags mp3 music files with images and track info

global artist, which
artist = 'homestuck'        

def unescape(string):
    string = string.replace("\/", "/")
    string = string.replace("\\\\", "\\")
    return string

def imgToTrack(tag, image):
    if imghdr.what(image) != "gif":    
        tag.addImage(3, image, u"cover")
        tag.getImages()[0].mimeType='image/'+(imghdr.what(image))
    else:
        im = Image.open(image)
        if im.mode != "RGB":
            im = im.convert("RGB")
        im.save("imgs/temp.jpg", "JPEG")
        tag.addImage(3, "imgs/temp.jpg", u"cover")
        tag.getImages()[0].mimeType='image/jpeg'
        os.remove("imgs/temp.jpg" % imgs)
    

def tagMusic():
    print "Adding tags..."
    imgs = 'D:\Programming\Python\imgs\omg'

    musics = 'C:/Users/hpp3/Dropbox/Public/remixes'

    i = 0
    for filename in os.listdir(musics):
        if filename[-4:] != ".mp3":
            continue
        name = filename[:-4]+".jpg"

        try:
            int(name[0:2])
            title = name[5:-4]
        except:
            title = name[:-4]
        print "Tagging %s..." % title
        tag = eyeD3.Tag()
        filename = filename.replace(":", "-")
        filename = filename.replace("?", "")
        filename = filename.replace("/", "-")
        tag.link("%s/%s" % (musics, filename))
        tag.setVersion(34)
        tag.removeImages()
        name = filename[:-4]+".jpg"
        
        try:
            i = int(name[0:2])
            if i == 1:
                raise
            imgToTrack(tag, "%s/%s" % (imgs,name))
        except:
            print("Defaulting to album.jpg")
            imgToTrack(tag, "%s/album.jpg" % imgs)
        
        tag.setAlbum("Miscellaneous")
        tag.setArtist("Homestuck")
        tag.setTitle(title)
        tag.setTrackNum((i,None))
        tag.update()

def main():

    tagMusic()
    
main()
