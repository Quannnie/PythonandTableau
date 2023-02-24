# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:59:18 2023

@author: Quang
"""

import pandas as pd


#reading .xlsx file
data = pd.read_excel('articles.xlsx')
data.info()
'''
0   article_id                       10437 non-null  int64: id của bài báo
1   source_id                        10437 non-null  object: id của nhà xuất bản
2   source_name                      10437 non-null  object: tên nhà xuất bản
3   author                           9417 non-null   object: tên tác giả
4   title                            10435 non-null  object: tên bài báo
5   description                      10413 non-null  object: mô tả bài báo
6   url                              10436 non-null  object: link của bài báo
7   url_to_image                     9781 non-null   object 
8   published_at                     10436 non-null  object: ngày giờ xuất bản
9   content                          9145 non-null   object: nội dung bài báo
10  top_article                      10435 non-null  float64: bài báo có là top_article hay không
11  engagement_reaction_count        10319 non-null  float64: số lượt thích, chia sẻ hay tương tác với bài báo
12  engagement_comment_count         10319 non-null  float64: số lượt bình luận
13  engagement_share_count           10319 non-null  float64: số lượng chia sẻ
14  engagement_comment_plugin_count  10319 non-null  float64: số lượt bình luận có tài khoản
'''


#sumary of data
data.describe()


#counting the number of articles by source
#format of groupby: df.groupby(['cloumn_to_group'])['cloumn_to_count'].count() or .sum()
data.groupby(['source_id'])['article_id'].count()
'''
source_id
1                             1
abc-news                   1139
al-jazeera-english          499
bbc-news                   1242
business-insider           1048
cbs-news                    952
cnn                        1132
espn                         82
newsweek                    539
reuters                    1252
the-irish-times            1232
the-new-york-times          986
the-wall-street-journal     333
Name: article_id, dtype: int64
'''

#number of reactions by publisher
data.groupby(['source_name'])['engagement_reaction_count'].sum()
'''
source_name
460.0                            0.0
ABC News                    343779.0
Al Jazeera English          140410.0
BBC News                    545396.0
Business Insider            216545.0
CBS News                    459741.0
CNN                        1218206.0
ESPN                             0.0
Newsweek                     93167.0
Reuters                      16963.0
The Irish Times              26838.0
The New York Times          790449.0
The Wall Street Journal      84124.0
Name: engagement_reaction_count, dtype: float64
'''

#dropping a column
data = data.drop(['engagement_comment_plugin_count' ], axis = 1)


#function in Python
def thisfunction ():
    print('this is my first function')
    
thisfunction()


#this is a function with variables
def aboutMe(name):
    print('This is '+name)
    return name

a= aboutMe('Quang')


def aboutMe(name, surname, location):
    print('This is '+name +  '. My surname is '+ surname+ '. I am from '+ location)
    return name, surname, location
a= aboutMe('Quang', 'Huynh', 'LA')

#using for loops in function
def favfood(food):
    for x in food:
        print ('Top food is '+ x)


fastfood = ['burgers','pizza','pie']
healthyfood = ['salad','water','fruit']
favfood(fastfood)
favfood(healthyfood)




# #creating a keyword flag
# keyword ='crash'

# #let create a for loop to isolate each titile row
# length = len(data)
# keyword_flag = []
# for x in range (0,length):
#     # tham chiếu đến cột 'title', hàng x
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)




#create a function
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range (0,length):
        # tham chiếu đến cột 'title', hàng x
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

kwf = keywordflag('murder')

#creating a new column in data dataframe
data['keyword_flag'] = pd.Series(kwf)
#create a column:
    #1. create a list
    #2. append object into list
    #3. data['name_of_column'] = pd.Series(name_of_list)


#playing around with classes
class Car:
    cartype = 'Automobile' #class atribute
    def __init__(self, name, make, color):
        self.carname = name #instance atribute
        self.carmake = make #instance atribute
        self.carcolor = color #instance atribute
mycar = Car('KIA','mercedes','black')

#for atribute in a class
carname = mycar.carname
carmake = mycar.carmake
carcolor = mycar.carcolor

#sentiment analysis installer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)
neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)
#đưa vào dataframe
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
#chuyển về series
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

#đưa series vào df
data['title_neg_sentiment'] =title_neg_sentiment 
data['title_pos_sentiment']=title_pos_sentiment 
data['title_neu_sentiment']=title_neu_sentiment 

#writing the data

data.to_excel('blogme_cleaned.xlsx', sheet_name='blogme_data', index = False)






        
    
        
        
