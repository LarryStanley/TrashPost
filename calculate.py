import json
import urllib2
import sys

with open("trashData.json") as jsonFile:
    allData = json.load(jsonFile)
    likeCount = 0
    commentCount = 0
    for post in allData:
        likeCount += int(post['likes']['summary']['total_count'])
        commentCount += int(post['comments']['summary']['total_count'])
    print likeCount
    print commentCount