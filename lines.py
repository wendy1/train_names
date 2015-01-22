__author__ = 'skamau'
import json
import urllib2
import datetime

def todate(datestring):
    return datetime.datetime.fromtimestamp(int(datestring))

feeds = dict()
feeds['Lowell'] = 'http://developer.mbta.com/lib/RTCR/RailLine_10.json'
feeds['Newburyport/Rockport'] = 'http://developer.mbta.com/lib/RTCR/RailLine_12.json'
feeds['Fitchburg/South Acton'] = 'http://developer.mbta.com/lib/RTCR/RailLine_9.json'

if __name__ == '__main__':

    printlines = ''
    for (line, url) in feeds.items():
        printlines = printlines + "\n--- %s line\n" % line
        info = urllib2.urlopen(url)
        data = json.load(info)

        results = data['Messages']

        trip_printed = []

        for train in sorted(results, key=lambda r:r['Scheduled']):
          trip = train['Trip']
          if not trip in trip_printed:
            destination = train['Destination']
            trainNumber = train['Vehicle']
            scheduled = todate(train['Scheduled'])
            if scheduled < datetime.datetime.now() - datetime.timedelta(minutes=10):
                continue
            if trainNumber == '':
                trainNumber = 'unknown'
            printlines = printlines +  "%s Trip %s to %s, train is '%s'\n" % (scheduled.strftime('%I:%M'), trip, destination, trainNumber)
            trip_printed.append(trip)
    printlines = printlines +  '\n'
    print printlines