## WTI and Brent Prices Prediction
<b>Prepared by</b>: Muhammad Amirul (17202062), Zaimie Azmin (17202336)
<br/><b>Instructor</b>: Prof. Dr. Teh Ying Wah
<br/><b>Subject</b>: WQD7005 Data Mining

## 

The world depends on crude oil as it is an essential source of energy. However, crude oil is a non-renewable energy which means it comes from sources that will not be replenished. Crude oil is an important source of energy due to its myriad uses in daily life. Crude oil can be refined and transformed into petrochemicals and other more useful products through a process known as petroleum refining process. It is a process used by oil refinery or petroleum refinery to produce products such as liquified petroleum gas(LPG), gasoline, jet fuel, diesel fuel, industrial fuel and asphalt base. Oil refineries use many processing units and one of them is known as crude oil distillation unit (CDU) which is the first processing unit in almost all oil refineries. The CDU distils crude oil to separate it into fractions of different boiling points which then are processed further in other processing units. Automobiles need oil to operate. Production of myriad household goods is using oil-based plastics as raw materials. Thus, the whole world is depending on crude oil. 

Crude oil is one of the commodities sold in the market with volatile price which plays important roles in the global economy. There are several crude oil prices traded internationally and one of them is West Texas Intermediate (WTI). Fluctuation of crude oil price affects both oil producing and non-oil producing countries. High crude oil price adds burden to consumers especially those with low wages. Both poor and rich people rely on automobiles—need fuel to operate—for commuting which means spending in fuel for automobiles is unavoidable as it is a necessary spending even if the crude oil price rises. High crude oil price affects directly to the poor people. Oil exporters and oilfield service companies are benefited from increasing crude oil price but face huge difficulties when the price falls. Changes in crude oil price even shift the political landscape all over the world. Changing crude oil price affects significantly to the world economy. Knowing that many things are affected by the fluctuation of crude oil price,forecasting crude oil price can be very useful to anyone who interested in investing in the crude oil market. 

This project is divided into 4 milestone. Starting from data collection up until model deployment. Following are the updates for each milestone:


<b>Milestone 1:</b> Web Crawling

In this part, we crawled the data needed using some libraries from Python like BeautifulSoup and Selenium. selenium is used to open the browser and wait for the webiste to fully load all the javascript. Then, we used BeatifulSoup to get the html tag that we desired. Further explanation can be seen in the following links.
* Python code: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/webcrawl.py">webcrawl.py</a>
* Data crawled in csv format: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/wtiprice.csv">wtiprice.csv</a>
* Slides: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/MILESTONE%201%20-%20WEB%20SCRAPING.pdf">MILESTONE 1 - WEB SCRAPING</a>
* Youtube video: <a href="https://youtu.be/6_hUi_ktaWw">Web crawling using python</a>


<b>Milestone 2:</b> Uploading Data into Hive

Apache Hive is an open software in which its processing uses MapReduce. It is easy to adapt with Hive since it use SQL-like language. Further explanation can be seen in the following links.
* Slides: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/MILESTONE%202%20-%20STORE%20DATA%20INTO%20HIVE.pdf">MILESTONE 2 - STORE DATA INTO HIVE DATA WAREHOUSE</a> & <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/MILESTONE%202%20-%20INSTALLATION%20AND%20PROGRESS%20UPDATES.pdf">INSTALLATION & UPDATES</a>
* Youtube video: <a href="https://youtu.be/A2JoxsWwvZ4">
Uploading CSV File to Hive</a>


<b>Milestone 3:</b> Connecting Hive to Python

Once our data is inserted in Hive, we can acces it through Python by using library named PyHive. PyHive will connect to HiveServer2 and we will be able to write query from Python and recieve the data easily.
* Python code: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/ConnHive.ipynb">here</a>
* Instruction: <a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/howpyhive.txt">Installing PyHive</a>
* Youtube video: <a href="https://youtu.be/vsGvP_vGuTo">Connect to Apache Hive using PyHive</a>


<b>Milestone 4:</b> Modeling

This part focusses on modeling the price prediction fo crude oil prices. We used Support Vector Machine (SVM), Linear Regresion, as well as Long Short-Term Memory algorithm to create the model. Step by step on how to do each modelling is shared in the links below:
* Python code: 
<a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/WTI%20Prediction%20(LSTM).ipynb">Predicting WTI Price using LSTM</a> &
<a href="https://github.com/muhdamirulsamsul/DataMining/blob/master/WTI%20Closing%20Price%20Prediction%20(SVM%20%26%20LR).ipynb">Predicting WTI Price using SVM and LR</a>

<b>Milestone 5:</b> Deployment

Once we done with the modelling, it's time to deploy our model in Kivy and Flask. Kivy and Flask are framework for application and web development. 
* Youtube video: <a href="https://youtu.be/BscIYNKPtC0">Deploying Machine Learning Model in Mobile App using Kivy</a>
* Source code: <a href="https://github.com/muhdamirulsamsul/DataMining/tree/master/kivy_project">kivy_project</a>
* Visit our website: http://wqd190018.pythonanywhere.com/
