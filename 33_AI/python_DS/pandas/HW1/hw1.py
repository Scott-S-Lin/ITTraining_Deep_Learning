# Data Science Homework 1
# www.ittraining.com.tw
# coding: utf-8

import sys
import urllib.request
import matplotlib.pyplot as plt
src_file="hw1_data.csv"

try:
    data= open(src_file,'r')
except IOError:
	print('no such file and try to get file using HTTP get')
	urllib.request.urlretrieve("https://",src_file )
	data= open(src_file,'r')

lines=[]
DataSet=[]
for line in data:
    #print(line.strip().split(','))
	DataSet.append((line.strip().split(',')))

#detrmine class position (line number
allclass=['Education level','Average monthly income','Working environment']


def parse_data(DataSet,allclass,class_type):
    i=0
    nums_of_type=len(allclass)
    start=0
    end=0
    list=[]
    last_flag=0
    if nums_of_type==(class_type+1): #last type
        last_flag=1

    for row in DataSet:
        #print(i,':',row)
        if (last_flag==1):
            if row[0]==allclass[class_type]: 
                start=i+1
        else:
            if row[0]==allclass[class_type]:
                start=i+1
            if row[0]==allclass[class_type+1]:
                break

        i+=1
    end=i
	
    return start,end;
#-------------------------------------------
#define list operation         
#extract subset table from list
def list_subset(T,row_list,column_list):

    d=[]
    idx=0
    for i in row_list:
        d.append([])
        for j in column_list:
            d[idx].append(T[i][j])
            
        idx+=1
    return d
		
		
def get_data(DataSet,allclass,class_type,field):
    s,e=parse_data(DataSet,allclass,class_type)
    d=list_subset(DataSet,range(s,e),field)
    return d



def list_sub(list1,list2):
    return list(map(lambda x, y: x - y, list1, list2))


def list_add(list1,list2):
    return list(map(lambda x, y: x + y, list1, list2))

def list_div(list1,list2):
    return list(map(lambda x, y: x / y, list1, list2))

def list_multiply(list1,list2):
    return list(map(lambda x, y: x * y, list1, list2))
	
def list_round(list1,digit):
    return list(map(lambda x: round(x,digit),list1))

def get_one_column(T,cidx):
    res=[]
    t=list_subset(T,list(range(len(T))),[cidx])
    for row in t:
        for i in row:
            res.append(i)
    return res;
    
	
def list_to_float(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j]=float(M[i][j])
    return M;
	
	
def list_calculate(M):
    n_record=len(M)
    p=[100]*n_record
    #print(len(M[0]))
    f1=get_one_column(M,0)  #male population
    f2=get_one_column(M,1) #male smoke percentage
    f3=get_one_column(M,2)  #female population
    f4=get_one_column(M,3)  #female smoke percentage
    a=list_round(list_div((list_multiply(f1,f2)),p),1)
    b=list_round(list_div((list_multiply(f3,f4)),p),1)
    total=list_round(list_add(a,b),1)
    percent=list_round(list_multiply(list_div(total,list_add(f1,f3)),p),1)
    return percent	



def plot_bar_chart(data_set,x_label,total,X_title):
  
    means_frank = get_one_column(data_set,1)
    means_guido = get_one_column(data_set,3)
    means_total =total
    print(means_total)
    n_groups = len(x_label)



    # create plot
    # set figure size.you can comment it out for auto re-size
    plt.figure(figsize=(10,6))
    #index =  np.arange(0, 2*n_groups, 2)
    index=range(0,2*n_groups,2)
    bar_width = [0.5]*len(index)
    opacity = 0.8


    #matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
    rects1 = plt.bar(index, means_frank, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Male',align="center")

    rects2 = plt.bar(list_add(index,bar_width), means_guido, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Female',align="center")
    rects3 = plt.bar(list_add(index,list_multiply(bar_width,[2]*len(index))), means_total, bar_width,
                     alpha=opacity,
                     color='y',
                     label='total',align="center")

    plt.xlabel(X_title)
    plt.ylabel('Smoking percentag (%)')
    plt.title('Smoking percentage vs '+X_title, y = 1.02)
    asex = plt.gca()
    asex.set_ylim(0, 55)
    plt.xticks(list_add(index,bar_width), x_label)
    plt.legend()

    plt.tight_layout()
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    plt.show()

    
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%4.1f' % height,
                ha='center', va='bottom')
        
        
        


# In[113]:


def plot_line_chart(data_set,x_label,total,X_title):
    # data to plot
    means_frank = get_one_column(data_set,1)
    means_guido = get_one_column(data_set,3)
    means_total =total
    print(means_total)
    n_groups = len(x_label)
    # create plot
    # set figure size.you can comment it out for auto re-size
    plt.figure(figsize=(10,6))
    #index = np.arange(n_groups)
    index=list(range(n_groups))
    bar_width = [0.3]*len(index)
    opacity = 0.8


    #matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
    line1 = plt.plot(list_add(index,bar_width), means_frank,
                     alpha=opacity,
                     color='b', marker='o', linestyle='solid',
                     label='Male')
    
    for i,j in list(zip(range(0,n_groups),means_frank)):
        plt.text(float(i) + 0.235,float(j) + 2.35,j,fontsize=12)
        
    line2 = plt.plot(list_add(index,bar_width), means_guido, 
                     alpha=opacity,
                     color='g', marker='o', linestyle='solid',
                     label='Female')

    for i,j in list(zip(range(0,n_groups),means_guido)):
        plt.text(float(i) + 0.235,float(j) + 2.35,j,fontsize=12)
        
    line3 = plt.plot(list_add(index,bar_width), means_total, 
                     alpha=opacity,
                     color='y', marker='o', linestyle='solid',
                     label='Total')
    for i,j in list(zip(range(0,n_groups),means_total)):
        plt.text(float(i) + 0.235,float(j) + 2.35,j,fontsize=12)
        
     
    plt.xlabel(X_title)
    plt.ylabel('Smoking percentag (%)')
    plt.title('Smoking percentage vs '+X_title, y = 1.04)
    asex = plt.gca()
    asex.set_ylim(0, 55)
    plt.xticks(index + bar_width, x_label)
    plt.legend()
     
    plt.tight_layout()

    plt.show()



def plot_pie_chart(data_set,x_label,total,X_title):
    print(data_set)
    #調節圖形大小，寬，高
    plt.figure(figsize=(6.5,6.8))

   # data to plot
    #mP = np.array(data_set[:,1]).astype('float')
    #msP = np.array(data_set[:,2]).astype('float')
    #fP = np.array(data_set[:,3]).astype('float')
    #fsP = np.array(data_set[:,4]).astype('float')

    mP = get_one_column(data_set,0)
    msP =get_one_column(data_set,1)
    fP = get_one_column(data_set,2)
    fsP =get_one_column(data_set,3)
    #print(mP,msP,fP,fsP,x_label)
    n_groups = len(x_label)

    #定義餅狀圖的標籤，標籤是列表
    labels = x_label
    n_record=len(mP)
    vec_1=[1]*n_record
    vec_100=[100]*n_record
    
    a=list_round(list_multiply(mP,list_sub(vec_1,list_div(msP,vec_100))),0)
    b=list_round(list_multiply(fP,list_sub(vec_1,list_div(fsP,vec_100))),0)

    vec_total=list_add(a,b)
    #vec_total = np.round(mP * ( 1 - (msP / 100)),0) + np.round(fP * ( 1 - (fsP / 100)),0)

	
	
    #print(means_frank, vec_total)
    #每個標籤占多大，會自動去算百分比
    sizes = vec_total
    colors = colors = ['orange','red','yellowgreen','lightskyblue','purple','yellow']
    #將某部分爆炸出來， 使用括弧，將最大的一塊塊分割出來，數值的大小是分割出來的與其他兩塊的間隙
    #print(vec_total.index(max(vec_total)))
    #expList = [0,0,0,0,0]
    #expList[vec_total.index(max(vec_total))] = 0.05
    #explode = expList

    #patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
    
    patches,l_text,p_text = plt.pie(sizes,labels=labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                    startangle = 90,pctdistance = 0.6)

    #labeldistance，文本的位置離遠點有多遠，1.1指1.1倍半徑的位置
    #autopct，圓裡面的文本格式，%3.1f%%表示小數有三位元，整數有一位元的浮點數
    #shadow，餅是否有陰影
    #startangle，起始角度，0，表示從0開始逆時針轉，為第一塊。一般選擇從90度開始比較好看
    #pctdistance，百分比的text離圓心的距離
    #patches, l_texts, p_texts，為了得到圓形圖的返回值，p_texts圓形圖內部文本的，l_texts圓形圖外label的文本

    #改變文本的大小
    #方法是把每一個text遍歷。調用set_size方法設置它的屬性
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    # 設置x，y軸刻度一致，這樣圓形圖才能是圓的
    plt.axis('equal')
    plt.title('Proportion of different of '+X_title+' in non-smoking population')
    #plt.legend()
    plt.show()


# In[115]:


num_arg=len(sys.argv)
print(sys.argv,num_arg)

arg_class=['E','A','W','e','a','w']
arg_chart=['l','b','p']

def process_arg(arg):
	# '-Wp'
	class_type=-1
	chart_type=-1
	
	if len(arg)!=3:
		show_help()
	
	n=-1
	try:
		n=arg.index('-')
	except ValueError:
		show_help()
	finally:
		if n!=0: show_help()  # measn starting '-'

	if arg[1] in arg_class:
		class_type=arg[1]
	if arg[2] in arg_chart:
		chart_type=arg[2]

	if class_type==-1 or chart_type==-1:
		show_help()
	return class_type,chart_type

def show_help():
	print("Usage:"+sys.argv[0]+" -[E|A|W]"+"[l|b|p]")
	sys.exit(-1)


if len(sys.argv)<=1:
	show_help()

#write for loop to scan legal command line argument

for num in range(1,num_arg):
	arg_str=sys.argv[num]
	class_type,chart_type=process_arg(arg_str)

	if class_type.upper() == 'E':
		class_type=0
	elif class_type.upper() == 'A':
		class_type=1
	elif class_type.upper() == 'W':
		class_type=2
	else:
		pass

	X=get_data(DataSet,allclass,class_type,[0,1,2,3,4])
	title=get_one_column(X,0)
	DATA=list_to_float(list_subset(X,list(range(len(X))),list(range(1,len(X[0]))))) # except for column 0
	total_per=list_calculate(DATA)

	if chart_type=='l':
		plot_line_chart(DATA,title,total_per,allclass[class_type])
	elif chart_type=='b':
		plot_bar_chart(DATA,title,total_per,allclass[class_type])
	elif chart_type=='p':
		plot_pie_chart(DATA,title,total_per,allclass[class_type])
	else:
		pass

