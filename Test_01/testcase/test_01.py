# -*- coding: utf-8 -*-
import csv
from ddt import data, unpack, ddt
from selenium import webdriver
import unittest, time
from selenium.webdriver import ActionChains
from os.path import os
from HTMLTestRunner import HTMLTestRunner
from base.config import getCsvData

@ddt
class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    @data(*getCsvData())
    @unpack
    def test_case(self,searchTerm,searchResult):
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        above = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_link_text(u"高级搜索").click()
        driver.find_element_by_id("adv_keyword").send_keys(searchTerm)
        driver.find_element_by_id("q5_1").click()
        driver.find_element_by_xpath(u"//input[@value='高级搜索']").click()
        time.sleep(2)
        #切换到新打开的窗口
        handles=driver.window_handles
        driver.switch_to.window(handles[-1])
        self.assertEqual(driver.title,searchResult)
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test1)
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    file="F:\\java-oxygen\\"
    report_path=os.path.join(file,"report_"+now+".html")
    with open(report_path,"wb") as rp:
        runner=HTMLTestRunner(
            stream=rp,
            title="自动化测试报告",
            description="用例执行情况"
            )
        runner.run(suite)
    
    
    
    
    
    