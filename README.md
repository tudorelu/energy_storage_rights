Table of Contents
=================
  * [Status](#Status)
  * [Introduction](#Introduction)
  * [Vision](#Vision)
  * [Objectives](#Objectives)
  * [Deliverables](#Deliverables)
  * [Desired Features](#Desired_Features)
  * [Milestones](#Milestones)
  * [The potential of the project](#The_potential_of_the_project)
  * [Acknowledgement](#Acknowledgement)
  * [Work allocation](#work_allocation)
  * [Link to our other resources](#Link to our other resources)
   

## Status
We are currently undergoing the development of our second deliverable. We have developed a webiste that is able to visualize Solar irradiation, Water occurence, Wind power density, Possible site for Pumped Hydro, and the distance to energy grid node in Australia. In addition, our website have the abilities to do data analysis by identify the possible energy output at the point of interest (for wind and solar for now), determined the possible annual power output, and calculate the return of investment (ROI). However, there is still plenty of room for us to improve on our calculation as we realized there are many factors that can affect the outcome. Moreover, the user are able to draw specific shape in the map using our sketch widget, this can be used for selecting the user-desired area for evaluation. The next step of our development will mainly focus on developing the algorithm for calcuating ROI and further develop on the area selection function. The instruction on how to run our website can be found [here](https://github.com/tudorelu/energy_storage_rights/tree/master/Code)

## Introduction
Deployment of renewable energy technologies in different location are often comes with advantage and disadvantage. The energy storage rights is a digital platform that will map, evaluate, promote and help investments in the development rights for energy storage pilot projects such as pumped hydro energy storage, floating solar pilots on lake or sea. Alongside with the platform is energy storage rights application.

We strike to built up an application which used to evaluate and optimize the performance and potential of location viable for development of different renewable-energy technologies, this outcome will then be visualized to the target user. 

Through our development on this project, we use Google drive for documentation purposes and data storage. Trello for task management and assignment. The links can be found in [Link to our other resources](#Link_to_our_other_resources).

## Vision
Our client, the team of Energy Storage Rights, wishes to develop a website application that can find the best location to get the richest energy source in order to maximize the profit margin. The target users include small enterprises, organizations, individuals. In summary, an applicable and portable website application which can evaluate and utilize the renewable energy for potential users is our client’s desired outcome at the end of the project.  

## Objectives
Refer to [Objectives.xlsx](https://github.com/tudorelu/energy_storage_rights/blob/master/Objectives.xlsx)

## Deliverables
### First deliverable:
#### A basic website with maps ready to use
#### A basic map with some basic functions including search, zoom in & out.
#### A user interface which should be able to display renewable energy distribution in map.
#### Basic data is sourced 
Relevant data of World-wide Wind speed, Solar exposure, Water coverage
#### Basic data is normalized and ready to use
The data we search should be modified to the same format which can be used and visualized by our map. 
#### Being able to visualize layer data
A kind of renewable energy will be shown on our map, including solar, wind and hydro energy, which will be displayed on different layers, at least for sample size scale. 
### Second deliverable (MVP)
#### Other relevant data is sourced
Solar energy: cloud amount and sunrise time, sunset time
Wind energy: wind direction, wind gust
Water energy: The depth of lake, precipitation
#### Energy grid data is implemented 
Display energy grid on map and their distances between each other.
#### Calculate the user selected area
The selected area can be in polygon or rectangle. Once our user select the area they want to learn about, our application should be able to output the estimated electricity generation and its return for each renewable energy annually. 
#### Calculate the potential return of development
#### Calculate the estimated gross return of energy storage installation.
#### User-friendly interface to display essential information
### Third deliverable
#### Find the best combination of different technologies by calculation 
We will find the combinations of three kinds renewable energy including solar, wind and hydro energy.
#### A robust algorithm is developed 
The algorithm should be able to optimise the choices of renewable energy and its corresponding location. 
#### Calculate the return of investment for all combinations of technology
#### A professional & fancy website


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
