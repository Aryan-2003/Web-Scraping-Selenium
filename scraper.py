from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common import exceptions

url = 'http://talkingdictionary.swarthmore.edu/santali/?fields=all&semantic_ids=&q='
# base_url = 'http://talkingdictionary.swarthmore.edu/santali/?initial=a&page=1'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
 
    return str1

def fetch_each_transalion(driver,url1):
  driver.get(url1)
  words = driver.find_elements(By.CLASS_NAME,'entry ')
  return words
  

def fetch_words(url):
  driver = get_driver()
  driver.get(url)
  santali_divs = driver.find_elements(By.CLASS_NAME, "entry ")
  santali_words_per_page = []
  english_words_per_page = []
  for i in range(len(santali_divs)):
    lst = (santali_divs[i].text).split('\n')
    santali_words_per_page.append(lst[0])
    eng_lst = lst[2].split(' ')
    if len(eng_lst)==1:
      english_words_per_page.append(eng_lst[0])
    else:
      word = listToString(eng_lst[1:])
      english_words_per_page.append(word)
  return [santali_words_per_page,english_words_per_page]


def fetch_audio(url):
  driver = get_driver()
  driver.get(url)
  audio_lst = [] 
  audio_tag = driver.find_elements(By.CLASS_NAME,'audio-file')
  for i in range(len(audio_tag)):
    audio_lst.append(audio_tag[i].get_attribute('href'))
  return audio_lst


def get_initials(driver):
  driver.get(url)
  li_divs = driver.find_elements(By.CLASS_NAME,"page")
  page_initial_list = []
  for i in range(len(li_divs)):
    page_initial_list.append(li_divs[i].text)
  return page_initial_list


def fetch_details(driver,word):
  audio_link = word.get_attribute('href')
  return audio_link


if __name__ == '__main__':
  driver = get_driver()
  page_initial_list = get_initials(driver)


  # english_words = []
  # santhali_words = []
  # audio_links = []
  # for init in page_initial_list:
  #   url = 'http://talkingdictionary.swarthmore.edu/santali/?initial='+init+'&page=1'
  #   tup = fetch_words(url)
  #   aud = fetch_audio(url)
  #   santhali_words = santhali_words + tup[0]
  #   english_words = english_words + tup[1]
  #   audio_links = audio_links + aud
    
  #   # print(init)

  # print(len(santhali_words),len(english_words),len(audio_links))


    ###########
  words = []
  for init in page_initial_list:
    url1 = 'http://talkingdictionary.swarthmore.edu/santali/?initial='+init+'&page=1'
    words = words + fetch_each_transalion(driver,url1)

  # print(len(words))
  # print(words[0].text)

  for word in words:
    print(fetch_details(driver,word))
    
    



  
  




  

  

  
  
