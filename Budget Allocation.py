import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def menu():
    print('\n___________________________________________________________________________\n>>> B U D G E T   A L L O C A T I O N   F O R   P A S T   5   Y E A R S <<<\n___________________________________________________________________________\n \n**Press 1 for budget allocated to each ministry\n**Press 2 for total expenditures for 5 years\n**Press 3 for miscellaneous expenditures\n'.center(100))
    #print(' **Press 1 for budget allocated to each ministry'.center(50))  # use csv file
    #print('**Press 2 for total expenditures for 5 years\n'.center(50))  # sum of each year


u=0
listdef = [4.59, 4.78, 4.96, 5.03, 5.76]
listagr = [1.01, 1.09, 1.16, 1.21, 1.38]
listdef1 = pd.Series([4.59, 4.78, 4.96, 5.03, 5.76])
listagr2 = pd.Series([1.01, 1.09, 1.16, 1.21, 1.38])
ser = [listagr2 + listdef1]

#g = pd.Series(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'])

def conti():
    t=int(input('Would you like to continue....................?\n\nPress 1 to continue\nPress 2 to exit\nEnter your choice:'))
    if(t==1):
        label()    
    else:
        print('\n___________________________________________________________________________\n>>> T H A N K S      F O R       U S I N G <<<\n___________________________________________________________________________\n \n')
        quit()
        
        
def linechartd():
    
    plt.ylabel('Budget(in lakh crores)')
    plt.xlabel('Years')
    plt.title('Defence spending')
    plt.plot(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], listagr, color='b')
    plt.show()
    
def barchartd():
    plt.ylabel('Budget(in lakh crores)')
    plt.xlabel('Years')
    plt.title('Defence spending')
    plt.bar(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], listagr, color='b')
    plt.show()


def linecharta():
    plt.ylabel('Budget(in lakh crores)')
    plt.xlabel('Years')
    plt.title('Agricultural spending')
    plt.plot(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], listagr, color='b')
    plt.show()


def barcharta():
    plt.ylabel('Budget(inlakh crores)')
    plt.xlabel('Years')
    plt.title('Agricultural spending')
    plt.bar(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], listagr, color='b')
    plt.show()


def miod():
    c = int(input('___________________________________________________________________________\n \n**For Line chart >>> Press 1 \n**For Bar chart  >>> Press 2\n \nEnter your choice:  '))
    if c == 1:
        linechartd()
    elif c == 2:
        barchartd()


def mioa():
    c = int(input('___________________________________________________________________________\n \n**For Line chart >>> Press 1 \n**For Bar chart  >>> Press 2\n \nEnter your choice:  '))
    if c == 1:
        linecharta()
    else:
        barcharta()

def misc():
     agrisub=[1.15,1.38,1.34,1.45,1.31]
     foraid=[1.23,1.58,1.96,2.14,2.58]
     c = int(input('___________________________________________________________________________\n \n**For Line chart >>> Press 1 \n**For Bar chart  >>> Press 2\n \nEnter your choice:  '))
     if c==1:
         plt.plot(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], agrisub, color='b',label='Subsidies for agriculture')
         plt.plot(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], foraid, color='g',label='Foreign aid distributed')
         plt.legend(loc='upper left')
         plt.title('Miscellaneous spendings')
         plt.xlabel('Years')
         plt.ylabel('Budget(in lakh crores)')
         plt.show()
     elif c==2:
         x=range(5)
         plt.bar([0,1,2,3,4], agrisub, color='b',label='Subsidies for agriculture',width=0.2)
         plt.bar([0.2,1.2,2.2,3.2,4.2], foraid, color='g',label='Foreign aid distributed',width=0.2)
         plt.xticks(x,['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'])
         plt.legend(loc='upper left')
         plt.title('Miscellaneous spendings')
         plt.xlabel('Years')
         plt.ylabel('Budget(in lakh crores)')
         plt.show() 
def label():
    menu()
    d = int(input("Enter your choice:  "))
    if d == 1:
        print('___________________________________________________________________________\n \n**For budget information of Ministry of Defence     >>> Press 1\n**For budget information of Ministry of Agriculture >>> Press 2'.center(
                100))
        a = int(input('\nEnter your choice:  '))
        if a == 1:
            miod()
            conti()
        elif a == 2:
            mioa()
            conti()
    elif d == 2:
        plt.xlabel('Years')
        plt.ylabel('Budget(in lakh crores)')
        plt.plot(['2017-18', '2018-19', '2019-20', '2020-21', '2021-22'], [5.60, 5.87, 6.12, 6.24, 7.14])
        plt.title('Cumulative spending')
        plt.show()
        conti()
    elif d==3:
        misc()
        conti()
label()
