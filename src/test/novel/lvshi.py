from time import sleep

from selenium.webdriver.common.by import By

from selenium import webdriver


#https://www.69shuba.pro/txt/47113/31439537
def testChrome(d, num,book_id):
    url_prefix = 'https://www.69shuba.pro/txt/'+book_id+'/@@@.html'
    url = url_prefix.replace('@@@',num)

    next_url,title, msg = sub_content(url)
    while num+'_' in next_url:
        url = next_url
        try:
            next_url,_,msg0 = sub_content(url)
            msg = msg + msg0
        except Exception as e:
            sleep(10)

            print('发生错误：{0}'.format(e))

    title = title.replace('天启之夜', '').replace('小书包小说网', '')
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
    print(url)
    title = driver.title
    msg = driver.find_element(By.XPATH, '//*[@id="content"]').text
    #
    next_url = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[6]/a[3]').get_attribute('href')
    driver.quit()
    return next_url,title,msg


#https://www.xiaoshubao.net
if __name__ == "__main__":
    #book_id= '456816'
    book_id = '47113'
    with open('lvshi.txt', "a") as d:
        for i in range(31439535,31449535):
            testChrome(d, str(i),book_id)