import json

from algoliasearch.search_client import SearchClient


# Set-up client
client = SearchClient.create('N2BVRKR2WU', 'fc548024e0db5e888ec47f639ddbe857')
index = client.init_index('demo_helpdesk')

# Search
query = input("Enter search: ")
if len(query) < 250:    # limit of 512 characters per query by Algolia
    # res = index.search(query)
    data = index.browse_objects({
        'query': query,
        'attributesToRetrieve': ['title', 'category']
    })

    # data = res["hits"]
    # for i in data:
    #     ans = {"title": i["title"], "category": i["category"]}
    for hit in data:
        print(hit)
