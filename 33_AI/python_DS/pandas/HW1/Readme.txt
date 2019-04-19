# Data Science Homework 1

#----------------
# How to Execute
#------------------
python3 hw1.py

Usage:hw1.py -[E|A|W][l|b|p]

Example:
python3 hw1.py -El -Ab -Wp

Note:
Before running, you may need to do
sudo apt-get install python3-tk
pip install matplotlib

#----------------
# Readme
#------------------

Step1: parse command line argument
	process_arg(arg)
	show_help() if the format of input argument is illegal
	Usage:hw1.py -[E|A|W][l|b|p]
 
Step2: get .csv file and save file using URLlib
	FileName:"hw1_data.csv"

Step3:parse .csv file and add to list
	get_data() and parse_data()

Step4: Calculate data using list operation
	data manipulation using some self-defined functions,because Numpy is not allowd

Step5: Prepare data to plot 
	plot_bar_chart
	plot_line_chart()
	plot_pie_chart()
   
   
#----------------
# function list in hw1.py
#------------------
def show_help():

#--- Array list manipulation using list---

def parse_data(DataSet,allclass,class_type):
def get_data(DataSet,allclass,class_type,field):

#--- Array list manipulation ---
def list_subset(T,row_list,column_list):
def list_sub(list1,list2):
def list_add(list1,list2):
def list_div(list1,list2):
def list_multiply(list1,list2):
def list_round(list1,digit):
def get_one_column(T,cidx):
def list_to_float(M):
def list_calculate(M):
#---Plot Chart --------
def plot_bar_chart(data_set,x_label,total,X_title):
def autolabel(rects):
def plot_line_chart(data_set,x_label,total,X_title):
def plot_pie_chart(data_set,x_label,total,X_title):
def process_arg(arg):




