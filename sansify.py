import sanslib, requests, random, constants, time, os, glob, discord

async def sans(message, client):
    print("SansRequest")
    files = glob.glob('tempout/*')
    for f in files:
            os.remove(f)
    files = glob.glob('tempin/*')
    for f in files:
            os.remove(f)
    imageFound=False
    if message.attachments:
        print(message.attachments)
        if message.attachments[0].url.endswith((".png",".jpg",".jpeg")):
            imgURL=message.attachments[0].url
            imageFound=True
            print("SansImageAttached")
    if imageFound==False:
        async for pastMess in message.channel.history(limit=50, oldest_first=False):
            if len(pastMess.attachments) > 0:
                attachURL=str(pastMess.attachments[0].url)
                if attachURL.endswith((".png",".jpg",".jpeg")):
                    imgURL=attachURL
                    imageFound=True
                    print("FoundSansImageInChannel")
                    break
    if imageFound:    
        imageName=str(message.channel.id)+str(random.randint(1,99999999))
        if imgURL.endswith(".png"):
            fileExt=".png"
        if imgURL.endswith(".jpg"):
            fileExt=".jpg"  
        if imgURL.endswith(".jpeg"):
            fileExt=".jpeg"
        tempfilein="tempin/"+imageName+fileExt
        tempfileout="tempout/"+imageName+fileExt
        with open(tempfilein, 'wb') as f:
            f.write(requests.get(imgURL).content)
            f.close()
        print("SavedSansImage")
        time.sleep(.1)
        sansEye=sanslib.sans_eye(tempfilein, tempfileout)
        print(sansEye)
        if sansEye!="noface":
            constants.run_coro(message.channel.send(file=discord.File(tempfileout)), client)  
            print("SentBetterSans")
            return(tempfilein, tempfileout)
    constants.run_coro(message.channel.send("No face or file found!"), client)
    print("FaceOrImageNotFount")
            
            