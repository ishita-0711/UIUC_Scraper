from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import uiuc_api as ua

# Correct way to initialize Chrome in newer Selenium versions
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("http://catalog.illinois.edu/courses-of-instruction/cs/")

# to extract - "CS" + course number, credit hours, name of the course, what its about, Gen ed reqs, pre reqs

products = driver.find_elements(by='xpath', value='//div[@class="courseblock"]')

# XPath: //a[@class="schedlink"]        → overall heading
# XPath: //p[@class="courseblockdesc"]  → course description

# 1 to extract (2) = (course number, name, credits), description
# ask how to get credits and course number and name separately

for block in products:
    try:
        title = block.find_element('xpath', './/a[@class="schedlink"]').text
        desc = block.find_element('xpath', './/p[@class="courseblockdesc"]').text
        print("Course:", title)
        print("Description:", desc)
        print()
    except Exception as e:
        print("Error:", e)


#Refactoring code to use UIUC_API instead of selenium

#get course number, name, credits and description
def getCourse(courseName, year=None, quarter=None, redirect=False):
    course = ua.get_course(courseName, year, quarter, redirect)
    return course.number, course.name, course.hours, course.description
