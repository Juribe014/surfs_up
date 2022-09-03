# surfs_up

## Overview of the analysis: 

The purpose of this analysis is to determine the sustainability of an ice cream shop year-round at Oahu, Hawaii. This will be determined by looking at historical temperature data. From this data the hottest month of the year (June) as well as the coldest month of the year (December) will be analyzed. To perform this analysis the following tools were used: SQLite, SQLAlchemy, Pandas, and Python.

## Results: 

The following images are the summary statistics obtained from the the historical data available. 

### June Temperature Summary

![june_summary](https://user-images.githubusercontent.com/104809098/188284726-e9b0c911-f399-4efc-b6ec-2a9fcdb5c445.png)

### December Temperature Summary

![december_summary](https://user-images.githubusercontent.com/104809098/188284729-af49d215-e813-4b4d-887f-5e366c054ce2.png)

* From the images above, one can see that the max temperatures are relatively close to each other for the months of June (85) and December(83). However the minimum for June (64) and December (56) has a much wider difference. 
* The means  are also letting us know that the average temperature is similar for each month (74.9 and 71.0). 
* One must also be aware that the data sets are not looking at the same amount of data points. For June there are 1700 points of reference, while December only has 1517.

## Summary: 

Based on the current information and the analytical tools used, one can determine that temperature trends indicate that an ice-cream shop can remain open year-round. Outside of the summary statistics, it would also be beneficial to remove any outliers in the data sets that might skew the data one way or the other. For this we can use a box plot or scatter plot to have a better visual of the temperature trends. I would also increase the amount of months that are being used to determine sustainability for the ice cream shop.  


























