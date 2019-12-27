from modules.scrape import mangacrawler
from modules.files import files
scrapeObject = mangacrawler()
scrapeObject.startpage()
fileObj = files()
fileObj.getName()
fileObj.processfiles()
fileObj.cleanImg()
fileObj.cleanZip()
fileObj.cleanDir()
print ("If there is no error msg on your screen then Enjoy!! All tasks completed successfully.")
