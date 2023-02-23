import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib

#url = str( https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/04-01-2021.csv)

url_1 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/04-"

url_2 = "-2021.csv"

urls = []
for i in range(1,31):
  if i <10:
    temp_url = "0" + str(i)
  else:
    temp_url = str(i)
  temp = str(url_1 + temp_url + url_2)
  urls.append(temp)

url_data = (r'url')



all_data = []

for i in range(0,len(urls)):
  

  data_csv = pd.read_csv(urls[i])

  data_csv.head()

  data_list = data_csv.values.tolist()

  all_data.append(data_list)

want_data = []

for j in range(0,len(all_data)):

  for i in range(0,58): 


    temp_list = []
  
    #state
    temp_list.append(all_data[j][i][0]) 

    # confirmed cases
    temp_list.append(all_data[j][i][5])

    # deaths
    temp_list.append(all_data[j][i][6])

    # total tests
    temp_list.append(all_data[j][i][11])

    # testing rate - out of 100,000 persons
    temp_list.append(all_data[j][i][16])

    want_data.append(temp_list)






# INPUT
print("Hello There")
print(" ")
print("Welcome to my United States Covid-19 statistical analysis program")
print(" ")

# which state?
#state = input("What state would you like to see analyzed? ")

print(" ")
print("Good choice")
print(" ")
print("Displayed above is the comparison between confirmed cases and total deaths within your chosen American state throughout the month of April in the year of 2021...")

total_cases = []
total_deaths = []

x_list = [] 
y_list = []

for i in range(0,58): 
    

    # confirmed cases
    x_list.append(data_list[i][5])

    # deaths
    y_list.append(data_list[i][6])

    total_cases.append(x_list)
    total_deaths.append(y_list)

#print(total_cases)
#print(total_deaths)

#days_list = [j for j in ]

#all_cases = [527513, 68002, 0, 861653, 335529, 3740038, 509194, 338447, 104038, 49, 47614, 2228212, 1098723, 103, 7959, 33659, 187479, 1331747, 718948, 364486, 310014, 443408, 457896, 60945, 446459, 687638, 932604, 573938, 311654, 590973, 108663, 219559, 314928, 94676, 995365, 197447, 2044345, 967521, 107298, 164, 1070771, 447931, 183830, 1148121, 131437, 147897, 577550, 122532, 846472, 2890257, 396985, 22824, 3093, 658341, 401718, 152733, 659600, 58069]

#all_deaths = [10887, 347, 0, 17305, 5735, 61672, 6284, 8084, 1624, 0, 1105, 35084, 20158, 3, 136, 483, 2045, 24252, 13324, 5931, 4979, 6497, 10376, 782, 8718, 17594, 18716, 7221, 7195, 9132, 1570, 2243, 5459, 1301, 25529, 4058, 52209, 12631, 1522, 2, 19495, 6788, 2491, 26160, 2303, 2669, 9495, 1962, 12188, 50164, 2197, 246, 27, 10751, 5487, 2674, 7542, 707]

# x axis values
#x = all_cases
# corresponding y axis values
#y = all_deaths

#plt.plot(days_list, y)
  
# naming the x axis
plt.xlabel("total confirmed cases", fontsize=9)

# naming the y axis
plt.ylabel("total deaths", fontsize=9)

#title
plt.title("Total Cases Compared to Total Deaths in Chosen State", fontsize=14)

#plt.plot(range(0,10000))

#plt.show()

x1_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30]
y1_list = []
for i in range(0,len(x1_list)):

  y1_list.append(want_data[i][0][1])


plt.plot(x1_list,y1_list)

plt.show()