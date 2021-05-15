
from algoliasearch.search_client import SearchClient

# Set-up client
client = SearchClient.create('N2BVRKR2WU', 'fc548024e0db5e888ec47f639ddbe857')
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
                            # 'query': query,
                            'attributesToRetrieve': ['_title', '_category', '_questionID'],
                            'alternativesAsExact': ['multiWordsSynonym'],
                            'responseFields': ['hits'],
                            'removeWordsIfNoResults': 'lastWords',
                            'ignorePlurals': ['en']
                        })

    # result = [hit for hit in data]
    result = data['hits']
    for item in result:
        answers = {'_questionID': item['_questionID'], '_title': item['_title'], '_category': item['_category']}
        return [answers]


# ans = search_bar(query="cost")
# print(ans)
# for i in ans:
#     print(i)

