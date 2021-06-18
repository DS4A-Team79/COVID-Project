import os
import numpy as np # linear algebra
import pandas as pd # data processing, I/O
import matplotlib.pyplot as plt # plotting
from tsmoothie.smoother import LowessSmoother # smoothing

smoother = LowessSmoother(smooth_fraction=0.1, iterations=1)
data = pd.read_csv("./time_series_covid_19_confirmed_US.csv")
byState = data.groupby("Province_State").sum()

location_set = byState.iloc[:,0:5]
case_set = byState.iloc[:,5:]
t_case_set = case_set.transpose()

## Write loop that creates a new folder for every state and puts the
## raw time series, the differenced time series and the smoothed time series along with thier data

# define the name of the directory to be created
states_dir = "./States"
try:
    os.mkdir(states_dir)
except OSError:
    print ("Creation of the directory %s failed" % states_dir)
else:
    print ("Successfully created the directory %s " % states_dir)

for case in t_case_set:

	path = f"./States/{case}"
	try:
	    os.mkdir(path)
	except OSError:
	    print ("Creation of the directory %s failed" % path)
	else:
	    print ("Successfully created the directory %s " % path)

	# writes raw data to csv 
	t_case_set[case].to_csv(f'./States/{case}/{case}_raw.csv', index = True)

	# writes raw plot to csv
	plt.rc('font', size=24)
	fig, ax = plt.subplots(figsize=(30, 30))
	plt.plot(case_set.transpose()[case],linewidth=5)
	plt.xlabel("Dates")
	plt.ylabel("Total Cases")
	plt.title(f"Cumulative distribution of COVID cases in {case}")
	plt.savefig(f'./States/{case}/{case}_cumcases_plot.png')	

	#writes diff'd ts to csv
	t_case_set[case].diff().to_csv(f'./States/{case}/{case}_diff.csv', index = True)
	plt.rc('font', size=24)
	fig, ax = plt.subplots(figsize=(30, 30))
	plt.plot(case_set.transpose().diff()[case],linewidth=5)
	plt.xlabel("Dates")
	plt.ylabel("Cases")
	plt.title(f"Distribution of new COVID cases per day in {case}")
	plt.savefig(f'./States/{case}/{case}_newcases_plot.png')	

	#writes LOWESS smoothed ts to csv
	smooth_array=smoother.smooth(t_case_set[case].diff().dropna()).smooth_data
	pd.DataFrame(smooth_array).to_csv(f'./States/{case}/{case}_smooth.csv', index = True)
	plt.rc('font', size=24)
	fig, ax = plt.subplots(figsize=(30, 30))
	for point in smooth_array:
		plt.plot(point, linewidth=5)
	plt.xlabel("Dates")
	plt.ylabel("Cases")
	plt.title(f"Locally Regressed Distribution of new COVID cases per day in {case}")
	plt.savefig(f'./States/{case}/{case}_smooth_plot.png')	
