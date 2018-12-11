import sanslib, os, requests, random


async def sans(message, client):
    if len(message.attachments)>0 and message.attachments[0]['url'].endswith((".png",".jpg",".jpeg")):
        for attachment in message.attachments:
            imgUrl=message.attachments[0]['url']
    else:
        print("finging past messages")
        async for pastMess in client.logs_from(message.channel,limit=1, reverse=True):
            print(pastMess.content)
            if len(pastMess.attachments)>0 and pastMess.attachments[0]['url'].endswith((".png",".jpg",".jpeg")):
                for attachment in message.attachments:
                    imgUrl=pastMess.attachments[0]['url']            
            
            
            
    if imgUrl.endswith(".png"):
        tempfile="tempin/"+str(random.randint(1,9999999999999))+".png"
    if imgUrl.endswith(".jpg"):
        tempfile="tempin/"+str(random.randint(1,9999999999999))+".jpg"              
    if imgUrl.endswith(".jpeg"):
        tempfile="tempin/"+str(random.randint(1,9999999999999))+".jpeg"
                
                
                
        
    with open(tempfile, 'wb') as f:
        f.write(requests.get(imgUrl).content)
        f.close()
            