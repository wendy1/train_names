#_*_ coding: utf-8 _*_

__author__ = 'skamau'
import json
import urllib2


info = urllib2.urlopen('http://developer.mbta.com/lib/RTCR/RailLine_10.json')

data = json.load(info)

results = data['Messages']

printed = []
for train in results:
  heading = train['Trip']
  if not heading in printed:
    destination = train['Destination']
    trainNumber = train['Vehicle']
    if trainNumber == '':
    	trainNumber = 'unknown'
    print "Trip %s to %s, train is '%s'" % (heading, destination, trainNumber)
    printed. append(heading)