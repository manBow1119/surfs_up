# Project Overview
The purpose of this analysis was to examine weather data from weather stations in Hawaii to inform decisions about a surf/ice cream shop. Initial analyses gathered precipitation and temperature data for several stations during a given year's time period. These analyses were further examined to reveal descriptive statistics for temperature data for the months of June and December during this time period.

### Technologies
* Python (pandas, numpy, matplotlib, sqlalchemy)
* SQLite
* Flask

### Results
Initial exploratory analysis reveal that: 
* Temperature ranges for most months fall between 68 and 81 degrees, with a strong concentration around 74-77 degress.
* Precipitation tends to be quite cyclical; though precipation occurred frequently and regularly, periodic data show a few data points with nearly twice as much precipitation as local averages.

Further Analysis of June and December data show that:
* There is only slight variability in average temperature for June and December (75 and 71, respectively), with very similar standard deviations.
* While minimum temperature for December (56) was considerably lower than June (64), maximum temperature values show far less variability (83 in Decemeber, 85 in June)

### Summary
One noteable conculsion from this analysis is that temperatures in Hawaii tend to show very little seasonal variability between Summer and Winter months for average and max temperatures, when compared to what one would expect from other states' seasonal patterns. Additionally, there is regular consistent precipitation specifically in Hawaii that is incommensurable with mainland expectations. Future analysis of precipiation data for both June and December should also be queried for a more robust comparison, particularly when guiding decisions for a business that primarily operates outdoors.
