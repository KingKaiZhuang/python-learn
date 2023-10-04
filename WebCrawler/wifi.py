from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

# WiFi網路名稱到IP地址的映射
network_ip_mapping = {
    "STUST": "http://教室1的IP地址",
    # 其他網絡名稱和對應的IP地址
}

# 偵測當前連接的WiFi網路名稱
current_network_name = "STUST"  # 這個名稱應該是根據實際情況獲得的

# 根據當前網路名稱選擇對應的IP地址
if current_network_name in network_ip_mapping:
    ip_address = network_ip_mapping[current_network_name]
else:
    # 如果未找到對應的IP地址，可以設置一個默認的IP地址
    print("連線失敗")

# 使用選擇的IP地址來訪問網站
url = ip_address + "/login"
