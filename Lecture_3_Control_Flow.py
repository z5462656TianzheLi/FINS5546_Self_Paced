"""Docstring for this module(Lecture_3_Control_Flow).

This module is mainly for self_paced learning. of FINS5546 Lecture_2 content."""
#happy = True
#very_happy = True
#if happy is True:
#    print('\tI am really happy')
#    if very_happy is True:
#        print('\t\tI am really very happy')
#print('This will be printed regardless of True or False')

#b = False
#if b is True:
#    print('b is True')
#else:
#    print('b is False')

#x = 1
#y= 1
#if x > 0 and y > 0:
#    pass
#elif x == 0 and y == 0:
#    pass
#else:
#    pass

#import yfinance as yf

#tic = ['QAN.AX','WES.AX']
#start_date = '2019-01-01'
#end_date = None

#for tics in tic:
#    df = yf.download(tics, start_date, end_date)
#    tic_base = tics.split('.')[0].lower()
#    print(tic_base)
#    print(df)
    #df.to_csv('{}_stock_price.csv'.format(tic_base))

#d = {
#    "beauty": True,
#    "truth": True,
#    "red wheelbarrow": 100000,
#    5: "fingers",
#    }

#for values in d.values():
    #print(values)

#for pairs in d.items():
    #print('\n')
    #print(pairs)
    #unpacking
    #key,value = pairs
    #print('KEY = {}, VALUE = {}'.format(key,value))
    #direct unpacking
    #print('KEY = {}, VALUE ={}'.format(*pairs))
#print('\n')
#for i in range(5,0,-1):
#    print('Ignition in {} seconds...'.format(i))

#print('\nIgnite!')

#letters = ["a", "b", "c", "d", "e"]
#print('Letters = {}'.format(letters))
#i = 0
#x = 1.0
#for letter in letters:
#    print('Current letter {} = {}_{}'.format(x ,letters[i],i + 1))
#    i = i + 1
#    x = x + 1.0

#the_sum = 0
#i = 0
#for i in range(0,101,1):
#    the_sum = the_sum + 1
#    print('i is now {}, the_sum is now {}'.format(i,the_sum))
#while i <= 100:
#    the_sum = the_sum + 1
#    i = i + 1
#    print('i is now {}, the_sum is now {}'.format(i,the_sum))

#years = [2018, 2019, 2020]
#months = [
#    "Jan",
#    "Feb",
#    "Mar",
#    "Apr",
#    "May",
#    "Jun",
#    "Jul",
#    "Aug",
#    "Sep",
#    "Oct",
#    "Nov",
#    "Dec",
#    ]

#for year in years:
#    for month in months:
#        print('It is now {}.{}'.format(year,month))

#sun_of_evens = 0
#for i in range(0,101,1):
#    if i % 2 == 0:
#        continue
#    if i % 3 == 0:
#        continue
#    if i % 7 == 0:
#        continue
#    if i % 13  == 0:
#       continue
#    sun_of_evens = sun_of_evens + i
#    print(sun_of_evens)

#pairs = [
#  ('a', 1),
#  ('b', 2),
#  ('c', 3),
#]
#pair = ('a',1)
#a,b = pair
#print(a)

#遍历时解包
#for a,b in pairs:
#    print('KEY: {}, VALUE: {}'.format(a,b))

#even_sum = []
#for i in range(0,10000001):
#    if i % 2 == 0:
#        even_sum.append(i)
#print(even_sum[:10])

#even_sum = [x for x in range(0,1000001) if x % 2 == 0]
#print(even_sum[:10])

#pairs = [
# ('a', 1),
#  ('b', 2),
#  ('c', 3),
#  ]

#dic = {key : value for key, value in pairs}
#print(dic)

#dic = {'a': 1, 'b': 2, 'c': 3}
#pairs = [(key,value) for key,value in dic.items()]
#print(pairs)

#lst = []
#for i in range(0,101):
#    if i % 2 == 0:
#        lst.append(i)
#print(lst)

#lst = [x for x in range(0,101) if x % 2 == 0]
#print(lst)

#gen = (i for i in range(101))
#print(gen)

#x = 93848.3945126
#print(round(x,3))