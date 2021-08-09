from django.shortcuts import render, resolve_url, redirect
#pytube package
from pytube import YouTube
import os
# Create your views here.
url = ''
def yt_download(request):
    return render(request,'yt_main.html')


def yt_downloader(request):
    global url
    url = request.GET.get('url') 
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.streams.filter(file_extension='mp4').all()
    for i in strm_all:
        resolutions.append(i.resolution)

    print("resolution : ",resolutions)
    return render(request,'yt_downloader.html',{'rsl': resolutions})

def yt_download_complete(request,res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    print("diretorio: ",dirs)
    if request.method == "POST":
        YouTube(url).streams.first().download(homedir+ "/Downloads")
        return render(request,"download_complete.html")

def download_complete (request,res):
    print ("res : ",res)
    global url
    return redirect("yt_main.html")