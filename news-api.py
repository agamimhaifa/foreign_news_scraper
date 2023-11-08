from newsapi import NewsApiClient
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')
Previous_Date = datetime.today() - timedelta(days=1)

# Init
newsapi = NewsApiClient(api_key='dc3d0bad23ca4f759b84181bf3f00941')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                          sources='bbc-news,the-verge',
#                                          category='business',
#                                          language='en',
#                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param=Previous_Date,
                                      to=today,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()