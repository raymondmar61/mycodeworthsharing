import os


def getfilenames(folderpath, fileextension):
    filesnames = os.listdir(folderpath)
    filenameslist = []
    for eachfilenames in filesnames:
        searchhtmlextension = eachfilenames[-5:]
        if searchhtmlextension == fileextension:
            filenameslist.append(eachfilenames)
    return filenameslist


def searchfiles(folderpath, filelist, wordsearch, capital=False):
    if capital is False:
        wordsearchlowercase = wordsearch.lower()
    else:
        wordsearchlowercase = wordsearch
    for eachfilelist in filelist:
        eachfilelist = folderpath + eachfilelist
        with open(eachfilelist, "r") as fileobject:
            linenumber = 1
            mentiontitle = 1
            aline = fileobject.readlines()
            for eachaline in aline:
                if capital is False:
                    eachaline = eachaline.strip().lower()
                else:
                    eachaline = eachaline.strip()
                if wordsearchlowercase in eachaline:
                    if mentiontitle == 1:
                        print("\n" + eachfilelist[-15:])
                        mentiontitle = 0
                    else:
                        pass
                    print(str(linenumber), eachaline)
                linenumber += 1


folderpath = "/media/sf_UbuntuShare2004/bloghtml/"
fileextension = ".html"
getfilenames(folderpath, fileextension)
filelist = getfilenames(folderpath, fileextension)
wordsearch = "Splash"
capitalletters = False
searchfiles(folderpath, filelist, wordsearch, capitalletters)
