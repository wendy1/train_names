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

def trip_printout():
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
                trip_printed.append(trip)
                destination = train['Destination']
                trainNumber = train['Vehicle']
                scheduled = todate(train['Scheduled'])
                if scheduled < datetime.datetime.now() - datetime.timedelta(minutes=10):
                    continue
                if trainNumber == '':
                    trainNumber = 'unknown'
                printlines = printlines +  "%s Trip %s to %s, train '%s'\n" % (scheduled.strftime('%I:%M'), trip, destination, trainNumber)

                # only print out 2 trips for each line
                if len(trip_printed) >= 2:
                    break
    return printlines

if __name__ == '__main__':
    #print trip_printout()
    #exit()

    import androidhelper
    droid = androidhelper.Android()

    while True:
        response = droid.dialogGetInput("Next Trips", trip_printout())
        if response.result is None:
            break