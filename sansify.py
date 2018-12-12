import sanslib, requests, random, constants, time, os, glob

async def sans(message, client):
    print("SansRequest")
    await client.send_typing(message.channel)
    files = glob.glob('tempout/*')
    for f in files:
            os.remove(f)
    files = glob.glob('tempin/*')
    for f in files:
            os.remove(f)
    imageFound=False
    if len(message.attachments) > 0:
        if message.attachments[0]['url'].endswith((".png",".jpg",".jpeg")):
            imgURL=message.attachments[0]['url']
            imageFound=True
            print("SansImageAttached")
    if imageFound==False:
        async for pastMess in client.logs_from(message.channel,limit=100, reverse=True):
            if len(pastMess.attachments) > 0:
                attachURL=str(pastMess.attachments[0]['url'])
                if attachURL.endswith((".png",".jpg",".jpeg")):
                    imgURL=attachURL
                    imageFound=True
                    print("FoundSansImageInChannel")
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
        if sansEye!="noface":
            constants.run_coro(client.send_file(message.channel, tempfileout), client)  
            print("SentBetterSans")
            return(tempfilein, tempfileout)
    constants.run_coro(client.send_message(message.channel, "No face or file found!"), client)
    print("FaceOrImageNotFount")
    return(tempfilein, tempfileout)
            
            