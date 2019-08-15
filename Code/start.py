from flask import Flask, render_template, request, jsonify
 
# import gdal
import numpy as np 
# from PIL import Image

app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('main.html')
    
@app.route('/about')
def about():
	return render_template('about.html')
    
@app.route('/contact')
def contact():
	return render_template('contact.html')
    
@app.route('/news')
def news():
	return render_template('news.html')
 

@app.route("/calculate_wind_power_density", methods=["GET", "POST"])
def calculate_wind_power_density():
    
    if request.method == "POST":
        lon= float(request.json['lon'])
        lat= float(request.json['lat'])
        eff= float(request.json['ef'])
        area= float(request.json['area'])
        # top:-8.923184
        # bottom:-43.958184
        # right:159.396449
        # left:112.618949
        # nearest neighbour
        # TBD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        
        column=int(((lon-112.618949)/(159.396449-112.618949))*14014)
        row=int(((-lat-8.923184)/(43.958184-8.923184))*18711 )
        x=column%140
        y=row%187
        column=int(column/140)
        row=int(row/187)
        data=np.genfromtxt('Datas/AU Wind '+str(column)+'-'+str(row)+'.csv',delimiter=',')
        wind_energy=str("{:.2f}".format(data[x][y]*1*eff/100))+" Wh per day"
        # column=int(((lon-112.618949)/(159.396449-112.618949))*18711)
        # row=int(((-lat-8.923184)/(43.958184-8.923184))*14014 )
        # x=column%187
        # y=row%140
        # column=int(column/187)
        # row=int(row/140)
        # data=np.genfromtxt('Datas/AU Wind '+str(column)+'-'+str(row)+'.csv',delimiter=',')
        # wind_energy=str("{:.2f}".format(data[x][y]*1*eff/100))+" Wh per day"
        # if aus_wind_np[row][column]>0:
        #     wind_energy=str("{:.2f}".format(data[x][y]*1*eff/100))+" Wh per day"
        # else:
        #     wind_energy="No wind data available"
        solar_energy=calculate_solar_energy(lat,lon,area,eff,1)
    return "wind: "+wind_energy+"\n"+"Solar: "+solar_energy
#  E = A * r * H * PR
# Where:
# E = Energy (kWh) 
# A = Total solar panel Area (m2) 
# r = solar panel yield or efficiency(%) 
# H = Annual average solar radiation on tilted panels (shadings not included)
# PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)
# ALLSKY_SFC_SW_DWN SRB/FLASHFlux 1/2x1/2 All Sky Insolation Incident on a Horizontal Surface (kW-hr/m^2/day) 
def calculate_solar_energy(lat,lon,m2,r,PR=1):

    row=int(((lon+180)/(180+180))*43200)
    column=int(((-(lat-60))/(60+55))*13800)
    x=column%138
    y=row%432
    column=int(column/138)
    row=int(row/432)
    data=np.genfromtxt('Datas/AU Solar '+str(column)+'-'+str(row)+'.csv',delimiter=',')
    out=str("{:.2f}".format(float(data[x,y])*m2*r*PR/100))+" kWh per day at "+str(r)+"%' efficiency"
    # row,column=getcolrow(lon,lat,60,-55,180,-180,global_solar_np)
    # print((lat,lon))
    # print((row,column))
    # print(global_solar_np[row][column])
    # if global_solar_np[row][column]>0:
    #     data=global_solar_np[row][column]
    #     out=str("{:.2f}".format(float(data)*m2*r*PR/100))+" kWh per day at "+str(r)+"%' efficiency"
    # else: 
    #     out="No solar data available"
    return out

def getcolrow(lon,lat,top,bottom,right,left,nparr):
    column=int(((lon-left)/(right-left))*nparr.shape[1])
    row=int(((-(lat-top))/(top-bottom))*nparr.shape[0])
    
    return (row,column)
if __name__ == '__main__':
    # 262215954
    # Image.MAX_IMAGE_PIXELS = 500000000
    # print("Loading Australia wind data")
    # aus_wind = Image.open('data/Australia wind.tif')
    # aus_wind_np=np.array(aus_wind)

    # print("Loading Global Solar radiation data")
    # global_solar_np = gdal.Open('data/GHI.tif')
    # global_solar_np = np.array(global_solar_np.GetRasterBand(1).ReadAsArray())

    print("Loading finished")
    app.run(debug=True)