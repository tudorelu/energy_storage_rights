Table of Contents
=================
  * [Status](#Status)
  * [Introduction](#Introduction)
  * [Vision](#Vision)
  * [Main features](#Main-features)
  * [Deliverables](#Deliverables)
  * [Desired Features](#Desired-Features)
  * [Milestones](#Milestones)
  * [The potential of the project](#The-potential-of-the_project)
  * [Acknowledgement](#Acknowledgement)
  * [Work allocation](#work-allocation)
  * [Link to our other resources](#Link-to-our-other-resources)
  * [Other Readme resources](#Other-Readme-resources)
   



## Status
We are currently undergoing the development of our second deliverable. We have developed a website that can visualize Solar irradiation, Water occurrence, Windpower density, Possible site for Pumped Hydro, and the distance to energy grid node in Australia. Also, our website has the abilities to do data analysis by identifying the possible energy output at the point of interest (for wind and solar for now), determined the possible annual power output, and calculate the return of investment (ROI). However, there is still plenty of room for us to improve on our calculation as we realized there are many factors that can affect the outcome. Moreover, the user can draw the specific shape in the map using our sketch widget, this can be used for selecting the user-desired area for evaluation. We use our Web branch to explore possibilities during development while the master branch consists of all the final works that are aligned with our deliverable. The next phase of the development will be mainly focused on developing the algorithm for calculating ROI and further develop on the area selection function. The instruction on how to run our website can be found [here](https://github.com/tudorelu/energy_storage_rights/tree/master/Code)

## Introduction
Deployment of renewable energy technologies in a different location often comes with advantage and disadvantage. The energy storage rights is a digital platform that will map, evaluate, promote and help investments in the development rights for energy storage pilot projects such as pumped hydro energy storage, floating solar pilots on lake or sea. Alongside with the platform is energy storage rights application.

We strike to build up an application which used to evaluate and optimize the performance and potential of location viable for development of different renewable-energy technologies, this outcome will then be visualized to the target user.

Through our development on this project, we use Google drive for documentation purposes and data storage. Trello for task management and assignment. The links can be found in [Link to our other resources](#Link-to-our-other-resources).

## Vision
Our client, the team of Energy Storage Rights, wishes to develop a website application that can find the best location to get the richest energy source in order to maximize the profit margin. The target users include small enterprises, organizations, individuals. In summary, an applicable and portable website application which can evaluate and utilize the renewable energy for potential users is our client’s desired outcome at the end of the project.  

## Main features

* **Visualize the energy distribution gloabal wide in the website**
* **Allow user to see the potential energy output from implementing renewable technologies in the desire location**
* **Energy output can be calculated by single point or polygon area**
* **Allow variation when calculating potential energy output using different attribute (energy price, hardware specification, etc.)**
* **Predict potential energy output using data that not involve in the equation (e.g. tempurature) instead of correlated data (e.g. solar irradiation)**

## Deliverables
### First deliverable (Semester 1 Week 6):
* **A basic website with maps ready to use**
* **A basic map with some basic functions including search, zoom in & out.**
* **A user interface which should be able to display renewable energy distribution in map.**
* **Basic data is sourced**<br />
Relevant data of World-wide Wind speed, Solar exposure, Water coverage
* **Basic data is normalized and ready to use**<br />
The data we search should be modified to the same format which can be used and visualized by our map. 
* **Being able to visualize layer data**<br />
A kind of renewable energy will be shown on our map, including solar, wind and hydro energy, which will be displayed on different layers, at least for sample size scale. 
### Second deliverable (MVP, Semester 1 Week 10)
* **Improved functionality of the map engine**<br />
Able to change the basemap base on user preference. Better visualize the data (use transparency and different ways of visualization such as discrete or category)
* **A high-efficient map engine**<br />
The speed of switching between different data layer is slow in deliverable one, it is resonable and neccessary to improve the performance and efficient of the website.
* **Relevant data is sourced**<br />
Solar energy: Global horizontal irradiation, Optimum tilt to maximize yearly yield, Photovoltaic power potential
Wind energy: Wind direction, Wind power density at different height
Water energy: The depth of lake, occurence of water, potential sites for pumped hydro
* **Energy grid data is implemented**<br />
Display energy grid on the map and their distances between each other. The visualization should tell the distance from the energy grid line ( electricity transmission line) to the point of interest. This can be used to future calculation of the cost required to implement various renewable technologies.
* **Calculate the user selected area**<br />
The user will be able to select the area that they are interesting to develop renewable technologies. The shape can be in polygon or rectangle. Our application should be able to measure the size of the area and output the estimated potential energy generation and its return for each renewable energy in details. 
* **Calculate the potential return of development**<br />
This include calculate annual power output, annual profit, net profit, and return of investment. The calculation is basic calculation that should be further improved in later development.
* **Calculate the estimated gross return of energy storage installation.**<br />
As above.
* **User-friendly interface to display essential information**<br />
Refine the design on side bar to be more professional.
### Third deliverable (Semester 2)
#### Stage 1 (By Week 6): 
##### Front-end: 
* **User interface design research and improvement**<br />
-A more user-friendly UI plan is refined.<br />
-Self-review previous UI structure<br />
-Develop and improve the information panel.<br />
* **Onboarding information page**<br />
-Use short, clear, subtle images and video, and plenty of personality in its user onboarding flow to welcome new users and introduce important features.<br />
-Design a step by step User Manual/Guide and FAQ to make clear instruction for users. All core functions and features are included.<br />
* **Technical Review**<br />
-Review code readability, cohesion and coupling<br />
-Review program structure and architecture<br />
-Review compatibility<br />
* **Web server testing, comparison, and selection**<br />
* **Research & find an appropriate web server for backend usage**<br />
##### Back-end: 
* **Prepare a basic algorithm report on renewable energy calculation**<br />
1.	Wind  2.	Solar  3.	Pump Hydro
* **Find a storage method for Map layer data that has better compatibility**<br />
Given that our local data is big and is not compatible with many devices. Therefore, a faster way should be considered and implemented to allow the data can be read and process from every computer. <br />
The solution should be: <br />
-Allow the data to be read by every computer <br />
-Allow the data to be preprocessed  in a more efficient way. <br />
* **Research on alternative algorithm for energy calculation**<br />
Explore on other algorithm that can be used for calculation to determine the pros and cons of each algorithm.
* **Research and implement on algorithm of implementation cost of renewable energy facility**<br />
* **Integrate every algorithm with website**<br />

#### Stage 2 (By Week 10):
##### Front-end: 
* **Complete user acceptance testing. UI is refined based on user feedback**<br />
* **Web host is implemented and integrated.**<br />
Web hosting is a server where websites stored. Some features to consider: Server performance, price, features, customer supports, and server physical locations. Our website will need to be live by this stage.
* **Test case for web host implementation is created and tested. The test case should cover the program stability, usability, and efficiency.**<br />
* **Final code review**<br />
-Review code readability, cohesion and coupling<br />
-Review program structure and architecture<br />
-Review compatibility<br />
* **Handover documentation.**<br />
##### Front-end: 
* **ML model to predict energy output where incomplete data is presented**<br />
Select and train the ML model where it can predict the potential energy output where there is little or no data are given. Select and compare to choose a suitable model where it can predict with the highest accuracy. <br />
-    For example, when predicting solar energy output in a given point, potential output is given where the solar irradiation data is presented by default. When there is no available data for solar irradiation, the model should predict the solar irradiation value base on the data such as temperature where it is widely available.<br />
-    The model performance should be measured by accuracy, the accuracy measurement method will be decided later when we use different models. Some possible measure method includes Mean Squared Error, F1 score, and absolute difference. 


## Desired Features
Our final product is desired to have some other functions. The application should be able to identify the top N locations that are suitable for development in a relatively large area. To rank different locations, we will continue to use the return of investment as the parameter.<br />
On the other hand, the application should be able to select a combination of different technologies where it yields most energy output.

## Milestones
Refer to [Gantt Chart](https://github.com/tudorelu/energy_storage_rights/blob/master/Documents/Gantt Chart.xlsx)

## The potential of the project
Many potential users are interested in renewable energy, our application can help to identify the high potential area for developing renewable energy. This allows for generating more interaction between the property owner and the renewable energy developer. The landowner can benefit from this application by making a more effective and smart decision on the use of renewable energy product, it also helps them to reduce the spending in energy, increase in efficiency in energy storage. For the renewable energy developer, it grants them more opportunity to develop their products. This application is expected to create a win-win situation between each party.

## Acknowledgement
This project is acquired from Tudor Barbulescu (tudor.barbulescu@anu.edu.au) and carried out under computing project courses including COMP3500, COMP4500, and COMP8715 from The Australian National University. This project team is lead by project manager Yuanxin Ye (u5669371@anu.edu.au) and consist sixe other team members, Yunyuan Yu (u6092441@anu.edu.au), Yuanxin Ye (u5669371@anu.edu.au), Weiwei Liang (u6642464@anu.edu.au), Yufei Qian (u5981067@anu.edu.au), Peilin Song (u6225953@anu.edu.au), Dawei Zhang (u6302602@anu.edu.au), and Daoyu Li (u5912264@anu.edu.au).

## Work allocation
|Role|Principle|Vice|Assistant|
|--------|------|--------|--------|
|Project Manager|Yuanxin Ye|
|Spokesman|Yuanxin Ye | Yufei Qian|Yunyuan Yu|
|Recorder|Weiwei Liang |Yufei Qian|Yuanxin Ye|
|Back-end: Data Source Researcher|Yufei Qian|Daoyu Li|Yunyuan Yu, Weiwei Liang|
|Back-end: Algorithm Researcher|Weiwei Liang|Yufei Qian|Yunyuan Yu
|Back-end: Machine Learning Researcher and Developer|Daoyu Li|Yunyuan Yu|Yufei Qian, Yuanxin Ye|
|Back-end: Data Cleaning and Management developer|Dawei Zhang|Yunyuan Yu|
|Front-end: Web Developer|Peilin Song |Dawei Zhang|Yunyuan Yu, Daoyu Li|
|Front-end: Algorithm Tester and Developer|Yunyuan Yu|Peilin Song|Yufei Qian, Weiwei Liang|
|Front-end: Web Host server researcher|Dawei Zhang|Peilin Song|Yunyuan Yu, Daoyu Li|
|Front-end: Web Host implementation Developer|Daiwei Zhang|PeilinSong|Yunyuan Yu, Daoyu Li|
|Font-end Back-end Integrator|Yunyuan Yu|Yuanxin Ye|

## Link to our other resources
[Google doc](https://drive.google.com/open?id=1OcePBJw_gMNDE8a1w4bpGXbVZ-dVddzs) <br/>
[Meeting Agendas]( https://drive.google.com/drive/folders/1ruHMGQEwZx8xxoOjOGPwa9xU5NgL7rAN  )<br/>
[Algorithm Document]( https://drive.google.com/drive/folders/1IF7tnOA0B2_ef84wrJ-9GveKArFg9Ek4  )<br/>
[Data Research](https://drive.google.com/drive/folders/1ouNpwJ68z57oJTDXcNoi7cSna5wYiK6W  )<br/>
[Data Collection]( https://drive.google.com/drive/folders/1mtH_evyiBC0kgZiA23ROwWvUPP2KmC6z  )<br/>
[Decision Log]( https://drive.google.com/drive/folders/1CEMSQgAogMe8vQJReyoHRvSMf1Q6JC9H  )<br/>
[Reflection](https://drive.google.com/drive/folders/1XsYDRaATwrU3pg5XVH8vvCI1uunZui_c  )<br/>
[Risk Register]( https://drive.google.com/drive/folders/1cQ4A8ppLE5xk9f_Fk1UyjdJrg7GF1jlN  )<br/>
[Stakeholder analysis]( https://drive.google.com/drive/folders/10gsUFsP6mTIeGsW1DiLlHAU1DYdazl2U  )<br/>
[Test Case]( https://drive.google.com/drive/folders/1mXzHyvk3NEHUHc-ea4OYsFEOOUlcOTlA  )<br/>
[Work Log]( https://drive.google.com/drive/folders/1MQU0xjfCFbGTKCB5QzTTYm8QJPny00xG  )<br/>
[Trello page]( https://trello.com/b/A7bMM3s1/energy-storage-rights  )<br/>
[Semester 1 Document]( https://drive.google.com/drive/folders/1BD-qphvc1mOOeRAqcmFgobbKJgBE7TIh  )<br/>

## Other Readme resources
### Master Branch
[Master](https://github.com/tudorelu/energy_storage_rights)<br />
[Algorithm Document](https://github.com/tudorelu/energy_storage_rights/tree/master/Algorithm%20Documents)<br />
[Code](https://github.com/tudorelu/energy_storage_rights/tree/master/Code)<br />
[Code/Testing](https://github.com/tudorelu/energy_storage_rights/tree/master/Code/Testing%20on%20sample%20algorithm)<br />
[Code/data](https://github.com/tudorelu/energy_storage_rights/tree/master/Code/data)<br />
[Data Research](https://github.com/tudorelu/energy_storage_rights/tree/master/Data%20Research)<br />
[Progress](https://github.com/tudorelu/energy_storage_rights/tree/master/Progress)<br />
[To Do List App](https://github.com/tudorelu/energy_storage_rights/tree/master/To%20Do%20list%20App)<br />

### Web Branch
[Web](https://github.com/tudorelu/energy_storage_rights/tree/Web)<br />
[Large Data File](https://github.com/tudorelu/energy_storage_rights/tree/Web/Large%20Data%20File%20To%20Create%20Layers)<br />
[Basic Arcgis](https://github.com/tudorelu/energy_storage_rights/tree/Web/basic-arcgis)<br />
