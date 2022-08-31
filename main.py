from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
        notification.notify(
            title = title,
            message = message,
            app_icon = r"C:\Users\gunjan\Desktop\Projects\corona_break\icofile.ico",
            timeout = 7
        )
def getData(url):
        r = requests.get(url)
        return r.text


if __name__ == "__main__":
   while True:
       myHtmlData = getData(r'https://www.oneindia.com/covid-19-vaccine-tracker.html')
       soup = BeautifulSoup(myHtmlData, 'html.parser')
       states = ['Chandigarh','Punjab','Mizoram']

       for tr in soup.find_all('tbody')[0].find_all('tr'):
                myDataStr = tr.get_text()
                itemList = myDataStr.split(' ')
                if itemList[0] in states:
                    nTitle = 'Vaccination Updates of Covid-19'
                    nText = f"State {itemList[0]}\nDose 1 : {itemList[2]}\nDose 2 : {itemList[3]}\nTotal Vaccination:  {itemList[4]}\nTotal Vaccinated Day before : {itemList[5]}"
                    notifyMe(nTitle, nText)
                    time.sleep(3)
       time.sleep(3600)

         
        
       