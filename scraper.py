from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

url = 'http://talkingdictionary.swarthmore.edu/santali/?fields=all&semantic_ids=&q='


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
 

def fetch_word_divs(driver,base_url):
  driver.get(base_url)
  word_div = driver.find_elements(By.CLASS_NAME,'entry ')
  return word_div
  
# def fetch_details(driver,word_div):
#   driver.
#   words = word_div.text
#   return words


if __name__ == '__main__':
  
  print('Creating driver...')
  driver=get_driver()
  driver.get(url)

  # Since there are many pages so working on each page using the initial letter So fetching the initial letters
  
  initial_letters = []
  initials = driver.find_elements(By.CLASS_NAME,'page')
  for initial in initials:
    initial_letters.append(initial.text)
  
  print(initial_letters)

  
  #Fetching all the words divs

  
  santhali_words = [] 
  eng_words = [] 
  audio_links = [] 
  grammer = [] 

  
  for init in initial_letters:
    base_url = 'http://talkingdictionary.swarthmore.edu/santali/?initial=' + init +'&page=1'
    word_divs = fetch_word_divs(driver,base_url)
    # print(word_divs)
    for div in word_divs:
      audio_div = div.find_element(By.TAG_NAME,'a')
      audio_link = audio_div.get_attribute('href')
      lst = div.text.split('\n')
      # print(lst)
      santali_word = lst[0]
      english_word = ""
      english_word_lst = lst[2].split(' ')
      if len(english_word_lst)==1:
        english_word = english_word_lst[0]
        grammer.append('NaN')
      else:
        english_word = listToString(english_word_lst[1:])
        grammer.append(english_word_lst[0])

      eng_words.append(english_word)
      santhali_words.append(santali_word)
      if audio_link:
        audio_links.append(audio_link)
      else:
        audio_links.append('NaN')

  print(len(eng_words),len(santhali_words),len(audio_links))

  df = pd.DataFrame({
    'Santhali_word':santhali_words,
    'English_words':eng_words,
    'Grammer' : grammer,
    'Audio_links':audio_links
  })

  print(df)
  df.to_csv('santhali_to_english.csv',index=None)




  

 

  

  
  




    



  
  




  

  

  
  
