# -*- coding: utf-8 -*-
import pygame
import director
import presents_scene
import utils


def run():
    "Función principal del programa."

    dir = director.Director()
    scene = presents_scene.PresentsScene(dir)
    dir.change_scene(scene)
    dir.loop()


if __name__ == '__main__':
    run()
