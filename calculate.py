import json
import urllib2
import sys

with open("trashData.json") as jsonFile:
    allData = json.load(jsonFile)
    likeCount = 0
    commentCount = 0
    timeCount = []
    dateCount = []
    for post in allData:
        likeCount += int(post['likes']['summary']['total_count'])
        commentCount += int(post['comments']['summary']['total_count'])
        #about created time
        createdTime = post['created_time']
        createdTime = createdTime.split("T")
        if str(createdTime[0]) in dateCount:
            dateCount[str(createdTime[0])] = dateCount[str(createdTime[0])] + 1
        else:
            dateCount[str(createdTime[0])] = 1


    print likeCount
    print commentCount
    print dateCount