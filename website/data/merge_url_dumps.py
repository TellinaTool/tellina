import pickle
import sys

source_urls = sys.argv[1]
target_urls = sys.argv[2]

with open(source_urls, 'rb') as f:
    source = pickle.load(f)
with open(target_urls, 'rb') as f:
    target = pickle.load(f)

for u in source:
    if not u in target:
        target[u] = set([])
    for url in source[u]:
        if not url in target[u]:
            print('{}: {} added'.format(u, url))
            target[u].add(url)

with open('merged.urls', 'wb') as o_f:
    pickle.dump(target, o_f)
