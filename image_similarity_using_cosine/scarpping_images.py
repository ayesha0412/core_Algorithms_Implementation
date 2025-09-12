#using I crawler
# from icrawler.builtin import GoogleImageCrawler
# import os

# save_dir = "./image_similarity_using_cosine/images/"
# os.makedirs(save_dir, exist_ok=True)

# google_crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
# google_crawler.crawl(keyword="Wedneday Addams", max_num=10)

# <--using Selenium-->
#selenium: to allow and automate browser to open and scrap the imageswe want and then download that images
#requests: to grab the data of the image we want to download
#path: C:\chromedriver-win64\chromedriver-win64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
path = "C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(path)
wd = webdriver.Chrome(service=service)

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    url="https://www.google.com/search?sca_esv=1cd912c63e8479c3&rlz=1C1CHBF_en-GBPK1175PK1175&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeoJTKjrFjVxydQWqI2NcOha3O1YqG67F0QIhAOFN_ob1aWGQOelbxvw0PKo40QtwvZMGAT8mh52EQduMaEwrkL-OLEnIgHQ7APoKxFV9hua55yCiA1pSqi8NqYaykPBkHQYt8sF3mLIH7UYTHYwhcJqGpMVh&q=panda+img&sa=X&ved=2ahUKEwjcqqKS_dKPAxX3KvsDHY6qFfsQtKgLegQIEhAB&biw=1920&bih=911&dpr=1"
    wd.get(url) #google images page url
    image_urls=set() #no duplicates only unique urls
    while(len(image_urls)<max_images):
        #you've to scroll to the bttom of the page to load more images
        #find all the thumbanail and click and find the source and find that
        scroll_down(wd)
        thumbnails=wd.find_elements(By.CLASS_NAME,"YQ4gaf")
        for img in thumbnails[len(image_urls):max_images]:
            #while loop will continue to run until and unless we got enough urls
            #move to the next thumbnail that has been added already
            try:
                img.click()
                time.sleep(delay) #pop up real image
            except Exception:
                continue
        #unil now images has been clicked nad we are in inspect and class
            images=wd.find_elements(By.CLASS_NAME,"sFlh5c FyHeAf iPVvYb")
            for image in images:
                if image.get_attribute('src') in image_urls:
                    continue
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")
        return image_urls




def download_image(download_path,url, file_name):
    image_content=requests.get(url).content
    image_file=io.BytesIO(image_content)
    image=Image.open(image_file)
    file_path=download_path + file_name

    with open(file_path,"wb") as f:
        image.save(f, "JPEG")
        print("Downloaded",file_name)

urls=get_images_from_google(wd,1,10)
print(urls)

wd.quit()