from newsapi import NewsApiClient
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')
Previous_Date = datetime.today() - timedelta(days=1)

# Init
#newsapi = NewsApiClient(api_key='dc3d0bad23ca4f759b84181bf3f00941')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                          sources='bbc-news,the-verge',
#                                          category='business',
#                                          language='en',
#                                          country='us')

# /v2/everything
#all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param=Previous_Date,
#                                      to=today,
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)

# /v2/top-headlines/sources
#sources = newsapi.get_sources()

# Initialize the NewsApiClient with your API key
newsapi = NewsApiClient(api_key='dc3d0bad23ca4f759b84181bf3f00941')

# Set your parameters for the news query
country = 'il'        # Country (e.g., 'US' for United States)
category = 'technology'  # Category (e.g., 'technology')

# Fetch top headlines
#top_headlines = newsapi.get_top_headlines(country=country, category=category)


# Set your parameters for the news query
query = 'Gaza'  # Search query for "Middle East"
language = 'en'        # Language (e.g., 'en' for English)
source = 'al-jazeera-english'  # News source (Al Jazeera English)

# Set the number of results to 10
page_size = 10

# Fetch top headlines with the specified query
top_headlines = newsapi.get_everything(q=query, language=language, sources=source, sort_by='publishedAt', page_size=page_size)

if 'articles' in top_headlines:
    for article in top_headlines['articles']:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print("\n")
else:
    print("No articles found")