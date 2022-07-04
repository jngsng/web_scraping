import requests
from bs4 import BeautifulSoup

# method / function inside of object

SARAMIN_URL = "https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=python&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&job_type=1&panel_type=&search_optional_item=y&search_done=y&panel_count=y&" + "recruitPage=1" + "&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"


def extract_saramin_pages():
  saramin_result=requests.get(SARAMIN_URL)
  
  saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")
  
  pagination = saramin_soup.find("div",{"class":"pagination"})
  
  links = pagination.find_all("a")
  pages = []
  
  for link in links[:-1]:
    pages.append(int(link.string))
  
  max_page = pages[-1]