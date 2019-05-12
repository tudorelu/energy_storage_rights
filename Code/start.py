from flask import Flask, render_template, request, jsonify
 
from PIL import Image
Image.MAX_IMAGE_PIXELS = 262215954 
im = Image.open('data/Australia.tif')
import numpy as np 
imarray=np.zeros(im.size)
imarray=np.array(im)

app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('main.html')
 

@app.route("/my_function", methods=["GET", "POST"])
def my_function():
    if request.method == "POST":
        lon= float(request.json['lon'])
        lat= float(request.json['lat'])
        print((lon,lat))
        # top:-8.923184
        # bottom:-43.958184
        # right:159.396449
        # left:112.618949
        # nearest neighbour
        # TBD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        column=int(((lon-112.618949)/(159.396449-112.618949))*imarray.shape[1])
        row=int(((-lat-8.923184)/(43.958184-8.923184))*imarray.shape[0])
        if imarray[row][column]>0:
            return(str(imarray[row][column])+" W/m^2")
    return "No data available"
    
    #     data['release_date'] = request.json['movie_release_date']

    #     print(data, file=sys.stderr)

    #     return jsonify(data)
    # else:
    #     return render_template('the_page_i_was_on.html') 
if __name__ == '__main__':
	app.run(debug=True)