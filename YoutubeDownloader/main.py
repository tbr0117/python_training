from pytube import YouTube

link = input("Paste Youtube url to download : " )

yt = YouTube(link)  # load video info

videos = yt.streams.all() # streams all formats

video = list(enumerate(videos)) # list out all formats

for i in video:
    print(i)

print("Enter the format option to download")
vf_option =int(input("enter the option : "))
folderPath = input("Enter Folder Localtion :")
fileName = input("Enter file Name: ")

folderPath = folderPath if folderPath else "/"

dn_video = video[vf_option]  # chooose format
dn_video[1].download(folderPath, fileName) # downlaod stream 

print(" Downloaded Successfully")