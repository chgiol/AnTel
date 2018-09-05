from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import urllib


def comprobar():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1280x720")

        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get("http://www.piraminetlab.com")
        driver.find_element_by_tag_name("textarea").send_keys("http://www.rtve.es/alacarta/videos/telediario/")
        driver.find_element_by_id('boton_azul').click()
        time.sleep(5)
        link = driver.find_element_by_xpath("//a[@class='enlace']").get_attribute(
            "href")

        fecha = driver.find_element_by_xpath("//div[@id='info_titulo']").text
        fecha = fecha.replace(' ', '')
        fecha = fecha.replace('/', '_')
        print(link, fecha)
        driver.quit()
        return link, fecha
    except Exception as e:
        print('Error, no se ha encontrado archivo a descargar')
        driver.quit()
        return 0, 0


# comprobar()

# http://www.rtve.es/resources/TE_NGVA/mp4/9/2/1533912681629.mp4
def descarga_vid(link='http://techslides.com/demos/sample-videos/small.mp4', name='telediario'):
    t0=time.time()
    name = 'videos/' + name + ".mp4"
    print("****Connected****")
    print("Donloading.....")
    r = requests.get(link)
    f = open(name, 'wb')
    print('Writing')
    for chunk in r.iter_content(chunk_size=255):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    t1 = time.time()
    print(t1-t0)
    f.close()
    return name
