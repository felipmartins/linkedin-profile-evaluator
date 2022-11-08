import requests
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .face_detection import FaceDetector

def scrape_linkedin(user):
    dic = {}

    dic['url_name'] = user

    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.linkedin.com/uas/login")
    sleep(2)
    driver.find_element(By.NAME, 'session_key').send_keys('dezesseis.turma@gmail.com')
    sleep(2)
    driver.find_element(By.NAME, 'session_password').send_keys('Umasenhaforte-123')
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn'+'__'+'primary--large').submit()
    sleep(2)
    driver.get(f"https://www.linkedin.com/in/{user}")
    sleep(2)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pv-top-card--list-bullet'))
        )
        sleep(0.5)
    except:
        ...

    sleep(0.5)
    name = driver.find_element(By.CLASS_NAME, 'text-heading-xlarge')


    dic['full_name'] = name.text

    sleep(0.5)
    profile_pic = driver.find_element(By.CLASS_NAME, 'pv-top-card-profile-picture' + '__' + 'image').get_attribute("src")
    dic['profile_image'] = user + "_image.jpg"

    try:
        photo_response = requests.get(profile_pic)
        if photo_response.status_code == 200:
            dic['has_changed_profile_image'] = True
            image_path = "media/" + user + "_image.jpg"
            with open(image_path, "wb") as handler:
                handler.write(photo_response.content)
                dic["face_found_in_profile_image"] = FaceDetector.find_faces(image_path)
        else:
            dic['has_changed_profile_image'] = False
            dic["face_found_in_profile_image"] = False
    except:
        dic['has_changed_profile_image'] = False
        dic["face_found_in_profile_image"] = False
    try:
        sleep(0.5)
        background_pic = driver.find_element(By.CLASS_NAME, 'profile-background-image' + '__' + 'image').get_attribute("src")
        photo_response = requests.get(background_pic)
        if photo_response.status_code == 200:
            background_pic = user + "_background_image.jpg"
            with open('media/' + background_pic, "wb") as handler:
                handler.write(photo_response.content)
    except:
        background_pic = None
    dic['background_image'] = background_pic
    dic['has_changed_background_image'] = True if background_pic else False


    sleep(0.5)
    connections = driver.find_element(By.CLASS_NAME, 'pv-top-card--list-bullet')
    print(connections.text.split(' '))
    if 'followers' in connections.text:
        dic['connections'] = int(connections.text.split(' ')[1][-3::]) if "+" not in connections.text.split(' ')[1] else int(connections.text.split(' ')[1][-4:-1])
    else:
        dic['connections'] = int(connections.text.split(' ')[0]) if "+" not in connections.text.split(' ')[0] else int(connections.text.split(' ')[0][:-1])

    try:
        sleep(0.5)
        about = driver.find_element(By.CLASS_NAME, 'pv-shared-text-with-see-more').text
    except:
        about = None

    dic['about'] = about


    sleep(0.5)
    head_title = driver.find_element(By.CLASS_NAME, 'text-body-medium')
    dic['head_title'] = head_title.text


    driver.get(f"https://www.linkedin.com/in/{user}/overlay/contact-info")
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pv-profile-section' + '__' + 'section-info'))
        )
        sleep(0.5)
    except:
        ...
    sleep(0.5)
    contact_info = driver.find_element(By.CLASS_NAME, 'pv-profile-section' + '__' + 'section-info')
    sons = contact_info.find_elements(By.CSS_SELECTOR, 'a')
    contact_dic = {}
    counter = 1
    for son in sons:
        contact_dic['contact_'+str(counter)]=son.text
        counter+=1
    dic['contact_info'] = contact_dic


    driver.get(f'https://www.linkedin.com/in/{user}/details/education/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...
    education = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    edu_dic = {}
    counter = 1
    for son in education:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            edu_dic['edu_'+str(counter)] = string
            counter += 1

    dic['education'] = edu_dic
            

    driver.get(f'https://www.linkedin.com/in/{user}/details/skills/')

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...

    skill = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    skill_dic = {}
    counter = 1
    for son in skill:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            skill_dic['skill_'+str(counter)] = string
            counter += 1
    dic['skills'] = skill_dic


    driver.get(f'https://www.linkedin.com/in/{user}/details/recommendations/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...
    recommendation = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    recommend_dic = {}
    counter = 1
    for son in recommendation:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            recommend_dic['recommendation_'+str(counter)] = string
            counter += 1

    dic['recommendations'] = recommend_dic

    driver.get(f'https://www.linkedin.com/in/{user}/details/experience/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...

    experience = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    exp_dic = {}
    counter = 1
    for son in experience:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            exp_dic['exp_'+str(counter)] = string
            counter += 1
    dic['experience'] = exp_dic

    driver.get(f'https://www.linkedin.com/in/{user}/details/projects/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...
    projects = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    proj_dic = {}
    counter = 1
    for son in projects:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            proj_dic['proj_'+str(counter)] = string
            counter += 1
    dic['projects'] = proj_dic

    driver.get(f'https://www.linkedin.com/in/{user}/details/certifications/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...
    certifications = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    cert_dic = {}
    counter = 1
    for son in certifications:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            cert_dic['cert_'+str(counter)] = string
            counter += 1
    dic['certifications'] = cert_dic


    driver.get(f'https://www.linkedin.com/in/{user}/details/languages/')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item'))
        )
        sleep(0.5)
    except:
        ...
    languages = driver.find_elements(By.CLASS_NAME, 'pvs-list' + '__' + 'paged-list-item')
    lang_dic = {}
    counter = 1
    for son in languages:
        grand_sons = son.find_elements(By.CLASS_NAME, 'visually-hidden')
        string = ''
        for grand_son in grand_sons:
            string += grand_son.text + ' '
        if string.split():
            lang_dic['lang_'+str(counter)] = string
            counter += 1
    dic['languages'] = lang_dic


    driver.get(f'https://www.linkedin.com/in/{user}/recent-activity/shares/')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-finite-scroll__content'))
        )
        sleep(0.5)
    except:
        ...
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    posts = driver.find_elements(By.CLASS_NAME, 'feed-shared-update-v2')

    dic['authoral_posts'] = len(posts)

    driver.quit()

    return dic