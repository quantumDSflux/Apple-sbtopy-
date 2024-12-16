import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "None", [
            {
                'name': "IMG_1957",
                'path': "1e87a0063fa6f2c527fb3419651824ff.svg",
                'center': (247, 185),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "Crazy - JVNA & BEAUZ (NCS release)Crazy - JVNA & BEAUZ (NCS release)",
                'path': "7d2383af4ce9bddf2b06dd80e52b6be5.mp3"
            }
        ])

        self.var_Controlby = "Keyboard"
        self.var_Starttimer = 2.801
        self.var_Controlkeys = "0000"
        self.var_Score = 4
        self.var_WR = 20



        self.sprite.layer = 0

    @on_green_flag
    async def green_flag(self, util):
        while True:
            await util.sprites["rittai"].broadcast_A(util)

            await self.yield_()

    @on_pressed('t')
    async def key_t_pressed(self, util):
        if eq(config.USERNAME, "kazusc"):
            util.send_broadcast("TN")


@sprite('Thumbnail')
class SpriteThumbnail(Target):
    """Sprite Thumbnail"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "~誘導/GUIDE~",
                'path': "c6f9fc6a834106779330768059249c99.svg",
                'center': (247, 185),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 8

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True
        self.front_layer(util)
        self.change_layer(util, -1)

    @on_clicked
    async def sprite_clicked(self, util):
        self.costume.set_effect('ghost', 100)
        util.send_broadcast("Start")

    @on_broadcast('tn')
    async def broadcast_tn(self, util):
        self.shown = True
        self.front_layer(util)
        util.stop_all()
        return None


@sprite('遊びサムネ用')
class Spriteidentifier(Target):
    """Sprite 遊びサムネ用"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "コスチューム2",
                'path': "f4ed0b947dd7d322d47129e3e5d94b8d.svg",
                'center': (84, 263),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 9

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False


@sprite('Player')
class SpritePlayer(Target):
    """Sprite Player"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -174.51852477659796
        self._ypos = -7.652778141944618
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "Blue-Ball",
                'path': "9dd9e64c7fed28dcb29a1f9ba06dff53.svg",
                'center': (17, 17),
                'scale': 1
            },
            {
                'name': "Blue-Ball-light",
                'path': "3eac803f79b2c938034a848128e5e158.svg",
                'center': (83, 83),
                'scale': 1
            },
            {
                'name': "Red-Ball",
                'path': "de582e253f071d1ec3d8dae4e7b0b0c8.svg",
                'center': (17, 17),
                'scale': 1
            },
            {
                'name': "Red-Ball-light",
                'path': "71bd226c48a715b0cb92e1b07e7aa8ed.svg",
                'center': (34, 34),
                'scale': 1
            },
            {
                'name': "Yellow-Ball",
                'path': "701ae0eb86cc3e9ac091764e72f14157.svg",
                'center': (17, 17),
                'scale': 1
            },
            {
                'name': "Yellow-Ball-light",
                'path': "ba1f76a977e646f93247fb022da751b4.svg",
                'center': (34, 34),
                'scale': 1
            },
            {
                'name': "GUIDE-Area",
                'path': "65e7494d016fc7a412ede3a10011005e.svg",
                'center': (83, 83),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = -3.042251401638648
        self.var_y = "-0.01071590688611241"



        self.sprite.layer = 1

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        await self.my_Chara(util, )

    @warp
    async def my_Chara(self, util, ):
        self.costume.switch("Blue-Ball")
        self.var_x = ((self.var_x + ((tonum(letter_of(util.sprites.stage.var_Controlkeys, 1)) * 0.8) - (tonum(letter_of(util.sprites.stage.var_Controlkeys, 2)) * 0.8))) * 0.8)
        self.var_y = str(((tonum(self.var_y) + ((tonum(letter_of(util.sprites.stage.var_Controlkeys, 3)) * 0.8) - (tonum(letter_of(util.sprites.stage.var_Controlkeys, 4)) * 0.8))) * 0.8))
        self.xpos += self.var_x
        self.ypos += tonum(self.var_y)
        if self.get_touching(util, "Gate"):
            self.xpos += (0 - (self.var_x * 1.1))
            self.var_x = 0
            self.ypos += (0 - (tonum(self.var_y) * 1.1))
            self.var_y = "0"
            await self.my_Debug(util, )
        self.costume.switch("Blue-Ball-light")
        self.sounds.set_volume(100)

    @on_green_flag
    async def green_flag(self, util):
        self.var_x = 0
        self.var_y = "0"
        self.gotoxy(0, -100)
        self.costume.switch("Blue-Ball")
        self.back_layer(util)

    @warp
    async def my_Debug(self, util, ):
        while not not self.get_touching(util, "Gate"):
            self.xpos += -1


@sprite('Gate')
class SpriteGate(Target):
    """Sprite Gate"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -159
        self._ypos = -4
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Gate-Debug",
                'path': "ff66f123e427116db2f315f3330e3909.svg",
                'center': (12, 48),
                'scale': 1
            },
            {
                'name': "Gate-light",
                'path': "3737cd9c8d8a857b04982fd93a75ba57.svg",
                'center': (12, 48),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 6

    @on_green_flag
    async def green_flag(self, util):
        self.front_layer(util)
        self.change_layer(util, -3)

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        self.gotoxy(tonum(util.sprites["Gate-light"].var_x), tonum(util.sprites["Gate-light"].var_y))


@sprite('Gate-light')
class SpriteGatelight(Target):
    """Sprite Gate-light"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -159
        self._ypos = -4
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Gate-light",
                'path': "3737cd9c8d8a857b04982fd93a75ba57.svg",
                'center': (12, 48),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = -159
        self.var_y = -4
        self.var_Gatenum = 5



        self.sprite.layer = 7

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        self.gotoxy(self.var_x, self.var_y)
        if lt(self.distance_to(util, "Red-Ball"), 10):
            util.send_broadcast("Gate")
            util.sprites.stage.var_Score += 1
        if lt(self.distance_to(util, "Yellow-Ball"), 10):
            util.send_broadcast("Gate-Yel")
            util.sprites.stage.var_Score += 3

    @on_green_flag
    async def green_flag(self, util):
        self.var_x = 0
        self.var_y = 0
        self.front_layer(util)
        self.change_layer(util, -3)
        self.var_Gatenum = 1
        util.sprites.stage.var_Score = 0
        self.gotoxy(0, 0)

    @on_broadcast('gate')
    async def broadcast_Gate(self, util):
        self.var_Gatenum += 1
        self.var_x = pick_rand(-180, 180)
        self.var_y = pick_rand(-120, 120)

    @on_broadcast('gate-yel')
    async def broadcast_GateYel(self, util):
        self.var_Gatenum += 1
        self.var_x = pick_rand(-180, 180)
        self.var_y = pick_rand(-120, 120)


@sprite('Control by')
class SpriteControlby(Target):
    """Sprite Control by"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 180
        self._ypos = 120
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 70, "all around", [
            {
                'name': "Mobile",
                'path': "ae6d59d072ab1f8ca129898a94c6b704.svg",
                'center': (258, 60),
                'scale': 1
            },
            {
                'name': "Keyboard",
                'path': "f6c5afd01723dc18c0ac45f349b729fa.svg",
                'center': (258, 60),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 10

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        if eq(util.sprites.stage.var_Controlby, "Keyboard"):
            while True:
                util.sprites.stage.var_Controlkeys = (str((0 + tonum(util.inputs["right arrow"]))) + (str((0 + tonum(util.inputs["left arrow"]))) + (str((0 + tonum(util.inputs["up arrow"]))) + str((0 + tonum(util.inputs["down arrow"]))))))
                self.sounds.set_volume(100)

                await self.yield_()
        else:
            while True:
                util.sprites.stage.var_Controlkeys = (str((0 + tonum((util.inputs.mouse_down and lt(util.sprites["Player"].xpos, (util.inputs.mouse_x + 20)))))) + (str((0 + tonum((util.inputs.mouse_down and lt((util.inputs.mouse_x - 20), util.sprites["Player"].xpos))))) + (str((0 + tonum((util.inputs.mouse_down and lt(util.sprites["Player"].ypos, (util.inputs.mouse_y + 20)))))) + str((0 + tonum((util.inputs.mouse_down and lt((util.inputs.mouse_y - 20), util.sprites["Player"].ypos))))))))
                self.sounds.set_volume(100)

                await self.yield_()

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True
        self.front_layer(util)
        self.costume.switch(util.sprites.stage.var_Controlby)
        self.gotoxy(180, 120)

    @on_clicked
    async def sprite_clicked(self, util):
        if lt(self.costume.number, 3):
            if eq(util.sprites.stage.var_Controlby, "Mobile"):
                util.sprites.stage.var_Controlby = "Keyboard"
                self.costume.switch(util.sprites.stage.var_Controlby)
            else:
                util.sprites.stage.var_Controlby = "Mobile"
                self.costume.switch(util.sprites.stage.var_Controlby)


@sprite('Timer')
class SpriteTimer(Target):
    """Sprite Timer"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 224
        self._ypos = -150
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 100, "all around", [
            {
                'name': "1",
                'path': "9dbeb028d08e9d548ac07e9da6535634.png",
                'center': (5, 17),
                'scale': 2
            },
            {
                'name': "2",
                'path': "2c93d9f2a155a77964e584228db7a039.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "3",
                'path': "8d2e84838fab689fc9622ccccd8eec1b.png",
                'center': (10, 17),
                'scale': 2
            },
            {
                'name': "4",
                'path': "3d3171a074e810241fd13342b35dd23f.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "5",
                'path': "8a4dd802cda954f5ecb9a257428f4c33.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "6",
                'path': "1497e07f7777e0732a2838cf814fbc2c.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "7",
                'path': "9ca869c2c3ef6f0ef9ee0dc0fdf19728.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "8",
                'path': "d896e937540f0307a3c3908bbe15a7d7.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "9",
                'path': "2936dac6b37c29748afd7635b16a7416.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "0",
                'path': "af554e3fe38873d0df02bf8bcac41a08.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': ".",
                'path': "c2cb1b652ac3c72576c312bbf0f6cc4b.png",
                'center': (5, -7),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 0



        self.sprite.layer = 2

    @warp
    async def my_Timer(self, util, arg_val, arg_x, arg_y):
        self.gotoxy(arg_x, arg_y)
        self.var_i = len(str(arg_val))
        for _ in range(len(str(arg_val))):
            self.costume.switch(letter_of(str(arg_val), toint(self.var_i)))
            self.xpos += -16
            self.pen.stamp(util)
            self.var_i += -1

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        await self.my_Timer(util, div(toint((((util.sprites.stage.var_Starttimer + 60) - util.timer()) * 10000)), 10000), 240, -150)

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        util.sprites.stage.var_Starttimer = util.timer()
        while not gt(0, ((util.sprites.stage.var_Starttimer + 60) - util.timer())):
            self.pen.clear_all()
            await util.send_broadcast_wait("Stamp")

            await self.yield_()
        util.send_broadcast("Finish")

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('finish')
    async def broadcast_Finish(self, util):
        while True:
            self.pen.clear_all()
            await self.my_Timer(util, 0, 240, -150)

            await self.yield_()


@sprite('Score')
class SpriteScore(Target):
    """Sprite Score"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 157
        self._ypos = -115
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 120, "all around", [
            {
                'name': "1",
                'path': "9dbeb028d08e9d548ac07e9da6535634.png",
                'center': (5, 17),
                'scale': 2
            },
            {
                'name': "2",
                'path': "2c93d9f2a155a77964e584228db7a039.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "3",
                'path': "8d2e84838fab689fc9622ccccd8eec1b.png",
                'center': (10, 17),
                'scale': 2
            },
            {
                'name': "4",
                'path': "3d3171a074e810241fd13342b35dd23f.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "5",
                'path': "8a4dd802cda954f5ecb9a257428f4c33.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "6",
                'path': "1497e07f7777e0732a2838cf814fbc2c.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "7",
                'path': "9ca869c2c3ef6f0ef9ee0dc0fdf19728.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "8",
                'path': "d896e937540f0307a3c3908bbe15a7d7.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "9",
                'path': "2936dac6b37c29748afd7635b16a7416.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': "0",
                'path': "af554e3fe38873d0df02bf8bcac41a08.png",
                'center': (12, 17),
                'scale': 2
            },
            {
                'name': ".",
                'path': "c2cb1b652ac3c72576c312bbf0f6cc4b.png",
                'center': (5, -7),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 3



        self.sprite.layer = 13

    @warp
    async def my_Timer(self, util, arg_val, arg_x, arg_y):
        self.gotoxy(arg_x, arg_y)
        self.var_i = 1
        for _ in range(len(str(arg_val))):
            self.costume.switch(letter_of(str(arg_val), toint(self.var_i)))
            self.xpos += 16
            self.front_layer(util)
            self.create_clone_of(util, "_myself_")
            self.var_i += 1

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        if not False:
            self.delete_clone(util)
        await self.my_Timer(util, util.sprites.stage.var_Score, -240, -150)

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('show1')
    async def broadcast_show1_1(self, util):
        self.costume.set_effect('brightness', -200)
        await self.my_Timer(util, util.sprites.stage.var_Score, -16, 15)

    @on_broadcast('show2')
    async def broadcast_show2_1(self, util):
        self.costume.set_effect('brightness', -200)
        await self.my_Timer(util, util.sprites.stage.var_WR, 125, -115)

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True


@sprite('Red-Ball')
class SpriteRedBall(Target):
    """Sprite Red-Ball"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -127.13678982790714
        self._ypos = -4.350697131173088
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "Red-Ball",
                'path': "de582e253f071d1ec3d8dae4e7b0b0c8.svg",
                'center': (17, 17),
                'scale': 1
            },
            {
                'name': "Red-Ball-light",
                'path': "25c2a51a1519fb37dacd7e4659db39cb.svg",
                'center': (34, 34),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = -0.9048874193275953
        self.var_y = "-0.06717071640582488"



        self.sprite.layer = 4

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        await self.my_Chara(util, )

    @warp
    async def my_Chara(self, util, ):
        self.costume.switch("Red-Ball")
        if self.get_touching(util, "Player"):
            self.var_x = div((util.sprites["Player"].xpos - self.xpos), 40)
            self.var_y = str(div((util.sprites["Player"].ypos - self.ypos), 40))
        self.var_x = (self.var_x * 0.8)
        self.var_y = str((tonum(self.var_y) * 0.8))
        self.xpos += self.var_x
        self.ypos += tonum(self.var_y)
        if self.get_touching(util, "Gate"):
            self.xpos += (0 - self.var_x)
            self.var_x = 0
            self.ypos += (0 - tonum(self.var_y))
            self.var_y = "0"
            await self.my_Debug(util, )
        else:
            pass
        self.costume.switch("Red-Ball-light")
        self.sounds.set_volume(100)

    @on_green_flag
    async def green_flag(self, util):
        self.var_x = 0
        self.var_y = "0"
        self.gotoxy(-100, -100)

    @warp
    async def my_Debug(self, util, ):
        while not not self.get_touching(util, "Gate"):
            self.xpos += -1

    @on_clone_start
    async def clone_start(self, util):
        for _ in range(20):
            self.xpos += (self.var_x * 3)
            self.ypos += (tonum(self.var_y) * 3)
            self.costume.size += 20
            self.costume.change_effect('ghost', 5)
            self.sounds.set_volume(100)

            await self.yield_()
        self.delete_clone(util)

    @on_broadcast('gate')
    async def broadcast_Gate(self, util):
        self.create_clone_of(util, "_myself_")
        self.gotoxy(pick_rand(-180, 180), pick_rand(-120, 120))


@sprite('Yellow-Ball')
class SpriteYellowBall(Target):
    """Sprite Yellow-Ball"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -56.508445051013126
        self._ypos = -11.264344603584735
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "Yellow-Ball",
                'path': "701ae0eb86cc3e9ac091764e72f14157.svg",
                'center': (17, 17),
                'scale': 1
            },
            {
                'name': "Yellow-Ball-light",
                'path': "899496c0fbdc8cd7e83163dc56afe14e.svg",
                'center': (34, 34),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = 0
        self.var_y = 0



        self.sprite.layer = 3

    @on_broadcast('stamp')
    async def broadcast_Stamp(self, util):
        if eq((tonum(util.sprites["Gate-light"].var_Gatenum) % 3), 0):
            self.shown = True
            await self.my_Chara(util, )
        else:
            self.shown = False

    @warp
    async def my_Chara(self, util, ):
        self.costume.switch("Yellow-Ball")
        if self.get_touching(util, "Player"):
            self.var_x = div((util.sprites["Player"].xpos - self.xpos), 40)
            self.var_y = div((util.sprites["Player"].ypos - self.ypos), 40)
        self.var_x = (self.var_x * 0.8)
        self.var_y = (self.var_y * 0.8)
        self.xpos += self.var_x
        self.ypos += self.var_y
        if self.get_touching(util, "Gate"):
            self.xpos += (0 - self.var_x)
            self.var_x = 0
            self.ypos += (0 - self.var_y)
            self.var_y = 0
            await self.my_Debug(util, )
        else:
            pass
        self.costume.switch("Yellow-Ball-light")

    @on_green_flag
    async def green_flag(self, util):
        self.var_x = 0
        self.var_y = 0
        self.gotoxy(-100, -100)

    @warp
    async def my_Debug(self, util, ):
        while not not self.get_touching(util, "Gate"):
            self.xpos += -1

    @on_clone_start
    async def clone_start(self, util):
        for _ in range(20):
            self.shown = True
            self.xpos += (self.var_x * 3)
            self.ypos += (self.var_y * 3)
            self.costume.size += 20
            self.costume.change_effect('ghost', 5)
            self.sounds.set_volume(100)

            await self.yield_()
        self.delete_clone(util)

    @on_broadcast('gate-yel')
    async def broadcast_GateYel(self, util):
        self.create_clone_of(util, "_myself_")


@sprite('Result')
class SpriteResult(Target):
    """Sprite Result"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -0.42708931355345625
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "コスチューム1",
                'path': "f0e59d02aa37cc42966b653900eddaf2.svg",
                'center': (240, 180),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 12

    @on_broadcast('finish')
    async def broadcast_Finish(self, util):
        self.front_layer(util)
        if lt(util.sprites.stage.var_WR, util.sprites.stage.var_Score):
            util.sprites.stage.var_WR = util.sprites.stage.var_Score
        self.gotoxy(0, -900)
        self.shown = True
        for _ in range(30):
            self.ypos += div((0 - self.ypos), 5)
            self.sounds.set_volume(100)

            await self.yield_()
        util.send_broadcast("Show1")
        util.send_broadcast("Show2")

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False


@sprite('Fav & Lov')
class SpriteFavLov(Target):
    """Sprite Fav & Lov"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "コスチューム1",
                'path': "22ddb269fd37a02c8710d2277b9379f4.svg",
                'center': (240, -149),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "ポップ",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 11

    @on_green_flag
    async def green_flag(self, util):
        await self.sleep(0)
        self.front_layer(util)
        self.shown = True

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False


@sprite('rittai')
class Spriterittai(Target):
    """Sprite rittai"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "コスチューム1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "Crazy - JVNA & BEAUZ (NCS release)Crazy - JVNA & BEAUZ (NCS release)",
                'path': "7d2383af4ce9bddf2b06dd80e52b6be5.mp3"
            }
        ])





        self.sprite.layer = 5

    @on_broadcast('立体')
    async def broadcast_(self, util):
        while True:
            for _ in range(200):
                self.sounds.change_effect('pan', 2)

                await self.yield_()
            for _ in range(200):
                self.sounds.change_effect('pan', -2)

                await self.yield_()
            for _ in range(100):
                self.sounds.change_effect('pan', 2)

                await self.yield_()

            await self.yield_()

    @on_broadcast('(笑)')
    async def broadcast_A(self, util):
        self.sounds.set_effect('pan', 0)
        self.sounds.set_volume(100)
        util.send_broadcast("立体")
        await self.sounds.play("Crazy - JVNA & BEAUZ (NCS release)Crazy - JVNA & BEAUZ (NCS release)")




if __name__ == '__main__':
    engine.start_program()
