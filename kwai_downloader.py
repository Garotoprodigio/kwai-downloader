import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações
profile_url = "https://www.kwai.com/@Portelas"  # URL do perfil do Kwai
min_likes = 1  # Mínimo de likes para baixar o vídeo
max_videos = 10  # Número máximo de vídeos para baixar

# Configuração do Selenium para usar o ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless (sem abrir janela)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa a página do perfil
driver.get(profile_url)
time.sleep(5)  # Aguarda a página carregar

# Rola a página para garantir que os vídeos sejam carregados
scroll_pause_time = 3
last_height = driver.execute_script("return document.body.scrollHeight")

downloaded_videos = 0
video_urls = set()  # Para evitar duplicados

while downloaded_videos < max_videos:
    # Encontra os elementos dos vídeos
    video_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/video/")]')

    for video_element in video_elements:
        if downloaded_videos >= max_videos:
            break

        try:
            video_url = video_element.get_attribute('href')
            if video_url and video_url not in video_urls:
                video_urls.add(video_url)
                driver.get(video_url)
                time.sleep(3)

                # Obtendo a URL do vídeo
                video_src = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
                likes_element = driver.find_element(By.CLASS_NAME, "num")
                likes = int(likes_element.text.replace("K", "000").replace("M", "000000"))

                if likes >= min_likes:
                    # Faz o download do vídeo
                    response = requests.get(video_src)
                    if response.status_code == 200:
                        with open(f"video_{downloaded_videos + 1}.mp4", "wb") as file:
                            file.write(response.content)
                        print(f"Vídeo {downloaded_videos + 1} baixado com sucesso: {video_src}")
                        downloaded_videos += 1
                    else:
                        print(f"Erro ao baixar o vídeo: {video_src}")

        except Exception as e:
            print(f"Erro ao processar vídeo: {str(e)}")

    # Rola a página para carregar mais vídeos
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        # Não há mais conteúdo para carregar
        break

    last_height = new_height

# Encerra o Selenium
driver.quit()

print("Download concluído.")
