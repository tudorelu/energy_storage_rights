
Description
=================
This folder contain data collected from NASA POWER Project Data Sets (https://power.larc.nasa.gov/data-access-viewer/)
This including all sky/clear sky solar insolation data, Wind speed data at 50 meters, and some other relevant data.
However, those data can be only retreive by small amount of area or single point. Therefore, we have derive a simple algorithm to consolidate each file into one single output.
The raw data from the website contains various information that is no related when plotting our map on our map engine. We design our algorithm to reformat the data into the style that is accepted by Mapbox Engine. 



## Sample Data

-BEGIN HEADER-																
NASA/POWER SRB/FLASHFlux/MERRA2/GEOS 5.12.4 (FP-IT) 0.5 x 0.5 Degree Interannual Averages/Sums 																
Dates (month/day/year): 01/01/2017 through 12/31/2017 																
Location: Regional 																
Elevation from MERRA-2: Average for 1/2x1/2 degree lat/lon region = na meters   Site = na 																
Climate zone: na (reference Briggs et al: http://www.energycodes.gov) 																
Value for missing model data cannot be computed or out of model availability range: -999 																
Parameter(s): 																
ALLSKY_SFC_SW_DWN SRB/FLASHFlux 1/2x1/2 All Sky Insolation Incident on a Horizontal Surface (kW-hr/m^2/day) 																
-END HEADER-																

|LAT	|LON	|PARAMETER	|YEAR	|JAN	|FEB	|MAR	|APR	|MAY	|JUN	|JUL	|AUG	|SEP	|OCT	|NOV	|DEC	|ANN
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|--------|
|-35.25	|148.75	|ALLSKY_SFC_SW_DWN	|2017	|7.35	|6.55	|4.93	|3.96	|2.89	|2.52	|2.4	|3.28	|4.43	|6.02	|6.7	|6.77	|4.82|
|-35.25	|149.25	|ALLSKY_SFC_SW_DWN	|2017	|6.95	|5.94	|4.22	|3.92	|2.99	|2.39	|2.78	|3.63	|5.15	|5.93	|6.31	|6.48	|4.72|

## Sample Output

|latitude	|longitude	|mass (g)|
|---|---|---|
|-35.25	|149.25	|4.72|
|-35.25	|149.25	|4.72|
|-35.25	|148.75	|4.82|
|-35.25	|148.75	|4.82|
|-35.25	|149.25	|4.72|
|-35.25	|149.25	|4.72|
|-35.25	|148.75	|4.82|
|-35.25	|148.75	|4.82|
|-35.25	|149.25	|4.72|
|-35.25	|149.25	|4.72|
|-35.25	|148.75	|4.82|
|-35.25	|148.75	|4.82|
|-35.25	|149.25	|4.72|
|-35.25	|149.25	|4.72|
|-35.25	|148.75	|4.82|
|-35.25	|148.75	|4.82|
