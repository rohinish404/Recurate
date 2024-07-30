# Recurate

## PROGRESS

- custom live reload
- display json data of bookmarks in html site
- simple search + use lancedb for sematic search 
- chrome extension to execute the scrape tweets script

## TODO

- [x] add labelling script + a bit of preprocessing also
- [x] change scraping script to include only image scraping also + also make relevant changes to extension + add option for popup before saving + if
lot of tweets, somehow save in 500s
- [x] add image search using lancedb, name it memeSearch
- [x] categorise
- [x] add option for image search
- [ ] create a sh for executing files in flow
- [x] revamp whole ui 
- [ ] see if search over tweets can be improved
- [ ] create separate readmes
- [x] think of a better way for saving/managing files 
- [x] fking add print statements so to know what stage the file execution is at
- [ ] load more in scraping

**Try to finish this by next week tuesday/wednesday**

## FLOW

- Use chrome extension in src/scrape/scrape_extension to scrape the relevant page from X (twitter). Use both the text as well as image.

- Add those json files to src/data/.
- Run the execute.sh file which will create embeddings, store tweets as well as images in separate lancedb databases. download the images in src/data/downloaded_images/. create two new json files bookmarks_with_label.json and image_links.json.
- Now, we have all the files needed for running the app. 
- run the html as well as fastapi app and enjoy!
