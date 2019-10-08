
from flask import *

from datetime import datetime


from numpy import *

import pandas as pd


import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from math import sin, cos, sqrt, atan2, radians




app = Flask(__name__)

lookupdict ={}
print("+===========================================================================")
print("Loading !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for r in pd.read_csv('TokenLookup.csv', sep=',').values:
    
    lookupdict[r[0]]=r[1]
print(lookupdict)
if not len(lookupdict)>1:
    print("Loading Fail")
else: print("Success")
lookupdict=lookupdict
pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values
df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
energygriddata= pd.concat([df1,df2]).values


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        if n<=b:
            digits.append(int(n % (b+1)))
            n //= (b+1)
        else:
            digits.append(int(n % b))
            n //= b
    return digits[::-1]
def ConvertNumberIntoCell(x,y):
    ldict={0:'',1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    sout=""
    for i in numberToBase(y,26):
        if i==0 and len(sout)>=1:
            sout=sout+'z'
        else:
            sout=sout+ldict[i]
    return sout+str(x)

def distance(arr1,arr2):
    

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(arr1[0])
    lon1 = radians(arr1[1])
    lat2 = radians(arr2[0])
    lon2 = radians(arr2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

def findcloestpoint(x,y,data):
    # print("Retriveing Distance to Grid===================================")
    dist=100000
    value=0
    for i in range(len(data)):
        cdist=distance([x,y],data[i][1:3])
        if cdist<dist:
            dist=cdist
            value=data[i][3]

    # print("Finished Retriveing Distance to Grid===================================")
    return value
	
def ConvertLatlonToCellLocation(lat,lon,minLat,maxLat,minLon,maxLon,numberofrow,numberofcolumn):
    print((lat,lon,minLat,maxLat,minLon,maxLon,numberofrow,numberofcolumn))
    xd=((maxLat-minLat)-(lat-minLat))/(maxLat-minLat)*20
    x=math.floor((xd-math.floor(xd))*numberofrow)
    y=int(numberofcolumn*(lon-minLon)/(maxLon-minLon))
    print((x,y))
#     print((x,y))
    return ConvertNumberIntoCell(x,y)




def calfilename(lat,maxLat,minLat):
    return math.floor(((maxLat-minLat)-(lat-minLat))/(maxLat-minLat)*20)
	
def findcloestPumpedHydro(x,y,data):
    # print("Retriveing Pumped Hydro===================================")
    dist=100000
    value=0
    for i in range(len(data)):
        cdist=distance([x,y],data[i][0:2])
        if cdist<dist:
            dist=cdist
            value=data[i][5]
    print("Result: "+str(value))
    # print("Finished Retriveing Pumped Hydro===================================")
    return value 



@app.route('/calculate_solar_power',methods=['GET','POST'])
def calculate_solar_power():
    global a
	# print("COMING IN TO EXTRACT DATA---------------------------------------------------------------------")
    if request.method=='POST':
        lat= float(request.json['lon'])
        lon= float(request.json['lat'])
        print("-----------------------------------------------------------")
        # print(a + "  sssssssssssssssssssssssssssss")
        # # for r in pd.read_csv('TokenLookup.csv', sep=',').values:
        # #     lookupdict[r[0]]=r[1]
        
        # for r in pd.read_csv('TokenLookup.csv', sep=',').values:
            
        #     lookupdict[r[0]]=r[1]
        
        # pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values
        # df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
        # df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
        # energygriddata= pd.concat([df1,df2]).values



        return "Solar: "+str(RetriveSolar(lat,lon,lookupdict,-180,180,-55,60)[0])+" Wind: "+str(RetriveWind(lat,lon,lookupdict,112.61894917579332,159.39644917579332,-43.95818385506394,-8.92318385506394)[0])+" Distance to grid: "+str(findcloestpoint(lat,lon,energygriddata))+" Pumped Hydro: "+str(findcloestPumpedHydro(lat,lon,pumpedhydrodata))


		
	# print("EXITING FROM EXTRACT DATA---------------------------------------------------------------------")

# @app.route('/get_solar',methods=['GET','POST'])
# def get_solar():
#     if request.method=='POST':
#         lat= float(request.json['lon'])
#         lon= float(request.json['lat'])
#         lookupdict={}
#         for r in pd.read_csv('TokenLookup.csv', sep=',').values:
            
#             lookupdict[r[0]]=r[1]

#         return "Solar: "+str(RetriveSolar(lat,lon,lookupdict,-180,180,-55,60))
# @app.route('/get_wind',methods=['GET','POST'])
# def get_wind():
#     if request.method=='POST':
#         lat= float(request.json['lon'])
#         lon= float(request.json['lat'])
#         lookupdict={}
#         for r in pd.read_csv('TokenLookup.csv', sep=',').values:
            
#             lookupdict[r[0]]=r[1]


#         return " Wind: "+str(RetriveWind(lat,lon,lookupdict,112.61894917579332,159.39644917579332,-43.95818385506394,-8.92318385506394))

# @app.route('/get_pump',methods=['GET','POST'])
# def get_pump():
#     if request.method=='POST':
#         lat= float(request.json['lon'])
#         lon= float(request.json['lat'])
#         pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values



#         return " Pumped Hydro: "+str(findcloestPumpedHydro(lat,lon,pumpedhydrodata))

# @app.route('/get_grid',methods=['GET','POST'])
# def get_grid():
#     if request.method=='POST':
#         lat= float(request.json['lon'])
#         lon= float(request.json['lat'])
#         df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
#         df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
#         energygriddata= pd.concat([df1,df2]).values



#         return " Distance to grid: "+str(findcloestpoint(lat,lon,energygriddata))

def RetriveWind(lat,lon,LookUpDict,minLat,maxLat,minLon,maxLon):
#     Wind each is 233 or 234 *6237
# 112.61894917579332 159.39644917579332
# -43.95818385506394 -8.92318385506394
    # print("Retriveing AU Wind===================================")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
#     Dict {"AU Wind 1-0":'1SibpS2SvGV7G6U5I3IEWajAW_unr0S0TJUnQ1fKTqyc'}
    # print("File Selected: AU Wind "+str(calfilename(lat,maxLat,minLat))+"-0")
    SAMPLE_SPREADSHEET_ID = LookUpDict["AU Wind "+str(calfilename(lat,maxLat,minLat))+"-0"]
    print(SAMPLE_SPREADSHEET_ID + "   SAMPLE_SPREADSHEET_ID")
    SAMPLE_RANGE_NAME = 'Sheet1!'+ConvertLatlonToCellLocation(lat,lon,minLat,maxLat,minLon,maxLon,233,6237)
    print(SAMPLE_RANGE_NAME + "   SAMPLE_RANGE_NAME")
    # print("Range Selected: "+SAMPLE_RANGE_NAME)
    
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        # print('No data found.')
		# print("Finishe Retriveing Wind===================================")
	    return 0
    else:
        # print('Found:'+str(values[0]))
		# print("Finishe Retriveing Wind===================================")
        return values[0]
		
def RetriveSolar(lat,lon,LookUpDict,minLat,maxLat,minLon,maxLon):
#     Solar 230 *14400
# -180.0 180.0
# -55.0 60.0
    # print("Retriveing Solar===================================")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
#     Dict {"AU Wind 1-0":'1SibpS2SvGV7G6U5I3IEWajAW_unr0S0TJUnQ1fKTqyc'}
    # print("File Selected: Solar "+str(calfilename(lat,maxLat,minLat))+"-0")
    SAMPLE_SPREADSHEET_ID = LookUpDict["Solar "+str(calfilename(lat,maxLat,minLat))+"-0"]
    SAMPLE_RANGE_NAME = 'Sheet1!'+ConvertLatlonToCellLocation(lat,lon,minLat,maxLat,minLon,maxLon,230,14400)
    # print("Range Selected: "+SAMPLE_RANGE_NAME)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        # print('No data found.')
		# print("Finishe Retriveing Solar===================================")
	    return 0
    else:
        # print('Found:'+str(values[0]))
		# print("Finishe Retriveing Solar===================================")
        return values[0]

@app.route('/')
@app.route('/index')
def index():
    lookupdict ={}
    print("+===========================================================================")
    print("Loading Token")
    # for r in pd.read_csv('TokenLookup.csv', sep=',').values:
    
    #     lookupdict[r[0]]=r[1]
    # print(lookupdict)
    # if not len(lookupdict)>1:
    #     print("Loading Fail")
    # else: print("Success")
    # g.lookupdict=lookupdict
    # g.pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values
    # df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
    # df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
    # g.energygriddata= pd.concat([df1,df2]).values
    # print("Finished Loading Pumped Hydro and energy grid data from loca server")
    # print("+===========================================================================")
    return render_template('index.html')



@app.route('/map')

def map():
    lookupdict ={}
    print("+===========================================================================")
    print("Loading !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    global a
    a= "aaaa"
    # for r in pd.read_csv('TokenLookup.csv', sep=',').values:
        
    #     lookupdict[r[0]]=r[1]
    # print(lookupdict)
    # if not len(lookupdict)>1:
    #     print("Loading Fail")
    # else: print("Success")
    # g.lookupdict=lookupdict
    # g.pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values
    # df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
    # df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
    # g.energygriddata= pd.concat([df1,df2]).values
 
    return render_template('map.html')




def getcolrow(lon,lat,top,bottom,right,left,nparr):

    my_data = genfromtxt('output.csv', delimiter=',')

    column=int(((lon-left)/(right-left))*nparr.shape[1])

    row=int(((-(lat-top))/(top-bottom))*nparr.shape[0])

    

    return (row,column)


if __name__ == '__main__':

    
    # assign_value(b)
    # lookupdict ={}
    
    # for r in pd.read_csv('TokenLookup.csv', sep=',').values:
        
    #     lookupdict[r[0]]=r[1]
    # print(lookupdict)
    # if not len(lookupdict)>1:
    #     print("Loading Fail")
    # else: print("Success")
    # messages="NMB"
    # setattr(g, '_messages', messages)
    # g.lookupdict=lookupdict
    # g.pumpedhydrodata=pd.read_csv('pumpedhydro.csv', sep=',').values
    # df1=pd.read_csv('Energy Grid Data 1.csv', sep=',',header=None)
    # df2=pd.read_csv('Energy Grid Data 2.csv', sep=',',header=None)
    # g.energygriddata= pd.concat([df1,df2]).values
    app.run(debug=True)