from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


from jsonrpc import JSONRPCResponseManager, dispatcher
import sqlite3
import sys
import json
import math
import numpy as np
import os.path


from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler



@dispatcher.add_method
def fetchDataWeek(**kwargs):
    # print kwargs["value"]
    # value = kwargs["value"]
    # startDate = kwargs["startDate"]
    print "fetchDataWeek"
    device_id = kwargs["device_id"]
    # print startDate
    value = 604800
    # device_id = "7E33867D-3FD5-08EA-93B7-C03A27D730C9"
    # queryStr = 'select tstamp,rri from heart_rate where device_id = "'+device_id+'" and rri!="" order by tstamp limit '+str(value)
    queryStr = 'select tstamp,rri from heart_rate where device_id = "'+device_id+'" and rri!="" order by tstamp'
    print queryStr


    results = []
    date_results = []
    # for one week when value = 604800
    mySetZeroCount = 7200

    resultCount = 0;
    count = 0
    sdnnTotal = 0
    rmssdTotal = 0
    rrTotal =0
    mrr=0
    last = 0

    # con =None

    try:
        con = sqlite3.connect('db_week.db')

        cur = con.cursor()
        cur.execute(queryStr)


        data = []
        rows = cur.fetchall()
        rri_for_std = []
        for row in rows:
            if int(row[1]) < 1200:
                if row[1]!=None and count>2:
                    rrTotal += int(row[1])
                    mrr = rrTotal/(count-1)
                    sdnnTotal += pow( int(row[1]) - mrr,2)
                    rmssdTotal += pow( int(row[1]) - last,2)
                    last = int(row[1])

                if count==mySetZeroCount:
                    sdnn = math.sqrt(sdnnTotal/(count-1))
                    rmssd = math.sqrt(rmssdTotal/(count-1))
                    if rmssd < 400:
                        results.append(rmssd)
                        date_results.append(row[0])
                    rmssdTotal=0
                    sdnnTotal=0
                    rrTotal=0
                    resultCount+=1
                    count = 0

                count+=1
            # print row[1]
            rri_for_std.append(int(row[1]))

        dataout = []
        print "before std"
        try:
            std = np.std(rri_for_std)
        except:
            traceback.print_exc(file=sys.stdout)
        print "------************ rri std %s:" % std
        for x in range(len(results)):
            dataout.append({'rmssd':results[x],'date':date_results[x]})
    except lite.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

    return dataout


@dispatcher.add_method
def fetchDataOneDay(**kwargs):
    # print kwargs["value"]
    # value = kwargs["value"]
    # startDate = kwargs["startDate"]
    print "fetchDataOneDay"
    device_id = kwargs["device_id"]
    print device_id
    # print startDate
    value = 86400
    # device_id = "7E33867D-3FD5-08EA-93B7-C03A27D730C9"
    queryStr = 'select tstamp,rri from heart_rate where device_id = "'+device_id+'" and rri!="" order by tstamp limit '+str(value)
    print queryStr


    results = []
    date_results = []
    # for one day when value = 86400
    mySetZeroCount = 900

    resultCount = 0;
    count = 0
    sdnnTotal = 0
    rmssdTotal = 0
    rrTotal =0
    mrr=0
    last = 0

    # con =None

    try:
        con = sqlite3.connect('db_week.db')

        cur = con.cursor()
        cur.execute(queryStr)


        data = []
        rows = cur.fetchall()
        for row in rows:
            # if row[1] < 1400:
            if row[1]!=None and count>2 and int(row[1])<1200:
                rrTotal += int(row[1])
                mrr = rrTotal/(count-1)
                sdnnTotal += pow( int(row[1]) - mrr,2)
                rmssdTotal += pow( int(row[1]) - last,2)
                last = int(row[1])
                # count+=1

            if count==mySetZeroCount:
                sdnn = math.sqrt(sdnnTotal/(count-1))
                rmssd = math.sqrt(rmssdTotal/(count-1))
                # if rmssd<400:
                results.append(rmssd)
                date_results.append(row[0])
                rmssdTotal=0
                sdnnTotal=0
                rrTotal=0
                resultCount+=1
                count = 0

            count+=1

        dataout = []
        for x in range(len(results)):
            dataout.append({'rmssd':results[x],'date':date_results[x]})
    except lite.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

    return dataout



@dispatcher.add_method
def fetchData(**kwargs):
    print kwargs["value"]
    value = kwargs["value"]
    startDate = kwargs["startDate"]
    print startDate
    queryStr = 'select tstamp,rri from heart_rate where tstamp > "'+str(startDate)+'"  limit '+str(value)
    print queryStr


    results = []
    date_results = []
    if value==604800:
        mySetZeroCount = 7200
    elif value==259200:
        mySetZeroCount = 3600
    elif value==86400:
        mySetZeroCount = 900
    elif value == 14400:
        mySetZeroCount = 320
    elif value == 7200:
        mySetZeroCount = 180
    else:
        mySetZeroCount = 400
    resultCount = 0;
    count = 0
    sdnnTotal = 0
    rmssdTotal = 0
    rrTotal =0
    mrr=0
    last = 0

    # con =None

    try:
        con = sqlite3.connect('Onyx0333.sqlite')

        cur = con.cursor()
        cur.execute(queryStr)


        data = []
        rows = cur.fetchall()
        for row in rows:
            if row[1]!=None and count>2:
                rrTotal += int(row[1])
                mrr = rrTotal/(count-1)
                sdnnTotal += pow( int(row[1]) - mrr,2)
                rmssdTotal += pow( int(row[1]) - last,2)
                last = int(row[1])

            if count==mySetZeroCount:
                sdnn = math.sqrt(sdnnTotal/(count-1))
                rmssd = math.sqrt(rmssdTotal/(count-1))
                results.append(rmssd)
                date_results.append(row[0])
                rmssdTotal=0
                sdnnTotal=0
                rrTotal=0
                resultCount+=1
                count = 0

            count+=1

        dataout = []
        for x in range(len(results)):
            dataout.append({'rmssd':results[x],'date':date_results[x]})
    except lite.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

    return dataout


@dispatcher.add_method
def pushData(**kwargs):
    print "pushData"
    # print kwargs["data"]
    dataToSave = kwargs["data"]
    dataStress = dataToSave["stressed"]
    dataNotStress = dataToSave["notStressed"]
    # print dataStress

    def getBoundingBox(X):
        print X
        # X = dataToSave
        mean =  np.mean(X,axis=0)
        print mean
        Xlength = len(X)
        X_corrd = X
        print Xlength
        X.append([0,mean[1]])
        X.append([1,mean[1]])
        X.append([3,mean[1]])
        X.append([4,mean[1]])
        X.append([5,mean[1]])
        X.append([1200,mean[1]])
        X.append([1201,mean[1]])
        X.append([1202,mean[1]])
        X.append([1230,mean[1]])
        X.append([1220,mean[1]])

        # print X
        X = StandardScaler().fit_transform(X)
        X[:,1] = 0.12*X[:,1]


        ##############################################################################
        # Compute DBSCAN
        # db = DBSCAN(eps=30, min_samples=8).fit(X)
        # db = DBSCAN(eps=0.15, min_samples=5).fit(X)
        db = DBSCAN(eps=0.18, min_samples=4).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_

        # print X[labels == 5]
        # print labels ==0
        print labels

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

        print('Estimated number of clusters: %d' % n_clusters_)

        def  findBounday(lbl):
            "This returns a bounding box for a label lbl"
            upper=0
            low = 10000
            left = 10000
            right =0
            for  i in range(0,Xlength):
                if labels[i]==lbl:
                    x = X_corrd[i][0]
                    y = X_corrd[i][1]
                    print i,lbl,x,y
                    if x<left:
                        left = x
                    if x>right:
                        right = x
                    if y < low:
                        low = y
                    if y > upper:
                        upper = y

            return [left, low, right - left, upper - low]

        # print findBounday(3)
        # print findBounday(2)
        # print findBounday(1)
        # print findBounday(0)

        boundaryToReturn = []
        for i in range(0, n_clusters_):
            boundary = findBounday(i)
            print i
            print boundary
            if boundary[0]!=10000:
                boundaryToReturn.append(boundary)

        return boundaryToReturn
###################### end def getboundingbox


    print dataStress
    print "-------------------data stress clustering-----------------------"
    boundingboxStress = getBoundingBox(dataStress)
    print "-------------------data notstress clustering-----------------------"
    boundingboxNotStress = getBoundingBox(dataNotStress)

    print boundingboxStress
    boundingbox = {}
    boundingbox["stress"] = boundingboxStress
    boundingbox["notStressed"] = boundingboxNotStress

    np.save("log.npy",dataToSave)
    # return boundaryToReturn
    return boundingbox


@dispatcher.add_method
def checkNames(**kwargs):
    print "checkMinMaxDates"
    sqlite3.sqlite_version
    con = None
    dataResult = []
    try:
        con = sqlite3.connect('db_week.db')

        cur = con.cursor()
        cur.execute("select distinct device_id from heart_rate")


        dataResult = []
        rows = cur.fetchall()
        for row in rows:
            date_results.append(row[0])
    except lite.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()
    return data


@dispatcher.add_method
def checkMinMaxDates(**kwargs):
    print "checkMinMaxDates"
    sqlite3.sqlite_version
    con = None
    data = []
    try:
        con = sqlite3.connect('Onyx0333.sqlite')
        cur = con.cursor()
        cur.execute('SELECT min(tstamp) from heart_rate')
        tstampMin = cur.fetchone()
        data.append(tstampMin)

        cur.execute('SELECT max(tstamp) from heart_rate')
        tstampMax = cur.fetchone()
        data.append(tstampMax)
        print "MinDate: %s" % data + "MaxDate: %s" % data

    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()
    return data


@Request.application
def application(request):
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4010, application)
