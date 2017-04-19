#!/usr/bin/python3
import urllib.request, json

def download(song, place, person):
	persons = ["none","none","none","none","none"]
	persons[place-1] = person
	url = "https://www.travelthroughmusic.com/merged_videos/C{}_{}_{}_{}_{}_{}.mp4".format(song, persons[0],persons[1],persons[2],persons[3],persons[4])
	file = "{}_{}_{}.mp4".format(song, place, person)
	print("Downloading:", url, "to", file)
	urllib.request.urlretrieve(url, file)

#Taken from https://www.travelthroughmusic.com/data.en.json
compositions = json.loads("""
[
    {
      "title": ["Symphony No.40 in G minor,", "KV. 550, first movement"],
      "composer": "Wolfgang Amadeus Mozart",
      "musicians": [
        ["JKGfroerer","EKoch","TCope","MHeilbrunn","NWright"],
        ["MDugal","GMHoebig","DDesautels","JJonquil"],
        ["SMurray","YAHooker","MThomson","GWolfe","JLockhart"],
        ["CWHamann","LKhaner","LMatiation","JCrow","RSimoneau"],
        ["CJMillard","MHowatt","JScott","TLi","BMJames"]
      ]
    },
    {
      "title": ["Symphony No.5 in C minor,", "op. 67, first movement"],
      "composer": "Ludwig Van Beethoven",
      "musicians": [
        ["JKGfroerer","EKoch","TCope","MHeilbrunn","NWright"],
        ["MDugal","GMHoebig","DDesautels","JJonquil"],
        ["SMurray","YAHooker","MThomson","GWolfe","JLockhart"],
        ["CWHamann","LKhaner","LMatiation","JCrow","RSimoneau"],
        ["CJMillard","MHowatt","JScott","TLi","BMJames"]
      ]
    },
    {
      "title": ["Carmen, Suite No.1,", "Les TorÃ©adors"],
      "composer": "Georges Bizet",
      "musicians": [
        ["JKGfroerer","EKoch","TCope","MHeilbrunn","NWright"],
        ["MDugal","GMHoebig","DDesautels","JJonquil"],
        ["SMurray","YAHooker","MThomson","GWolfe","JLockhart"],
        ["CWHamann","LKhaner","LMatiation","JCrow","RSimoneau"],
        ["CJMillard","MHowatt","JScott","TLi","BMJames"]
      ]
    }
  ]
""");

for compositionIndex, composition in enumerate(compositions):
	for groupIndex, musicianGroup in enumerate(composition["musicians"]):
		for musician in musicianGroup:
			download(compositionIndex+1, groupIndex+1, musician) 

