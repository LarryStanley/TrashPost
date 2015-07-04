# -*- coding: utf-8 -*-
import json
import urllib2
import sys

with open("trashData.json") as jsonFile:
    allData = json.load(jsonFile)
    likeCount = 0
    commentCount = 0
    allMessage = ''
    timeCount = []
    dateCount = {}
    hourCount = {}
    for post in allData:
        
        if 'message' in post:
            allMessage += post['message']

        likeCount += int(post['likes']['summary']['total_count'])
        commentCount += int(post['comments']['summary']['total_count'])

        #about created time
        createdTime = post['created_time']
        createdTime = createdTime.split("T")

        #date count
        if str(createdTime[0]) in dateCount:
            dateCount[str(createdTime[0])] = dateCount[str(createdTime[0])] + 1
        else:
            dateCount[str(createdTime[0])] = 1

        #time count
        createdHour = createdTime[1].split(":")[0]
        createdHour = int(createdHour)
        if createdHour in hourCount:
            hourCount[createdHour] = hourCount[createdHour] + 1
        else:
            hourCount[createdHour] = 1

    #sort the result
    dateCount = sorted(dateCount.iteritems(), key=lambda d:d[1], reverse = True)
    hourCount = sorted(hourCount.iteritems(), key=lambda d:d[1], reverse = True)

    print "{}:{}".format("letter", len(allMessage))
    print len(allMessage)/len(allData)
    print "{}:{}".format("Post count", len(allData))
    print "{}:{}".format("Likes",likeCount)
    print "{}:{}".format("Comments",commentCount)
    print dateCount
    print hourCount