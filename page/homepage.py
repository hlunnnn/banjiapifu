import re
import sys
import time
from selenium.webdriver.common.by import By
from base.base import Base
from get_driver import GetDriver


class HomePage(Base):


    def view(self,num):
        url = "https://www.sanguosha.cn/news/detail/{}.html".format(num)
        # self.base_get(url)


    def get_pifu(self):
        str = self.base_get_text((By.XPATH,"//span[contains(text(),'稀有兑换')]/.."))
        # srt = "十二、稀有兑换时间：4月2日-4月8日内容：188888银币兑换竭战鳞伤*曹昂（静+动）66666银币兑换步骘1600将魂兑换杨修2800将魂兑换陈琳6000将魂兑换士燮22222雁翎兑换挺身陷阵*甘宁22222雁翎兑换淑逸闲华*吴国太44444雁翎兑换迅雷风烈*张角（动态+静态）44444雁翎兑换役使鬼神*左慈（动态+静态）"
        print(str)
        dic = {}
        date = re.findall("稀有兑换时间：(.+?)内容",str)
        reg = re.findall("44444雁翎兑换(.+?)（动态\+静态）",str)
        dic[date[0]] = reg
        print(dic)

        for key in dic:
            print(key,end=' ')
            for item in dic[key]:
                print(item,end=' ')
            print("")




if __name__ == '__main__':
        print(sys.path)
        driver = GetDriver.get_driver()
        h = HomePage(driver)
        h.view("1189")
        time.sleep(2)
        h.get_pifu()
        GetDriver.quit_driver()
