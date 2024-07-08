import os
import requests
import time

def run():
    webSiteUrl = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY"))
    maxTrials = int(os.getenv("MAX_TRIALS"))

    websiteReacheble = pingURL(webSiteUrl=webSiteUrl, delay=delay, maxTrials=maxTrials)
    print("Hello world")
    return

def pingURL(**kwargs):
    webSiteUrl = kwargs.get('webSiteUrl')
    delay = kwargs.get('delay')
    maxTrials = kwargs.get('maxTrials')
    
    trials = 0
    while trials <= maxTrials:
        try:
            response = requests.get(webSiteUrl)
            if response.status_code == 200:
                print("A URL é acessível")
                return True
        except requests.ConnectionError:
            print(f"A conexão na {webSiteUrl} falhou, tentando novamente em {delay} segundos...")
            time.sleep(delay)
            trials += 1
    print("Máximo de tentativas alcançado. A URL não é acessível.")
    return False

if __name__ == "__main__":
    run()
