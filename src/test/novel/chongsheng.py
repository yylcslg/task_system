from time import sleep

from selenium.webdriver.common.by import By

from selenium import webdriver



def testChrome(d, num):
    url_prefix = 'https://www.xiaoshubao.net/read/456816/@@@.html'
    url = url_prefix.replace('@@@',num)

    next_url,title, msg = sub_content(url)
    while num+'_' in next_url:
        print(next_url)
        url = next_url
        try:
            next_url,_,msg0 = sub_content(url)
            msg = msg + msg0
        except Exception as e:
            sleep(10)

            print('发生错误：{0}'.format(e))

    title = title.replace('都重生了谁谈恋爱啊', '').replace('小书包小说网', '')
    content = msg.replace('-->>','').replace('本章未完，点击下一页继续阅读','')
    d.write('\r\n')
    d.write(title)
    d.write('\r\n')
    d.write(content)







def sub_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  # Chrome浏览器
    driver.get(url)

    title = driver.title
    msg = driver.find_element(By.XPATH, '//*[@id="content"]').text
    #
    next_url = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[6]/a[3]').get_attribute('href')
    driver.quit()
    return next_url,title,msg



if __name__ == "__main__":

    with open('chongsheng4.txt', "a") as d:
        for i in range(487,600):
            testChrome(d, str(i))