# Covid-19 Sentiment Analysis on Large-Scale Covid-19 Tweets using NLP and Deep Learning

## Fine-grained Sentiment Analysis on Large-Scale Covid-19 Tweets using Hybrid Convolutional LSTM Based on Naïve Bayes Sentiment Modeling


### Abstract

Millions of lives were affected rapidly throughout the world when the Covid-19 outbreak spread by leaps and bounds. During this catastrophic period, people used to express their condolence as well as emotions through different social networks. In order to analyze the public comments on Twitter, an experimental approach is developed based on popular words regarding this pandemic. In this paper, various NLP-based research works are discussed on sentiment analysis, trend prediction, topic modeling, learning mechanisms, etc. Furthermore, the hybrid deep learning models are developed based on the Naïve Bayes sentiment model to predict the sentiment from the collected huge number of Coronavirus-related tweets. After performing the n-gram analysis, the Covid-19 specific words are extracted based on their popularity. The public sentiment trend has been analyzed using the extracted topics related to Covid-19 and the tweets are classified according to their sentiment scores. The distinguished sentiment ratings are assigned to the collected tweets based on their sentiment class. Then **Convo-Sequential** and **Convo-Bidirectional** long-short term networks are trained using fine-grained sentiment-rated tweets to categorize Covid-19 tweets into five different sentiment classes. Finally, our proposed Convo-Sequential and Convo-Bidirectional LSTM models achieved **84.52%** and **85.03%** of validation accuracy respectively for the first phase dataset whereas using the second phase dataset the models obtained the validation accuracy of **86.58%** and **87.22%** respectively.

## Project Workflow
Here, the proposed system architecture of the project is presented.

![](https://github.com/ArunavaKumar/Covid-19_Fine-grained_Sentiment_Analysis/blob/main/Images/Proposed%20Methodology.png)
                                 
### Important Note

#### Please use Winrar or any rar extractor to extract these rar files containing the First and Second phased datasets with pre-processed and sentiment rated tweets. 


### Data Collection

I streamed live tweets from the twitter after WHO declared Covid-19 as a pandemic. Since this Covid-19 epidemic has affected the entire world, I collected worldwide Covid-19 related English tweets at a rate of almost 10k per day in two phases starting from **August-October, 2020** and **April-June, 2021**. I prepared the first phase dataset of about **489k** tweets collected from **20th August to 20th October 2020**. After one month I again start collecting tweets from the twitter as on that time the pandemic was spreading with its fatal intensity. I collected almost **320k** tweets in the period **April 26 to June 27, 2021** for the second phase dataset.

The datasets areavailable in my [Kaggle](https://www.kaggle.com/datasets/arunavakrchakraborty/covid19-twitter-dataset) data repository.


#### Content

The datasets I developed contains the important information about most of the tweets as their attributes. The main attributes of both of these datasets are: 
- Tweet ID
- Creation Date & Time
- Source Link
- Original Tweet
- Favorite Count
- Retweet Count
- Original Author
- Hashtags
- User Mentions
- Place

Finally, I collected **3,20,316** tweets for first phase dataset and **4,89,269** tweets for second phase dataset containing the hash-tagged keywords like - `#covid-19`, `#coronavirus`, `#pandemic`, `#covid`, `#lockdown`, `#homequarantine`, `#quarantinecenter`, `#socialdistancing`, `#stayhome`, `#staysafe` etc. Here I represented an overview of the collected dataset.


#### Data Pre-Processing

I pre-processed these collected data by developing a user defined pre-processing function based on NLTK (Natural Language Toolkit, a Python library for NLP). In the first phase it converts all the tweets into lower case. Then it removes all extra white spaces, numbers, special characters, ASCII characters, URLs, punctuations & stop words from the tweets. Then it converts all ‘covid’ words into ‘covid19’ as we already removed all numbers from the tweets. Using stemming the pre-processing function has reduced inflected words to their word stem.


#### Sentiment Analysis

I calculated the sentiment polarity of each cleaned and pre-processed tweet using the NLTK based Sentiment Analyzer and get the sentiment scores for positive, negative and neutral categories to calculate the compound sentiment score for each tweet. I classified the tweets on the basis of the compound sentiment scores into three different classes i.e., Positive, Negative and Neutral. Then we assigned the sentiment polarity ratings for each polar(positive abd negative) tweet based on the following algorithm-

**Fine-grained Sentiment Classification Algorithm:**

![](https://github.com/ArunavaKumar/Covid-19_Fine-grained_Sentiment_Analysis/blob/main/Images/Fine-grained%20Classification.png)


#### Proposed Hybrid Convolutional LSTM model

![](https://github.com/ArunavaKumar/Covid-19_Fine-grained_Sentiment_Analysis/blob/main/Images/CNN%2BLSTM.png)

### Experimental Setup

This project was done with the following experimental setup:

⦁ **Hardware Configuration -** 
    - Processor: Intel Core i7-10750H Processor
    - Primary Memory: 16GB RAM
    - Secondary Memory: 1TB SSD
    - Graphics: Nvidia RTX 2060 6GB GPU
    - Operating System: Windows 10 Home Edition

⦁ **Software Configuration -** 
    - Programming Language: Python (3.7.3)
    - IDE: Jupyter Notebook, MS Visual Studio Code, Notepad++
    - H/W Acceleration Driver: Nvidia Graphics Driver, Nvidia CUDA Development Toolkit 11.2, Nvidia cuDNN 11.2 64-bit
    - Browser: Microsoft Edge, Google Chrome, Mozilla Firefox, Google Colaboratory, IBM Watson Studio

⦁ **Python Packages -** 
    - beautifulsoup4 == 4.7.1
    - dash == 1.19.0
    - gensim == 3.8.3
    - keras == 2.4.3
    - Markdown == 3.3.4
    - matplotlib == 3.1.0
    - nltk == 3.4.4
    - numpy == 1.16.4
    - pandas == 1.0.3
    - plotly == 4.14.3
    - preprocessor == 1.1.3
    - seaborn == 0.9.0
    - scikit-learn == 0.24.1
    - sklearn == 0.0
    - tensorflow == 2.4.0
    - tensorflow-gpu == 2.4.0
    - text2vec == 0.1.6
    - tweepy == 3.10.0
    - tweet-preprocessor == 0.5.0
    - wordcloud == 1.8.1

*The performance and effectiveness of the codes during the runtime may vary due to any changes in these versions of the following applications and python packages.*


### Important Note

In this repository I provided the Covid-19 datasets (both Phase I and Phase II) along with all the important source codes and respective outputs for my entire project work. The repository contains-
- The Covid-19 datasets (both Phase I and Phase II) in rar format.
- The python file `TweetStream.py` can be used for featching live tweets on Covid-19 as well as on any topic.
- In the `Output Figures` directory, I presented all the outputs from the experimentation on both of the Covid-19 datasets.
- The `Covid-19 Sentiment Analysis v3.0 (Part I).ipynb` and `Covid-19 Sentiment Analysis v3.0 (Part II).ipynb` jupyter notebooks represent entire analysis for both datasets.

*The MS Visual Studio Code or Notepad++ can be used to open the source codes for better visibility.*


### Acknowledgements

- I would like to express humbly my absolute amenity and heartfelt gratitude to **Dr. Dipankar Das** (Assistant Professor, Department of Computer Science and Engineering, Jadavpur University) and **Dr. Anup Kumar Kolya** (Assistant Professor, Department of Computer Science and Engineering, RCC Institute of Information Technology) who supported me throughout this research journey.


The research work is part of the publication entitled:

**Chakraborty, A. K., Das, D., & Kolya, A. K. (2023). Sentiment Analysis on Large-Scale Covid-19 Tweets using Hybrid Convolutional LSTM Based on Naïve Bayes Sentiment Modeling. ECTI Transactions on Computer and Information Technology, 17(3), 343–357. https://doi.org/10.37936/ecti-cit.2023173.252549**


#### - By Arunava Kumar Chakraborty
