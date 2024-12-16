from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# יצירת אובייקט WebDriver
driver = webdriver.Chrome()

# פתיחת אתר לדוגמה
driver.get("https://www.skylinewebcams.com/en/webcam/italia/lazio/roma/piazza-di-spagna.html")

# הדפסת כותרת הדף
print("Page title is:", driver.title)

#finding the video player
video_player = driver.find_element(By.TAG_NAME, "video")
driver.execute_script("arguments[0].click();", video_player)
driver.save_screenshot("screenshot.png")
#video_player.screenshot("video_screenshot.png")

# סגירת הדפדפן
driver.quit()
