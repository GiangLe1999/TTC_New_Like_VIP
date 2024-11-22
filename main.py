import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Cấu hình tài khoản
accounts = [
    # {
    #     "name": "legiangbmt017",
    #     "chrome_path": "C:\\Others\\Facebook Accounts\\legiangbmt017\\GoogleChromePortable\\GoogleChromePortable.exe",
    #     "user_data_dir": "C:\\Others\\Facebook Accounts\\legiangbmt017\\GoogleChromePortable\\Data\\profile\\Default",
    # },
    {
        "name": "n17dcqt014",
        "chrome_path": "C:\\Others\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "C:\\Others\\Facebook Accounts\\n17dcqt014\\GoogleChromePortable\\Data\\profile\\Default",
    },
    # {
    #     "name": "caytienbmt05",
    #     "chrome_path": "C:\\Others\\Facebook Accounts\\caytienbmt05\\GoogleChromePortable\\GoogleChromePortable.exe",
    #     "user_data_dir": "C:\\Others\\Facebook Accounts\\caytienbmt05\\GoogleChromePortable\\Data\\profile\\Default",
    # },
    # {
    # "name": "caytienbmt02", # Đang checkpoint
    #     "chrome_path": "C:\\Others\\Facebook Accounts\\caytienbmt02\\GoogleChromePortable\\GoogleChromePortable.exe",
    #     "user_data_dir": "C:\\Others\\Facebook Accounts\\caytienbmt02\\GoogleChromePortable\\Data\\profile\\Default",
    # },
    # {
    #     "name": "thanhtruong1691",
    #     "chrome_path": "C:\\Others\\Facebook Accounts\\thanhtruong1691\\GoogleChromePortable\\GoogleChromePortable.exe",
    #     "user_data_dir": "C:\\Others\\Facebook Accounts\\thanhtruong1691\\GoogleChromePortable\\Data\\profile\\Default",
    # },
    {
        "name": "caytienbmt09",
        "chrome_path": "C:\\Others\\Facebook Accounts\\caytienbmt09\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "C:\\Others\\Facebook Accounts\\caytienbmt09\\GoogleChromePortable\\Data\\profile\\Default",
    },
    {
        "name": "lttskda",
        "chrome_path": "C:\\Others\\Facebook Accounts\\lttskda\\GoogleChromePortable\\GoogleChromePortable.exe",
        "user_data_dir": "C:\\Others\\Facebook Accounts\\lttskda\\GoogleChromePortable\\Data\\profile\\Default",
    },
]

# Cấu hình driver
def init_driver(account):
    options = webdriver.ChromeOptions()
    options.binary_location = account["chrome_path"]
    options.add_argument(f"--user-data-dir={account['user_data_dir']}")  # Thư mục dữ liệu riêng
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument(f"--remote-debugging-port=9300")  # Cổng Debug riêng

    # Sử dụng webdriver-manager để tự động tải ChromeDriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# Tìm và nhấn nút thích trong tab mới
def like_post(driver):
    try:
        time.sleep(5)
        # Lấy URL hiện tại của tab
        current_url = driver.current_url
        
        # Xác định class dựa trên URL (Nút Like trên tất cả các Page đều có class giống nhau ngoại trừ nút Like trên page Reel)
        if "reel" in current_url:
            like_buttons = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xzolkzo x12go9s9 x1rnf11y xprq8jg x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1vqgdyp x100vrsf x1qhmfi1')]")
        else:
            like_buttons = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x5ve5x3')]")

        # Chọn nút Like dựa trên số lượng tìm thấy và URL
        if len(like_buttons) == 1:
            like_button = like_buttons[0]  # Chỉ có một nút
        elif "watch" in current_url:  # Nếu URL chứa từ "watch"
            like_button = like_buttons[0]
        else:
            like_button = like_buttons[1]  # Chọn nút thứ hai nếu có nhiều hơn một
        
        like_button.click()
        time.sleep(2)

        # Kiểm tra có bị hạn chế hoạt động không
        # Tìm thẻ span có chứa đoạn text cụ thể
        restricted_message = "Bạn không thể làm một hay nhiều việc như bình thường do hoạt động trên tài khoản của bạn không tuân thủ Tiêu chuẩn cộng đồng của chúng tôi."
        span_to_check = driver.find_elements(By.XPATH, f"//span[contains(text(), '{restricted_message}')]")
        if span_to_check:  # Nếu tìm thấy span với đoạn text cụ thể
            print("Thông báo hạn chế hoạt động đã xuất hiện.")
            return False

        return True  # Nếu không tìm thấy thẻ span, trả về True
    except Exception as e:
        print(f"An error occurred: {e}")
        return True

# Tìm và nhấn nút "Nhận tiền"
def receive_money(driver):
    try:
        money_button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'nhantien')]")
        money_button.click()
        time.sleep(15)
    except Exception:
        pass

# Vòng lặp chính
def perform_task(account, round_count):
    print(f"Initializing task for account: {account['name']}")
    driver = init_driver(account)
    completed_round = 0

    print(f"Navigating to login page for account: {account['name']}")
    driver.get("https://tuongtaccheo.com/index.php")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password' and contains(@placeholder, '*')]"))
        )
        
        login_button = driver.find_element(By.XPATH, "//input[@name='submit' and @type='submit' and contains(@value, 'ĐĂNG NHẬP')]")
        login_button.click()
        
    except NoSuchElementException:
        print("Lỗi: Không tìm thấy nút ĐĂNG NHẬP.")
        return False
    except Exception as e:
        print(f"Unexpected error during login: {e}")
        return False

    time.sleep(5)
    driver.get("https://tuongtaccheo.com/kiemtien/likepostvipcheo/")

    while completed_round < round_count:
        print(f"Starting round {completed_round + 1} of {round_count}...")
        try:
            time.sleep(10)
            buttons = driver.find_elements(By.XPATH, "//button[contains(@onclick, 'like')]")
            print(f"Found {len(buttons)} like buttons.")

            for i, button in enumerate(buttons):
                button.click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])

                # Gọi hàm like_post và kiểm tra kết quả
                if not like_post(driver):  # Nếu hàm trả về False
                    print("Stopping loop as like_post returned False.")
                    completed_round = round_count  # Gán completed_round bằng round_count
                    break  # Dừng vòng lặp

                print("Post liked successfully!")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                receive_money(driver)

            completed_round += 1

            if completed_round < round_count:
                print("Reloading task list for the next round...")
                reload_button = driver.find_element(By.ID, "tailai")
                reload_button.click()
                time.sleep(5)

        except Exception as e:
            print(f"Error occurred during round {completed_round + 1}: {e}")
            break

    print(f"Completed all {round_count} rounds for account: {account['name']}")
    driver.quit()
    print("Driver closed.")



# Số lần lặp
round_count = 5

# Thực thi
for account in accounts:
    perform_task(account, round_count)
