"""
    Fichier : main.py
    Auteur : Cédric BRUN
    Créer le 20/05/2019
    Description : Test du module appgamekit avec projet de faire un casse brique basic
"""

from appgamekit import *


class Base:

    mouse_x = 0

    def __init__(self, image: str, dev_mode: bool = False):
        """
        Description: Défini la base du casse brique
        :param image: nom du fichier
        :param dev_mode: mettre à True pour enclencher le mode développement.
        """

        self.image_id = load_image(image)
        self.dev_mode = dev_mode

        self.width = get_image_width(self.image_id)
        self.height = get_image_height(self.image_id)

        self.screen_w = get_window_width()
        self.screen_h = get_window_height()

        self.x = self.screen_w / 2 - self.width / 2
        self.y = self.screen_h - self.height

        self.sprite = create_sprite(self.image_id)
        set_sprite_size(self.sprite, self.width, self.height)
        pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            self.__x = 0
            return
        if value > self.screen_w - self.width:
            self.__x = self.screen_w - self.width
            return
        self.__x = value
        return

    def _development_mode(self):
        print_value("---- Classe Base ----")
        print_value("Window width = {}, height = {}".format(get_window_width(), get_window_height()))
        print_value("x = {}".format(self.x))
        print_value("get_sprite_x() = {}".format(get_sprite_x(self.sprite)))
        pass

    def _mouse_change(self):
        if self.mouse_x == get_raw_mouse_x():
            return False
        return True

    def update(self):
        joy = int(get_joystick_x() * 10)
        if joy:
            self.x += joy

        if self._mouse_change():
            self.x = get_raw_mouse_x() - 100

        set_sprite_position(self.sprite, self.x, self.y)
        if self.dev_mode:
            self._development_mode()
        pass


pass


def development_mode():
    print_value("DEV - MODE")
    print_value("FPS = {}".format(int(screen_fps())))
    print_value("get_joystick_x() = {}".format(get_joystick_x()))
    print_value("get_mouse_exists : {}".format(get_mouse_exists()))
    print_value("get_raw_mouse_x() = {}".format(get_raw_mouse_x()))


if __name__ == '__main__':

    screen_width = 1024
    screen_height = 768
    dev_mode = True
    with Application(x=500, y=100, width=screen_width, height=screen_height, app_name="Brick Breaker"):
        set_virtual_resolution(screen_width, screen_height)
        set_window_title("Brick Breaker")

        base = Base("base.png", dev_mode=dev_mode)
        while True:
            if dev_mode:
                development_mode()

            base.update()
            sync()
            if get_raw_key_pressed(KEY_ESCAPE):
                break
