import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
from termcolor import colored
import os
import pdb
class mangacrawler:

    def __init__(self):

        print ("""
        
                Developed By:

        ##################################
        ######### Niku Nitin #############
        ##################################


        """)
        

        time.sleep(2)
        print ("""
            This script is using mangafreak.net to download Mangas.


            On Launching of this script a browser will pop-up.

            DO NOT close the browser. Just minimize it and follow the
            instructions on the screen.

            Also close any popups that may popup from the website.



        """)

        time.sleep(7)
        print ("""
            For now this script runs only with Firefox. So you need
            to have firefox installed on your system. Works
            perfectly good in Linux and Windows (Python should be 
            added to Environment Variable), not sure on MacOS.


            """)
        time.sleep(10)
        print ("""
        Future update will include compatibility with other browsers
        other than Firefox and a gui of the program if possible.


        """)
        time.sleep(5)
        
        
        print ("So Enjoy!!")
        time.sleep(2)

        
        print ('\n')
        
        currentPath = os.getcwd()
        self.oldFileArr = []
        self.current = currentPath+"/files/"

        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('browser.download.folderList',2)
        self.profile.set_preference('browser.download.manager.showWhenStarting',False)
        self.profile.set_preference('browser.download.dir', self.current)
        self.profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip')

    def startpage(self):
        
        self.driver = webdriver.Firefox(self.profile)
        self.driver.get("https://w11.mangafreak.net/")
        chk = 1
        while chk == 1:
            try:
                searchElem = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[7]/form/input[2]")
                submitBtm = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[7]/form/input[1]")
                chk = 0
                print ("Website is loaded")
                self.searchAnime()
            except selenium.common.exceptions.NoSuchElementException:
                print ("Contents are loading..")
                time.sleep(5)

    def searchAnime(self):
        print (colored("#######################", "green"))
        print (colored("#######################", "green"))
        print ("Enter the name of anime you wish to download:")
        anime = input()
        print (colored("#######################", "green"))
        print (colored("#######################", "green"))
        print ("Looking for {}".format(anime))
        searchElem = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[7]/form/input[2]")
        searchElem.clear()
        searchElem.send_keys(anime)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[7]/form/input[1]").click()
        chk = 1
        while chk == 1:
            try:
                searchItems = self.driver.find_elements_by_class_name("manga_search_item")
                chk = 0
                print (colored("#######################", "green"))
                print (colored("#######################", "green"))
                print ("{} Results found".format(len(searchItems)))
                print (colored("#######################", "green"))
                if len(searchItems) == 0:
                    print (colored("#######################", "green"))
                    print (colored("#######################", "green"))
                    print ("No results found. Try again.")
                    self.searchAnime()
                else:
                    for i in searchItems:
                        searchName = i.find_element_by_xpath("./span[2]/h3").text
                        print (str(searchItems.index(i)+1)+" "+searchName)
                    print (colored("#######################", "green"))
                    print (colored("#######################", "green"))
                    print ('Choose options or press "R" to try again.')
                    option = input()
                    self.openAnime(option)

            except selenium.common.exceptions.NoSuchElementException:
                #print ("This is embarassing, but something went wrong.")
                #print ("Please try again.")
                #sys.exit(1)
                print ("Searching")

    def openAnime(self, option):
        if option == "R":
            self.searchAnime()
        else:
            xpath ="/html/body/div[2]/div[2]/div/div/div[3]/div/div[1]/div["+option+"]/span[2]/h3/a"
            animeName = self.driver.find_element_by_xpath(xpath)
            animeChk = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div/div[1]/div["+option+"]/span[2]/h3").text

            animeName.click()
            title = self.driver.title
            print (colored("#######################", "green"))
            print ("Reading {} ".format(title))
            
            print (colored("#######################", "green"))
            chk = 1
            while chk == 1:

                if title.startswith(animeChk+" Manga Chapter"):
                    chk = 0
                    self.downloadChapters()
                else:
                    print ("Redirecting...")
                    time.sleep(2)
    def downloadChapters(self):
        chk = 1
        while chk == 1:
            try: 
                episodeTable = self.driver.find_element_by_class_name("manga_series_list")
                chk = 0
            except selenium.common.exceptions.NoSuchElementException:
                print (colored("#######################", "green"))
                print (colored("#######################", "green"))
                print ("Searching Chapters...")
                print (colored("#######################", "green"))
        chapters = self.driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[4]/div/table/tbody/tr")
        print (colored("#######################", "green"))
        print (colored("#######################", "green"))
        print ("Total no of chapters found: {}".format(len(chapters)))
        print (colored("#######################", "green"))
        print ('Enter the chapters to download')
        print (colored("#######################", "green"))
        n1 = input("Starting Chapter: ")
        print (colored("#######################", "green"))
        n2 = input("Ending Chapter:(Leave blank to download till date chapter): ")
        print (colored("#######################", "green"))
        print (colored("#######################", "green"))
        if len(n2) == 0:
            n2 = int(chapters)
        num = int(n2)+1-int(n1)
        for i in range(int(n1), int(n2)+1):
            print ("Chapters are downloading. Please do not exit the script or close the browser.")
            print (colored("#######################", "green"))
            index = str(i)
            downloadElem = "/html/body/div[2]/div[2]/div/div/div/div[4]/div/table/tbody/tr["+index+"]/td[3]/a"
            self.driver.find_element_by_xpath(downloadElem).click()
            print (colored("#######################", "green"))
            print ("Chapter {} downloading...".format(i))
            print (colored("#######################", "green"))
            time.sleep(5)
            self.afterDownload(num)

        self.DownloadStatus = False
        while self.DownloadStatus == False:
            time.sleep(5)
            self.afterDownload(num)

    def afterDownload(self, num):
        self.newFileArr = self.cleanArr(os.listdir(self.current))
        self.newFileArr.sort()
        

        if len(self.newFileArr) == num:
             
            print ("File download completed. Parsing zip files to pdfs.")
            self.DownloadStatus = True
            time.sleep(20)
            self.driver.quit()
            return True
        else:
            commArr = set(self.oldFileArr) & set (self.newFileArr)
             
            for m in commArr:
                
                self.newFileArr.remove(m)
            
            for m in self.newFileArr:
                
                
                print (colored("#######################", "green"))
                print ("{} download Complete.".format(m))
                self.oldFileArr.append(m)

    def cleanArr(self, lt):
        nt = list.copy(lt)
        for i in lt:
            if i.endswith(".part"):
                nt.remove(i)
        return nt
            
