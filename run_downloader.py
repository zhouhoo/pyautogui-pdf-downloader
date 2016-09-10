import pyautogui
import time

pages = 1168 # 总共多少页
scrolltimes = 3  # 每页鼠标需要滚动的次数
download_x = 522 # 下载链接的位置x
download_y = 293  # 下载链接的位置y
first_item_x = 793  # 每页文件列表的第一个文件链接的x

scroll_x = 1590  # 鼠标滚动栏的x坐标
bind = [(299,226),(418,246),(511,229),(642,237)]# 鼠标滚动栏y坐标和文件列表的第一个文件链接的y坐标

for page in range(936,pages):
    if page == 0 :
        pass
    else:
        pyautogui.moveTo(1490, 758)# next page location
        pyautogui.click()
        time.sleep(1) #加载下一页需要时间
    print(page)
    for curren_scroll,first_item_y in bind:
        pyautogui.moveTo(scroll_x,curren_scroll)
        pyautogui.click()
        
        for moves in range(14):
            
           # distance = 6
            pyautogui.moveTo(first_item_x,first_item_y+37*moves)
            pyautogui.click()
            
            
            time.sleep(1) #弹出下载页需要时间
            pyautogui.click(download_x,download_y)
#             while distance >0:
#                 pyautogui.moveRel(0,2)
#                 pyautogui.click()
#                 distance -= 1
            #time.sleep(2)
            #pyautogui.click(701,380)# close on-downloading warning dailog
            pyautogui.click(1037,488)# close on-downloading warning dailog
            pyautogui.click(985,313)	# close pdf format error dailog
            pyautogui.click(1359,42)    # close pdf viewer
            pyautogui.click(1456,159)	# close Downloader dailog
            
        




