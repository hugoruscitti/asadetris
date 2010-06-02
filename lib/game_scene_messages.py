# -*- encoding: utf-8 -*-
import pygame
import scene
import utils
import pytweener
import board
import piece
import display

class GameSceneMessage:
    "Representa un mensaje dentro de la escena Game."

    def __init__(self, game):
        self.game = game
        self.tweener = pytweener.Tweener()
        self.timer = 0
        pass

    def on_update(self):
        self.timer += 1
        self.tweener.update(0.01)


class AreYouReadyMessage(GameSceneMessage):

    def __init__(self, game):
        GameSceneMessage.__init__(self, game)
        self.graphic_message, self.rect = utils.load_images('gamescene/are_you_ready.png')
        self.x = - 100
        self.rect.y = 200
        self.tweener.addTween(self, x=200, tweenTime=0.3,
                tweenType=pytweener.Easing.Elastic.easeOut)
        game.pause()

        #self.unpause_and_start_to_play()

    def on_update(self):
        GameSceneMessage.on_update(self)

        if self.timer > 50:
            self.game.show_graphic_message(GoMessage(self.game))

    def on_draw(self, screen):
        self.rect.x = self.x
        screen.blit(self.graphic_message, self.rect)


class GoMessage(GameSceneMessage):

    def __init__(self, game):
        GameSceneMessage.__init__(self, game)
        self.graphic_message, self.rect = utils.load_images('gamescene/go.png')
        self.x = - 100
        self.rect.y = 200
        self.tweener.addTween(self, x=200, tweenTime=0.3,
                tweenType=pytweener.Easing.Elastic.easeOut)

    def on_update(self):
        GameSceneMessage.on_update(self)

        if self.timer > 50:
            self.game.unpause_and_start_to_play()
            self.game.show_graphic_message(None)

    def on_draw(self, screen):
        self.rect.x = self.x
        screen.blit(self.graphic_message, self.rect)


class GameOverMessage(GameSceneMessage):

    def __init__(self, game):
        GameSceneMessage.__init__(self, game)
        game.pause()
        self.graphic_message, self.rect = utils.load_images('gamescene/game_over.png')
        self.x = - 100
        self.rect.y = 200
        self.tweener.addTween(self, x=200, tweenTime=0.3,
                tweenType=pytweener.Easing.Elastic.easeOut)

    def on_update(self):
        GameSceneMessage.on_update(self)

    def on_draw(self, screen):
        self.rect.x = self.x
        screen.blit(self.graphic_message, self.rect)


class PauseMessage(GameSceneMessage):

    def __init__(self, game):
        GameSceneMessage.__init__(self, game)
        self.graphic_message, self.rect = utils.load_images('gamescene/pause.png')
        self.x = - 100
        self.rect.y = 200
        self.tweener.addTween(self, x=200, tweenTime=0.3,
                tweenType=pytweener.Easing.Elastic.easeOut)

    def on_update(self):
        GameSceneMessage.on_update(self)

    def on_draw(self, screen):
        self.rect.x = self.x
        screen.blit(self.graphic_message, self.rect)
