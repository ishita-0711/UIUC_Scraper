import UIUCScrape as uS
import RedditScrape

COURSE_NUMBER = 0
COURSE_NAME = 1
COURSE_HOURS = 2
COURSE_DESCRIPTION = 3

print(uS.getCourse("CS124", '2024', 'fall')[COURSE_DESCRIPTION])