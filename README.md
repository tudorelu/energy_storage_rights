Table of Contents
=================
  * [Status](#Status)
  * [Introduction](#Introduction)
  * [Vision](#Vision)
  * [Objectives](#Objectives)
  * [Deliverables](#Deliverables)
  * [Desired Features](#Desired-Features)
  * [Milestones](#Milestones)
  * [The potential of the project](#The-potential-of-the_project)
  * [Acknowledgement](#Acknowledgement)
  * [Work allocation](#work-allocation)
  * [Link to our other resources](#Link-to-our-other-resources)
   

## Status
We are currently undergoing the development of our second deliverable. We have developed a webiste that is able to visualize Solar irradiation, Water occurence, Wind power density, Possible site for Pumped Hydro, and the distance to energy grid node in Australia. In addition, our website have the abilities to do data analysis by identify the possible energy output at the point of interest (for wind and solar for now), determined the possible annual power output, and calculate the return of investment (ROI). However, there is still plenty of room for us to improve on our calculation as we realized there are many factors that can affect the outcome. Moreover, the user are able to draw specific shape in the map using our sketch widget, this can be used for selecting the user-desired area for evaluation. The next step of our development will mainly focus on developing the algorithm for calcuating ROI and further develop on the area selection function. The instruction on how to run our website can be found [here](https://github.com/tudorelu/energy_storage_rights/tree/master/Code)

## Introduction
Deployment of renewable energy technologies in different location are often comes with advantage and disadvantage. The energy storage rights is a digital platform that will map, evaluate, promote and help investments in the development rights for energy storage pilot projects such as pumped hydro energy storage, floating solar pilots on lake or sea. Alongside with the platform is energy storage rights application.

We strike to built up an application which used to evaluate and optimize the performance and potential of location viable for development of different renewable-energy technologies, this outcome will then be visualized to the target user. 

Through our development on this project, we use Google drive for documentation purposes and data storage. Trello for task management and assignment. The links can be found in [Link to our other resources](#Link-to-our-other-resources).

## Vision
Our client, the team of Energy Storage Rights, wishes to develop a website application that can find the best location to get the richest energy source in order to maximize the profit margin. The target users include small enterprises, organizations, individuals. In summary, an applicable and portable website application which can evaluate and utilize the renewable energy for potential users is our client’s desired outcome at the end of the project.  

## Objectives
Refer to [Objectives.xlsx](https://github.com/tudorelu/energy_storage_rights/blob/master/Objectives.xlsx)

## Deliverables
### First deliverable:
* **A basic website with maps ready to use**
* **A basic map with some basic functions including search, zoom in & out.**
* **A user interface which should be able to display renewable energy distribution in map.**
* **Basic data is sourced**<br />
Relevant data of World-wide Wind speed, Solar exposure, Water coverage
* **Basic data is normalized and ready to use**<br />
The data we search should be modified to the same format which can be used and visualized by our map. 
* **Being able to visualize layer data**<br />
A kind of renewable energy will be shown on our map, including solar, wind and hydro energy, which will be displayed on different layers, at least for sample size scale. 
### Second deliverable (MVP)
* **Improved functionality of the map engine**<br />
Able to change the basemap base on user preference. Better visualize the data (use transparency and different ways of visualization such as discrete or category)
* **A high-efficient map engine**<br />
The speed of switching between different data layer is slow in deliverable one, it is resonable and neccessary to improve the performance and efficient of the website.
* **Relevant data is sourced**<br />
Solar energy: Global horizontal irradiation, Optimum tilt to maximize yearly yield, Photovoltaic power potential
Wind energy: Wind direction, Wind power density at different height
Water energy: The depth of lake, occurence of water, potential sites for pumped hydro
* **Energy grid data is implemented**<br />
Display energy grid on map and their distances between each other. The visualization should tell the distance from energy grid line ( electricity transmission line) to the point of interest. This can be use to future calculation of the cost that required to implement various renewable technologies.
* **Calculate the user selected area**<br />
The user will be able to selecte area that they are interest to develop renewable technologies. The shape can be in polygon or rectangle. Our application should be able to measure the size of the area and output the estimated potential energy generation and its return for each renewable energy in details. 
* **Calculate the potential return of development**<br />
This include calculate annual power output, annual profit, net profit, and return of investment. The calculation is basic calculation that should be further improved in later development.
* **Calculate the estimated gross return of energy storage installation.**<br />
As above.
* **User-friendly interface to display essential information**<br />
Refine the design on side bar to be more professional.
### Third deliverable
* **Find the best combination of different technologies by calculation**<br />
We will find the combinations of three kinds renewable energy including solar, wind and hydro energy.
* **Use machine learning technologies to predict point of interest where no data available**<br />
We will find the combinations of three kinds renewable energy including solar, wind and hydro energy.
* **A robust algorithm is developed**<br />
The algorithm should be able to optimise the choices of renewable energy and its corresponding location. 
* **Calculate the return of investment for all combinations of technology**
* **A professional & fancy website**


## Desired Features
###  Two primary functions
For our web application, we are planned to have two function to allow the users to identify the suitable area for renewable energy technologies development. 
For our first function, we need to calculate the return of investment by develop various kind of renewable technologies for the area selected by users. Then, we could use a similar algorithm to identify the top N locations that is suitable for development in a relative large area. To rank different locations, we will continue to use the return of investment as the parameter.

### Smart choices by system
Nearest energy grid<br />
Suitable locations for different technologies<br />
Best combination<br />
Analyze local developers<br />
### A user-friendly interface
Area cover<br />
Power output by month<br />
Total power output<br />
Total implementation cost<br />
Annual value<br />
Return of investment<br />
Shown data usage<br />

## Milestones
Refer to [Gantt_project_planner.xlsx](https://github.com/tudorelu/energy_storage_rights/blob/master/Gantt_project_planner.xlsx) above

## The potential of the project
Many potential users are interested in renewable energy, our application can help to identify the high potential area for developing renewable energy. This allow to generate more interaction between the property owner and renewable energy developer. Land owner can be benefit from this application by making more effective and smart decision on the use of renewable energy product, it also help them to reduce the spending in energy, increase in efficiency in energy storage. For the renewable energy developer, it grants them more opportunity to delop their products. This application is expected to create a win-win situation between each parties.

## Acknowledgement
This project is acquired from Tudor Barbulescu (tudor.barbulescu@anu.edu.au) and carried out under computing project courses including COMP3500, COMP4500, and COMP8715 from The Australian National University. This project team is lead by project manager Yuanxin Ye (u5669371@anu.edu.au) and consist sixe other team members, Yunyuan Yu (u6092441@anu.edu.au), Yuanxin Ye (u5669371@anu.edu.au), Weiwei Liang (u6642464@anu.edu.au), Yufei Qian (u5981067@anu.edu.au), Peilin Song (u6225953@anu.edu.au), Dawei Zhang (u6302602@anu.edu.au), and Daoyu Li (u5912264@anu.edu.au).

## Work allocation
|Team member|	Role|	Job description|
|--------|------|--------|
|Yuanxin Ye |	Project manager, Front-end developer, quality assurance engineer|	Responsible for web-development, agenda editing, and audit report writing. Doing research on energy source data and ReactJs.|
|Yunyuan Yu|	Back-end developer,software developer|	Responsible for audit report writing, back-end development and doing research on energy source data. Calculating the best location for getting renewable energy.|
|Weiwei Liang|	Front-end developer,software developer|	Responsible for audit report writing, web-development and agenda writing.|
|Daoyu Li	|Back-end developer,database administrator	|Responsible for doing the data research for renewable energy location. Doing the research of map API. Using the energy database, calculating the best location.|
|Dawei Zhang	|Front-end developer,web developer	|Responsible for web-development. Doing the research on ReactJs.|
|Yufei Qian	|Back-end developer, database developer	|Responsible for doing the data research for renewable energy location. Doing the research of map API. Using the energy database, calculating the best location.|
|Peilin Song	|Front-end developer,web developer	|Responsible for web-development. Doing the research on ReactJs.|

## Link to our other resources
Google doc: https://drive.google.com/open?id=1OcePBJw_gMNDE8a1w4bpGXbVZ-dVddzs <br/>
Trello page: https://trello.com/b/A7bMM3s1/energy-storage-rights

## Other Readme resources
### Master Branch

[Algorithm Document]https://github.com/tudorelu/energy_storage_rights/tree/master/Algorithm%20Documents

https://github.com/tudorelu/energy_storage_rights/tree/master/Code
https://github.com/tudorelu/energy_storage_rights/tree/master/Code/Testing%20on%20sample%20algorithm
https://github.com/tudorelu/energy_storage_rights/tree/master/Code/data
https://github.com/tudorelu/energy_storage_rights/tree/master/Data%20Research
https://github.com/tudorelu/energy_storage_rights/tree/master/Progress
https://github.com/tudorelu/energy_storage_rights/tree/master/To%20Do%20list%20App

### Web Branch
https://github.com/tudorelu/energy_storage_rights/tree/Web

https://github.com/tudorelu/energy_storage_rights/tree/Web/Large%20Data%20File%20To%20Create%20Layers
https://github.com/tudorelu/energy_storage_rights/tree/Web/basic-arcgis
