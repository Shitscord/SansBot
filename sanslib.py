from PIL import Image, ImageDraw
import face_recognition

def sans_eye(filename,output):
    image = face_recognition.load_image_file(filename)
    faceFeatures = face_recognition.face_landmarks(image)
    pilImage = Image.fromarray(image)
    if len(faceFeatures)==0:
        return("noface")
    leftFound=False
    rightFound=False
    for face_landmarks in faceFeatures:
        for facial_feature in face_landmarks.keys():           
            if facial_feature == "left_eye":
                leftFound=True
                xTot=0
                for rawCoord in face_landmarks[facial_feature]:
                    xTot=xTot+int(rawCoord[0])
                coordCount=len(face_landmarks[facial_feature])
                lxAverage=xTot//coordCount
            if facial_feature == "right_eye":
                rightFound=True
                xTot=0
                yTot=0
                for rawCoord in face_landmarks[facial_feature]:
                    xTot=xTot+int(rawCoord[0])
                    yTot=yTot+int(rawCoord[1])
        if leftFound and rightFound:
            coordCount=len(face_landmarks[facial_feature])
            rxAverage=xTot//coordCount
            ryAverage=yTot//coordCount
            sansEye = Image.open("sanseye.png")
            xDiff = (rxAverage - lxAverage) * 3
            wpercent = (xDiff / float(sansEye.size[0]))
            hsize = int((float(sansEye.size[1]) * float(wpercent)))
            sansEye = sansEye.resize((xDiff, hsize), Image.ANTIALIAS)
            pilImage.paste(sansEye, (rxAverage-(sansEye.size[0]//2),ryAverage-(sansEye.size[1]//2)), sansEye)
            pilImage.save(output)
            return("success")
    return("noface")