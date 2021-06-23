# Covid-19 Sentiment Analysis on Large-Scale Covid-19 Tweets using NLP and Deep Learning


## Sentiment Analysis on Large-Scale Covid-19 Tweets using Hybrid Convolutional LSTM Based on Naïve Bayes Sentiment Modelling




### Important Note

#### Please use Winrar or any rar extractor to extract these rar files containing the First and Second phased datasets with pre-processed and sentiment rated tweets. 


### Data Collection

I streamed live tweets from the twitter after WHO declared Covid-19 as a pandemic. Since this Covid-19 epidemic has affected the entire world, I collected worldwide Covid-19 related English tweets at a rate of almost 10k per day in two phases starting from **April-June, 2020** and **August-October, 2020**. I prepared the first phase dataset of about **235k** tweets collected from **19th April to 20th June, 2020**. After one month I again start collecting tweets from the twitter as on that time the pandemic was spreading with its fatal intensity. I collected almost **320k** tweets in the period **August 20 to October 20, 2020** for the second phase dataset.


### Content

The datasets I developed contains the important information about most of the tweets as their attributes. The main attributes of both of these datasets are: 
- **Tweet ID**
- **Creation Date & Time**
- **Source Link**
- **Original Tweet**
- **Favorite Count**
- **Retweet Count**
- **Original Author**
- **Hashtags**
- **User Mentions**
- **Place**

Finally, I collected **2,35,240** tweets for first phase dataset and **3,20,316** tweets for second phase dataset containing the hash-tagged keywords like - ***#covid-19***, ***#coronavirus***, ***#covid***, ***#covaccine***, ***#lockdown***, ***#homequarantine***, ***#quarantinecenter***, ***#socialdistancing***, ***#stayhome***, ***#staysafe*** etc. Here I represented an overview of the collected dataset.


### Data Pre-Processing

I pre-processed these collected data by developing a user defined pre-processing function based on NLTK (Natural Language Toolkit, a Python library for NLP). In the first phase it converts all the tweets into lower case. Then it removes all extra white spaces, numbers, special characters, ASCII characters, URLs, punctuations & stop words from the tweets. Then it converts all ‘covid’ words into ‘covid19’ as we already removed all numbers from the tweets. Using stemming the pre-processing function has reduced inflected words to their word stem.

### Sentiment Analysis

I calculated the sentiment polarity of each cleaned and pre-processed tweet using the NLTK based Sentiment Analyzer and get the sentiment scores for positive, negative and neutral categories to calculate the compound sentiment score for each tweet. I classified the tweets on the basis of the compound sentiment scores into three different classes i.e., Positive, Negative and Neutral. Then we assigned the sentiment polarity ratings for each tweet based on the following algorithm-

**Algorithm Sentiment Classification of Tweets (compound, sentiment):**
1. *for each tweet in dataset:*
2. *if tweet[compound] &lt; 0:*
3. *tweet[sentiment] = 0.0*        # assigned 0.0 for Negative Tweets
4. *elif tweet[compound] &gt; 0:*
5. *tweet[sentiment] = 1.0*        # assigned 1.0 for Positive Tweets
6. *else:*
7. *tweet[sentiment] = 0.5*        # assigned 0.5 for Neutral Tweets
8. *end*


### Experimental Setup

This project was done with the following experimental setup:

⦁ **Hardware Configuration -** Intel Core i7-10750H Processor, 16GB RAM, 1TB SSD, Nvidia RTX 2060 6GB GPU, Windows 10 Home Edition Operating System.

⦁ **Software Configuration -** Python (3.7.3) Programming Language, Anaconda, MS Visual Studio Code, Notepad++, Nvidia Graphics Driver, Nvidia CUDA Development Toolkit 11.2, Nvidia cuDNN 11.2 64-bit, Microsoft Edge, Google Chrome, Mozilla Firefox, Google Colaboratory, IBM Watson Studio

⦁ **Python Packages -** beautifulsoup4 == 4.7.1, bokeh == 1.2.0, dash == 1.19.0, en-core-web-sm == 3.0.0, gensim == 3.8.3, image == 1.5.33, keras == 2.4.3, Markdown == 3.3.4, matplotlib == 3.1.0, nltk == 3.4.4, numpy == 1.16.4, pandas == 1.0.3, plotly == 4.14.3, preprocessor == 1.1.3, seaborn == 0.9.0, scikit-learn == 0.24.1, sklearn == 0.0, spacy == 3.0.3, tensorflow == 2.4.0, tensorflow-gpu == 2.4.0, text2vec == 0.1.6, textblob == 0.15.3, tqdm == 4.58.0, tweepy == 3.10.0, tweet-preprocessor == 0.5.0, Unidecode == 1.2.0, vaderSentiment == 3.3.2, wordcloud == 1.8.1.

*The performance and effectiveness of the codes during the runtime may vary due to any changes in these versions of the following applications and python packages.*


### Important Note

In this repository I provided the Covid-19 datasets (both Phase I and Phase II) along with all the important source codes and respective outputs for my entire project work. The repository contains-
- The Covid-19 datasets (both Phase I and Phase II) in rar format.
- The python file **TweetStream.py** can be used for featching live tweets on Covid-19 as well as on any topic.
- In the **Covid-19 Sentiment Analysis v2.0** directory, I have presented my through experimentation on a sample Covid-19 dataset (Simmilar as the main datasets).
- In the **Oprimized Outputs** directory, I have presented all the outputs ffrom the experimentation on both of the Covid-19 datasets.

*Please use WinRar or any other Rar extracting softeare to extract the files for the datasets. The MS Visual Studio Code or Notepad++ can be used to open the source codes for better visibility.*


### Acknowledgements

I wouldn't be here without the help of my project guide **Dr. Anup Kumar Kolya**, *Assistant Professor*, *Dept of Computer Science and Engineering*, *RCCIIT* whose kind and valuable suggestions and excellent guidance enlightened to give me the best opportunity in preparing these datasets. If you owe any attributions or thanks, include him here along with any citations of past research.


The first phase dataset (Covid-19 Dataset I) is part of the publication entitled:

**Chakraborty A.K., Das S., Kolya A.K. (2021) Sentiment Analysis of Covid-19 Tweets Using Evolutionary Classification-Based LSTM Model. In: Pan I., Mukherjee A., Piuri V. (eds) Proceedings of Research and Applications in Artificial Intelligence. Advances in Intelligent Systems and Computing, vol 1355. Springer, Singapore. https://doi.org/10.1007/978-981-16-1543-6_7**


#### - By Arunava Kumar Chakraborty
