import re
import sys
import time
from selenium.webdriver.common.by import By
from base.base import Base
from get_driver import GetDriver


class HomePage(Base):


    def view(self,num):
        url = "https://www.sanguosha.cn/news/detail/{}.html".format(num)
        self.base_get(url)


    def get_pifu(self):

        if self.base_element_isexist((By.XPATH,"//*[contains(text(),'44444雁翎')]/..")):
            st = self.base_get_text((By.XPATH,"//*[contains(text(),'44444雁翎')]/.."))
            # srt = "十二、稀有兑换时间：4月2日-4月8日内容：188888银币兑换竭战鳞伤*曹昂（静+动）66666银币兑换步骘1600将魂兑换杨修2800将魂兑换陈琳6000将魂兑换士燮22222雁翎兑换挺身陷阵*甘宁22222雁翎兑换淑逸闲华*吴国太44444雁翎兑换迅雷风烈*张角（动态+静态）44444雁翎兑换役使鬼神*左慈（动态+静态）"
            return self.find(st)

        elif self.base_element_isexist((By.XPATH,"//*[contains(text(),'稀有兑换')]/..")):
            st = self.base_get_text((By.XPATH,"//*[contains(text(),'稀有兑换')]/.."))
            return self.find(st)
        else:
            return None

    def find(self,st):
        print(st)
        try:
            date = re.findall("时间：(.+月.+日-.+月.+日)", st)
            reg = re.findall("44444雁翎兑换(.+?)\（", st)
            print(date)
            print(reg)
            time = date[0]
            pifu = ""
            for item in reg:
                pifu = pifu + item + " "
            sp = time + "  " + pifu
            return sp
        except Exception as e:
            print(e)
            print("没有查到符合的值")
            return


if __name__ == '__main__':
        # print(sys.path)
        driver = GetDriver.get_driver()
        f = open("./te.txt","w")
        h = HomePage(driver)
        for num in range(539,1190):
        # for num in range(1178,1190):
            h.view(num)
            gp = h.get_pifu()
            if gp is not None:
                print("num：", str(num))
                print(gp)
                f.write(gp)
                f.write("\n")

        f.close()
        GetDriver.quit_driver()
