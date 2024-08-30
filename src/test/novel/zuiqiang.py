from time import sleep

from selenium.webdriver.common.by import By

from selenium import webdriver



def testChrome(d, num,book_id):
    url_prefix = 'https://www.piaotia.com/html/1/'+book_id+'/@@@.html'
    url = url_prefix.replace('@@@',num)

    next_url,title, msg = sub_content(url)
    # while num+'_' in next_url:
    #     url = next_url
    #     try:
    #         next_url,_,msg0 = sub_content(url)
    #         msg = msg + msg0
    #     except Exception as e:
    #         sleep(10)
    #
    #         print('发生错误：{0}'.format(e))
    #
    # title = title.replace('天启之夜', '').replace('小书包小说网', '')
    # content = msg.replace('-->>','').replace('本章未完，点击下一页继续阅读','')
    # d.write('\r\n')
    # d.write(title)
    # d.write('\r\n')
    # d.write(content)







def sub_content(url):
    print(url)
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  # Chrome浏览器

    t = driver.get(url)
    print(t)
    title = driver.title
    msg = driver.find_element(By.XPATH, '//*[@id="content"]').text
    print(msg)
    #
    next_url = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/div/div[6]/a[3]').get_attribute('href')
    driver.quit()
    return next_url,title,msg


#https://www.piaotia.com/html/1/1710/765235.html
if __name__ == "__main__":
    #book_id= '456816'
    book_id = '1710'
    page_id =765235
    with open('zuiqiang.txt', "a") as d:
        for i in range(0,269):
            testChrome(d, str(page_id+i),book_id)