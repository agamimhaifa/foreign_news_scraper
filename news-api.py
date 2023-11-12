from newsapi import NewsApiClient
from datetime import datetime, timedelta

DBG_PRINT_SOURCES = False #True

today = datetime.today().strftime('%Y-%m-%d')
Previous_Date = datetime.today() - timedelta(days=1)


# Initialize the NewsApiClient with agamimhaifas API key
newsapi = NewsApiClient(api_key='dc3d0bad23ca4f759b84181bf3f00941')

# /v2/top-headlines/sources
sources = newsapi.get_sources()
print ('Available resources:')

if DBG_PRINT_SOURCES:
    for s in sources['sources']:
        print ('Available resource: ', s['id'])


# Set your parameters for the news query
query='gaza'
country = 'il'        # Country (e.g., 'us' for United States)
category = 'technology'  # Category (e.g., 'business')
language='en'
news_sources='bbc-news,the-verge,google-news-ar'

# Fetch top headlines /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q=query,
                                          sources=news_sources,
                                          #category=category,
                                          #language=language,
                                          #country=country
                                          )
if 'articles' in top_headlines:
    for article in top_headlines['articles']:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print("\n")
else:
    print("No articles found")

 
# Set your parameters for the news query /v2/everything 
query = 'Gaza'  # Search query for "Middle East"
language = 'en'        # Language (e.g., 'en' for English)


for s in sources['sources']:
    # Set the number of results to 10
    page_size = 10
    source = s['id']
    # Fetch top headlines with the specified query
    everything = newsapi.get_everything(q=query, 
                                        language=language, 
                                        sources=source, 
                                        #domains='bbc.co.uk,techcrunch.com'
                                        from_param=Previous_Date,
                                        to=today,                                        
                                        sort_by='relevancy',#'publishedAt', 
                                        page_size=page_size)

    if 'articles' in top_headlines:
        for article in everything['articles']:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print("\n")
    else:
        print("No articles found")


