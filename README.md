Using `feedparser` and `pydiscourse`.

TODO:
- Hide API key
- Add authors with link to arxiv author page
- Include all sections (scrape from [this page](https://arxiv.org/category_taxonomy))
- Deal with cross-posting and updated articles
- Check that posts look good, including latex rendering ($ without space before creates pbs, for instance)
- When posting, look up author in database. If author is member of the Discourse, tag them
- wrap bot in scheduler (run every weekday) in a stable way (also with reboots)