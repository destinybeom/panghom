from datetime.date import today
import os

def SocialFileUP(request):
    FILEPATH = '/opt/webapp/gaya/gy01/media/file'
    IMGPATH = '/opt/webapp/gaya/gy01/media/img'

    fList = ['file01','file02','file03']
    iList = ['img01','img02','img03']

    fReturn = []
    iReturn = []

    if request.method == 'POST':
        for f in fList:
            if f in request.FILES:
                fTarget = request.FILES[f]
                fName = fTarget._name

                YMD = today().strftime('%Y/%m/%d')
                FULLPATH = os.path.join(FILEPATH, YMD)

                try:
                    os.makedirs(FULLPATH, mode=0777)
                except:
                    pass

                gFile = open('%s/%s' % (FULLPATH, fName) , 'wb')
                for chunk in fTarget.chunks():
                    gFile.write(chunk)
                gFile.close()
                fReturn.append(YMD+'/'+fName)

        for i in iList:
            if i in request.FILES:
                iTarget = request.FILES[i]
                iName = iTarget._name

                YMD = today().strftime('%Y/%m/%d')
                FULLPATH = os.path.join(IMGPATH, YMD)

                try:
                    os.makedirs(FULLPATH, mode=0777)
                except:
                    pass

                gImg = open('%s/%s' % (FULLPATH, fName) , 'wb')
                for chunk in iTarget.chunks():
                    gImg.write(chunk)
                gImg.close()
                fReturn.append(YMD+'/'+fName)
        return fReturn, iReturn

    else:
        return fReturn, iReturn

def SupportFileUP(request):
    FILEPATH = '/opt/webapp/gaya/gy01/media/file'
    IMGPATH = '/opt/webapp/gaya/gy01/media/img'

    fList = ['file01','file02','file03','file04','file05']
    iList = ['img01','img02','img03','img04','img05']

    fReturn = []
    iReturn = []

    if request.method == 'POST':
        for f in fList:
            if f in request.FILES:
                fTarget = request.FILES[f]
                fName = fTarget._name

                YMD = today().strftime('%Y/%m/%d')
                FULLPATH = os.path.join(FILEPATH, YMD)

                try:
                    os.makedirs(FULLPATH, mode=0777)
                except:
                    pass

                gFile = open('%s/%s' % (FULLPATH, fName) , 'wb')
                for chunk in fTarget.chunks():
                    gFile.write(chunk)
                gFile.close()
                fReturn.append(YMD+'/'+fName)

        for i in iList:
            if i in request.FILES:
                iTarget = request.FILES[i]
                iName = iTarget._name

                YMD = today().strftime('%Y/%m/%d')
                FULLPATH = os.path.join(IMGPATH, YMD)

                try:
                    os.makedirs(FULLPATH, mode=0777)
                except:
                    pass

                gImg = open('%s/%s' % (FULLPATH, fName) , 'wb')
                for chunk in iTarget.chunks():
                    gImg.write(chunk)
                gImg.close()
                iReturn.append(YMD+'/'+iName)
        return fReturn, iReturn

    else:
        return fReturn, iReturn
