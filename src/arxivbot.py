# arXiv API
import feedparser
from pydiscourse import DiscourseClient
import configparser
import json

ARXIV_CATS_DPATH = "../data/arxiv_categories.txt"
ARXIV_CATS_PATH = "../data/arxiv_categories.json"
ARXIV_PARAMS_PATH= "../params/arxiv.properties"

def clean_abstract(abstract):
    return abstract.replace('\n', ' ')

#Load API parameters
def loadParams(filepath):
    config = configparser.RawConfigParser()

    config.read(filepath)
    params = {'keys' : config.get("API", "api.key"),
              'username': config.get("API", "api.username"),
              'url': config.get("API", "api.url"),
              'rss': config.get("RSS", "rss.url")}
    return params

def filter_section(string,sec='cs') :
    if string.startswith(sec) :
        return True
    return False

def loadCategories(filePath) :
    with open(filePath) as json_file :
        data = json.load(json_file)
    json_file.close()
    return data

def getPapers(arxiv_rss, cathegory, n):
    feed = feedparser.parse(arxiv_rss + cathegory)
    return [paper for paper in feed.entries[:n]]

def loadSection(filePath, sec) :
    sections = []
    with open(filePath) as file_:
        lines = file_.read().split("\n")

        for line in lines :
            if (filter_section(line, sec)):
                if len(line) < 15 :
                    sections +=[line]
    file_.close()

    return sections

def main() :
    #Load parameters
    api_params = loadParams(ARXIV_PARAMS_PATH)
    arxiv_rss = api_params['rss']

    #Load Arxiv cathegory data
    arxiv_data = loadCategories(ARXIV_CATS_PATH)
    print("Categories: ", arxiv_data)
    # Discourse API
    client = DiscourseClient(
            api_params['url'],
            api_username= api_params["username"],
            api_key= api_params["keys"])

    print(dir(client))

    discourse_cats = client.categories()
    print(discourse_cats)
    cat_ids = {}

    print("Online Caths: ", [(cat["name"], cat['id']) for cat in discourse_cats])



    # Pull and post new preprints for each category
    for cat in arxiv_data["categories"] :
        sections = loadSection(ARXIV_CATS_DPATH, cat["short_name"])
        print("Sections: ", sections,cat["short_name"] )
        for section in sections:

            papers = getPapers(arxiv_rss, section, n=1)

            for paper in papers:
                try:
                    client.create_post(
                    content = clean_abstract(paper.summary) + "<br\> <span>Authors: </span>" +paper.author,
                    title = paper.title,
                    tags = [section],
                    category_id=cat['id']
                    )
                except Exception as e:
                    print("[Error, Warning, Log]: ", e)
                print ("Title: "+paper.title)

                print('='*50)


if __name__ == "__main__" :
    main()
