from algoliasearch.search_client import SearchClient
import os

# Set-up client
APP_ID = os.environ.get('ALGOLIA_APPID')
APP_KEY = os.environ.get('ALGOLIA_APIKEY')
client = SearchClient.create(APP_ID, APP_KEY)
index = client.init_index('demo_helpdesk')

index.set_settings({
    'searchableAttributes': ['_title', '_tags', '_category'],
    'ignorePlurals': True,
    'removeWordsIfNoResults': 'none'
})


# Search
def search_bar(*, query):
    data = index.search(query,
                        {
                            'attributesToRetrieve': ['_title', '_category', '_questionID'],
                            'alternativesAsExact': ['ignorePlurals', 'singleWordSynonym', 'multiWordsSynonym'],
                            'responseFields': ['hits'],
                            'removeWordsIfNoResults': 'lastWords',
                            'ignorePlurals': ['en']
                        })

    result = data['hits']
    for item in result:
        answers = {'_questionID': item['_questionID'], '_title': item['_title'], '_category': item['_category']}
        return [answers]
