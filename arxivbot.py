# arXiv API
import feedparser
arxiv_rss = 'http://export.arxiv.org/rss/'
sections = ['quant-ph']
def clean_abstract(abstract):
    return abstract.replace('\n', ' ').removeprefix('<p>').removesuffix('</p>')

# Discourse API
API_KEY = 'e3d20e29465a164c40b065d37ba1a24d920ae59303ab67ae48e479fe6b116019'

from pydiscourse import DiscourseClient
client = DiscourseClient(
        'https://arxiv-talk-test.discourse.group/',
        api_username='arxivbot',
        api_key=API_KEY)

# Pull new articles
for section in sections:
    feed = feedparser.parse(arxiv_rss + section)
    print('Posting arXiv feed', feed.etag)
    
    for paper in feed.entries:
        try:
            client.create_post(
            content = clean_abstract(paper.summary),
            title = paper.title,
            tags = [section]
            )
        except Exception as e: 
            print(e)
    
    