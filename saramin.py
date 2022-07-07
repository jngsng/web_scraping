import requests
from bs4 import BeautifulSoup

# method / function inside of object

URL1 = "https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=python&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&job_type=1&panel_type=&search_optional_item=y&search_done=y&panel_count=y&"

URL2 = "&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"


def extract_saramin_pages():
  result=requests.get(URL1+URL2)
  
  soup = BeautifulSoup(result.text, "html.parser")
  
  pagination = soup.find("div",{"class":"pagination"})
  
  links = pagination.find_all("a")
  pages = []
  
  for link in links[:-1]:
    pages.append(int(link.string))
  
  max_page = pages[-1]
  return(max_page)

def extract_job(result, result_corp):
  result = requests.get(f"{URL1}recruitPage={1}{URL2}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div",{"class":"area_job"})
  results_corp = soup.find_all("div",{"class":"area_corp"})

  title = (results.find("h2",{"class":"job_tit"})).find("a")["title"]
  corp = (results_corp.find("strong",{"class":"corp_name"}).find("a").string)
  corp = corp.strip()
  return{"title":title,"company":corp} 

def extract_saramin_jobs(last_page):
  #for page in range(last_page):
    result = requests.get(f"{URL1}recruitPage={1}{URL2}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"area_job"})
    results_corp = soup.find_all("div",{"class":"area_corp"})
  
    for result, result_corp in zip(results, results_corp):
      job = extract_job(result, result_corp)
      print(job)
      
      #title = (result.find("h2",{"class":"job_tit"})).find("a")["title"]
      #corp = (result_corp.find("strong",{"class":"corp_name"}).find("a").string)
      #corp = corp.strip()
      #print(title,corp)
      
    #for result in results_corp:
     # corp = (result.find("strong",{"class":"corp_name"}).find("a").string)
      #corp = corp.strip()
      #print(title, corp)
