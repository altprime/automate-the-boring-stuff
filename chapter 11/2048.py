'''
2048

play 2048 game at https://gabrielecirulli.github.io/2048/

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def playGame():
    url = "https://gabrielecirulli.github.io/2048/"
    browser = webdriver.Firefox()
    browser.get(url)

    game = browser.find_element_by_class_name("game-container")
    over = browser.find_element_by_class_name("retry-button")

    while over.is_displayed() == False:
        game.send_keys(Keys.UP)
        game.send_keys(Keys.RIGHT)
        game.send_keys(Keys.DOWN)
        game.send_keys(Keys.LEFT)


    print("Game over")

playGame()