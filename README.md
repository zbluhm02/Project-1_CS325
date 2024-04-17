**How to Use the News Scrapper:**
1. Make sure to have Git Bash and Conda installed and working on your system.
2. Download the requirement.yaml file.
3. Run this command in git bash, "conda env create -f requirement.yaml".
4. Download all the files on github and leave them in there directories.
5. Navigate to that directory through Git Bash and enter the command "python run.py".
6. This should automatically scrap the news articles and save them to as many files as urls specified.
7. This will save the scraped files in the "processed" directory and the summarized files (+ titles) in the "summarized" directory.
8. Word counts for each article will be outputed to consle.
9. To add or change what articles it scraps, either add new urls to the input.txt page seperated by new lines or replace the existing urls with new ones.

**What this Program Does:**
 This programs purpose is to scrap down new's articles to only their usable text.
