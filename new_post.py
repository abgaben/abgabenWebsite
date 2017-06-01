import datetime
import os

print("=== NEW JEKYLL-POST TOOL ===")
today = datetime.datetime.now()
year = str(today.year)
month = str(today.month).zfill(2)
day = str(today.day).zfill(2)
print("Time: "+today.strftime("%Y-%m-%d %H:%M:%S"))
title = input("Bitte den Titel des neuen Posts eingeben: ")
fileTitle = title.lower().replace(" ","-").replace("/","").replace("*","")
category = input("Bitte die Kategorie des neuen Posts eingeben: ")

filename = "./_posts/"+year+"-"+month+"-"+day+"-"+category.lower()+"-"+fileTitle+".md"

print("\nDanke, erstelle .md datei")
post = open(filename,"w")
post.write("---\n"+
           "layout: post\n"+
           "title: '"+title+"'\n"+
           "date: "+today.strftime("%Y-%m-%d %H:%M:%S")+"\n"+
           "category: "+category+"\n"+
           "tags: [SS-17, "+category+"]\n"+
           "---\n\n")
post.close()
print("Done, file created\nNow opening the best Editor")
os.system("emacsclient --alternate-editor=\"\" "+filename)
print("Done, finished")
