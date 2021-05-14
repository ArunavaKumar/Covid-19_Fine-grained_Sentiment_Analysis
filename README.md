# Covid-19-Tweets-Dataset




### Important Note

#### Please use Winrar or any rar extractor to extract the rar file containing the First and Second phased datasets with pre-processed and sentiment rated tweets. 


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


### Acknowledgements

I wouldn't be here without the help of my project guide **Dr. Anup Kumar Kolya**, *Assistant Professor*, *Dept of Computer Science and Engineering*, *RCCIIT* whose kind and valuable suggestions and excellent guidance enlightened to give me the best opportunity in preparing these datasets. If you owe any attributions or thanks, include him here along with any citations of past research.
