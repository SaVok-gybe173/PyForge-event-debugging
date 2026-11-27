from PyForge.easel.app import App
from PyForge.easel.scene import Scene
from PyForge.easel.surface import Surface
from PyForge.widget.button import Button
from PyForge.widget.text import BigText
from PyForge.font import FontTTF
from PyForge.easel.object import PfObjectIMG
from  PyForge.easel.event import (Event,
        CommonEvent,
        DisplayEvent,
        WindowEvent,
        KeyboardEvent,
        TextEditingEvent,
        TextEditingExtEvent,
        TextInputEvent,
        MouseMotionEvent,
        MouseButtonEvent,
        MouseWheelEvent,
        JoyAxisEvent,
        JoyBallEvent,
        JoyHatEvent,
        JoyButtonEvent,
        JoyDeviceEvent,
        JoyBatteryEvent,
        ControllerAxisEvent,
        ControllerButtonEvent,
        ControllerDeviceEvent,
        ControllerTouchpadEvent,
        ControllerSensorEvent,
        SensorEvent,
        QuitEvent,
        UserEvent,
        SysWMEvent,
        TouchFingerEvent,
        MultiGestureEvent,
        DollarGestureEvent,
        DropEvent,
        AudioDeviceEvent
    )
import os

# класс PfObjectIMG с draw 
class Img(PfObjectIMG):
    def draw(self, win):
        win.blit(self.img, self.left_top)

class MainScene(Scene):
    def clickButtonMain(self, num: int):
        print(f"Нажата кнопка {num}!")

    def printEvent(self, text: str) -> None:
        self.list.add_text(text)

    def __init__(self, page: App):
        super().__init__(page)
        self.font = FontTTF(os.path.join("assets", "fonts", "Oswald-Regular.ttf"))


        # фон для BigText
        sur = Surface((page.size[0], page.size[1]-page.size[1]//5))
        sur.fill((125, 125, 125, 125))
        self.append(Img(page, (0, page.size[1]//5), sur))
        
        # список событий
        self.list = BigText(page, (0, page.size[1]//5), (page.size[0], page.size[1]-page.size[1]//5), self.font, color=(0,0,0))
        self.append(self.list)

    def quit(self, common: CommonEvent, quit: QuitEvent) -> bool:
        """
        SDL_QUIT
        Пользователь запросил закрытие приложения (нажал на крестик окна, Alt+F4 или эквивалент в оконной системе).
        """
        return True
    

    def app_terminating(self, common):
        self.printEvent("app_terminating (common)")
        return super().app_terminating(common)

    def app_lowmemory(self, common):
        self.printEvent("app_lowmemory (common)")
        return super().app_lowmemory(common)

    def app_willenterbackground(self, common):
        self.printEvent("app_willenterbackground (common)")
        return super().app_willenterbackground(common)

    def app_didenterbackground(self, common: CommonEvent) -> None:
        self.printEvent("app_didenterbackground (common)")
        return super().app_didenterbackground(common)

    def app_willenterforeground(self, common: CommonEvent) -> None:
        self.printEvent("app_willenterforeground (common)")
        return super().app_willenterforeground(common)

    def app_didenterforeground(self, common: CommonEvent) -> None:
        self.printEvent("app_didenterforeground (common)")
        return super().app_didenterforeground(common)


    def localechanged(self, common: CommonEvent) -> None:
        self.printEvent("localechanged (common)")
        return super().localechanged(common)

    def displayevent(self, common: CommonEvent, display: DisplayEvent) -> None:
        self.printEvent(f"displayevent (common, display) display={display.display}, event={display.event}, data1={display.data1}")
        return super().displayevent(common, display)

    def windowevent(self, common: CommonEvent, window: WindowEvent) -> None:
        self.printEvent(f"windowevent (common, window) windowID={window.windowID}, event={window.event}, data1={window.data1}, data2={window.data2}")
        return super().windowevent(common, window)

    def syswmevent(self, common: CommonEvent, syswm: SysWMEvent) -> None:
        self.printEvent(f"syswmevent (common, syswm) msg={syswm.msg}")
        return super().syswmevent(common, syswm)

    def clipboardupdate(self, common: CommonEvent) -> None:
        self.printEvent(f"clipboardupdate (common)")
        return super().clipboardupdate(common)

    def render_targets_reset(self, common: CommonEvent) -> None:
        self.printEvent(f"render_targets_reset (common)")
        return super().render_targets_reset(common)

    def render_device_reset(self, common: CommonEvent) -> None:
        self.printEvent(f"render_device_reset (common)")
        return super().render_device_reset(common)

    def sensorupdate(self, common: CommonEvent, sensor: SensorEvent) -> None:
        self.printEvent(f"sensorupdate (common, sensor) which={sensor.which}, data={sensor.data}")
        return super().sensorupdate(common, sensor)

    # События клавиатуры

    def keydown(self, common: CommonEvent, key: KeyboardEvent) -> None:
        self.printEvent(f"keydown (common, key) windowID={key.windowID}, state={key.state}, repeat={key.repeat}, keysym.scancode={key.keysym.scancode}, keysym.sym={key.keysym.sym}, keysym.mod={key.keysym.mod}, keysym.unused={key.keysym.unused}")
        return super().keydown(common, key)

    def keyup(self, common: CommonEvent, key: KeyboardEvent) -> None:
        self.printEvent(f"keyup (common, key) windowID={key.windowID}, state={key.state}, repeat={key.repeat}, keysym.scancode={key.keysym.scancode}, keysym.sym={key.keysym.sym}, keysym.mod={key.keysym.mod}, keysym.unused={key.keysym.unused}")
        return super().keyup(common, key)

    def textediting(self, common: CommonEvent, edit: TextEditingEvent) -> None:
        self.printEvent(f"textediting (common, edit) windowID={edit.windowID}, text={edit.text}, start={edit.start}, length={edit.length}")
        return super().textediting(common, edit)

    def textinput(self, common: CommonEvent, text: TextInputEvent) -> None:
        self.printEvent(f"textinput (common, text) windowID={text.windowID}, text={text.text}")
        return super().textinput(common, text)

    def keymapchanged(self, common: CommonEvent) -> None:
        self.printEvent(f"keymapchanged (common)")
        return super().keymapchanged(common)

    def textediting_ext(self, common: CommonEvent, editExt: TextEditingExtEvent) -> None:
        self.printEvent(f"textediting_ext (common, editExt) windowID={editExt.windowID} text={editExt.text}, start={editExt.start}, length={editExt.length}")
        return super().textediting_ext(common, editExt)

    # События мыши

    def mousemotion(self, common: CommonEvent, motion: MouseMotionEvent) -> None:
        #self.printEvent(f"mousemotion (common, motion) which={motion.which} state={motion.state}, x={motion.x}, y={motion.x}, xrel={motion.xrel}, yrel={motion.yrel}")
        return super().mousemotion(common, motion)

    def mousebuttondown(self, common: CommonEvent, button: MouseButtonEvent) -> None:
        self.printEvent(f"mousebuttondown (common, button) which={button.which} button={button.button}, state={button.state}, clicks={button.clicks}, x={button.x}, y={button.y}")
        return super().mousebuttondown(common, button)

    def mousebuttonup(self, common: CommonEvent, button: MouseButtonEvent) -> None:
        self.printEvent(f"mousebuttonup (common, button) which={button.which} button={button.button}, state={button.state}, clicks={button.clicks}, x={button.x}, y={button.y}")
        return super().mousebuttonup(common, button)

    def mousewheel(self, common: CommonEvent, wheel: MouseWheelEvent) -> None:
        self.printEvent(f"mousewheel (common, wheel) which={wheel.which} x={wheel.x}, y={wheel.y}, direction={wheel.direction}, preciseX={wheel.preciseX}, preciseY={wheel.preciseY}, mouseX={wheel.mouseX}, mouseY={wheel.mouseY}")
        return super().mousewheel(common, wheel)

    # Джойстик (классический API)
    def joyaxismotion(self, common: CommonEvent, jaxis: JoyAxisEvent) -> None:
        self.printEvent(f"joyaxismotion (common, jaxis) which={jaxis.which} axis={jaxis.axis}, value={jaxis.value}")
        return super().joyaxismotion(common, jaxis)

    def joyballmotion(self, common: CommonEvent, jball: JoyBallEvent) -> None:
        self.printEvent(f"joyballmotion (common, jball) which={jball.which} ball={jball.ball}, xrel={jball.xrel}, yrel={jball.yrel}")
        return super().joyballmotion(common, jball)

    def joyhatmotion(self, common: CommonEvent, jhat: JoyHatEvent) -> None:
        self.printEvent(f"joyhatmotion (common, jhat) which={jhat.which} hat={jhat.hat}, value={jhat.value}")
        return super().joyhatmotion(common, jhat)

    def joybuttondown(self, common: CommonEvent, jbutton: JoyButtonEvent) -> None:
        self.printEvent(f"joybuttondown (common, jbutton) which={jbutton.which} button={jbutton.button}, state={jbutton.state}")
        return super().joybuttondown(common, jbutton)

    def joybuttonup(self, common: CommonEvent, jbutton: JoyButtonEvent) -> None:
        self.printEvent(f"joybuttonup (common, jbutton) which={jbutton.which} button={jbutton.button}, state={jbutton.state}")
        return super().joybuttonup(common, jbutton)

    def joydeviceadded(self, common: CommonEvent, jdevice: JoyDeviceEvent) -> None:
        self.printEvent(f"joydeviceadded (common, jdevice) which={jdevice.which}")
        return super().joydeviceadded(common, jdevice)

    def joydeviceremoved(self, common: CommonEvent, jdevice: JoyDeviceEvent) -> None:
        self.printEvent(f"joydeviceremoved (common, jdevice) which={jdevice.which}")
        return super().joydeviceremoved(common, jdevice)
        
    def joybatteryupdated(self, common: CommonEvent, jbattery: JoyBatteryEvent) -> None:
        try:
            self.printEvent(f"joybatteryupdated (common, jbattery) which={jbattery.which}, level={jbattery.level}")
        except:
            self.printEvent(f"joybatteryupdated (common, jbattery) which={jbattery.which}")
        return super().joybatteryupdated(common, jbattery)

    # Контроллеры (Game Controller API, SDL2)

    def controlleraxismotion(self, common: CommonEvent, caxis: ControllerAxisEvent) -> None:
        self.printEvent(f"controlleraxismotion (common, caxis) which={caxis.which}, axis={caxis.axis}, value={caxis.value}")
        return super().controlleraxismotion(common, caxis)

    def controllerbuttondown(self, common: CommonEvent, cbutton: ControllerButtonEvent) -> None:
        self.printEvent(f"controllerbuttondown (common, cbutton) which={cbutton.which}, button={cbutton.button}, state={cbutton.state}")
        return super().controllerbuttondown(common, cbutton)

    def controllerbuttonup(self, common: CommonEvent, cbutton: ControllerButtonEvent) -> None:
        self.printEvent(f"controllerbuttonup (common, cbutton) which={cbutton.which}, button={cbutton.button}, state={cbutton.state}")
        return super().controllerbuttonup(common, cbutton)

    def controllerdeviceadded(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        self.printEvent(f"controllerdeviceadded (common, cdevice) which={cdevice.which}")
        return super().controllerdeviceadded(common, cdevice)

    def controllerdeviceremoved(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        self.printEvent(f"controllerdeviceremoved (common, cdevice) which={cdevice.which}")
        return super().controllerdeviceremoved(common, cdevice)

    def controllerdeviceremapped(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        self.printEvent(f"controllerdeviceremapped (common, cdevice) which={cdevice.which}")
        return super().controllerdeviceremapped(common, cdevice)

    def controllertouchpaddown(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        self.printEvent(f"controllertouchpaddown (common, ctouchpad) which={ctouchpad.which}, touchpad={ctouchpad.touchpad}, finger={ctouchpad.finger}, x={ctouchpad.x}, y={ctouchpad.y}, pressure={ctouchpad.pressure}")
        return super().controllertouchpaddown(common, ctouchpad)

    def controllertouchpadmotion(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        self.printEvent(f"controllertouchpadmotion (common, ctouchpad) which={ctouchpad.which}, touchpad={ctouchpad.touchpad}, finger={ctouchpad.finger}, x={ctouchpad.x}, y={ctouchpad.y}, pressure={ctouchpad.pressure}")
        return super().controllertouchpadmotion(common, ctouchpad)

    def controllertouchpadup(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        self.printEvent(f"controllertouchpadup (common, ctouchpad) which={ctouchpad.which}, touchpad={ctouchpad.touchpad}, finger={ctouchpad.finger}, x={ctouchpad.x}, y={ctouchpad.y}, pressure={ctouchpad.pressure}")
        return super().controllertouchpadup(common, ctouchpad)

    def controllersensorupdate(self, common: CommonEvent, csensor: ControllerSensorEvent) -> None:
        self.printEvent(f"controllersensorupdate (common, csensor) which={csensor.which}, sensor={csensor.sensor}, data={csensor.data}")
        return super().controllersensorupdate(common, csensor)

    # Сенсорный ввод и жесты

    def fingerdown(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        self.printEvent(f"fingerdown (common, tfinger) touchId={tfinger.touchId}, fingerId={tfinger.fingerId}, x={tfinger.x}, y={tfinger.y}, dx={tfinger.dx}, dy={tfinger.dy}, pressure={tfinger.pressure}, pressure={tfinger.pressure}")
        return super().fingerdown(common, tfinger)

    def fingerup(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        self.printEvent(f"fingerup (common, tfinger) touchId={tfinger.touchId}, fingerId={tfinger.fingerId}, x={tfinger.x}, y={tfinger.y}, dx={tfinger.dx}, dy={tfinger.dy}, pressure={tfinger.pressure}, pressure={tfinger.pressure}")
        return super().fingerup(common, tfinger)

    def fingermotion(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        self.printEvent(f"fingermotion (common, tfinger) touchId={tfinger.touchId}, fingerId={tfinger.fingerId}, x={tfinger.x}, y={tfinger.y}, dx={tfinger.dx}, dy={tfinger.dy}, pressure={tfinger.pressure}, pressure={tfinger.pressure}")
        return super().fingermotion(common, tfinger)

    def multigesture(self, common: CommonEvent, mgesture: MultiGestureEvent) -> None:
        self.printEvent(f"multigesture (common, mgesture) touchId={mgesture.touchId}, dTheta={mgesture.dTheta}, dDist={mgesture.dDist}, x={mgesture.x}, y={mgesture.y}, numFingers={mgesture.numFingers}")
        return super().multigesture(common, mgesture)

    def dollargesture(self, common: CommonEvent, dgesture: DollarGestureEvent) -> None:
        self.printEvent(f"dollargesture (common, dgesture) touchId={dgesture.touchId}, gestureId={dgesture.gestureId}, numFingers={dgesture.numFingers}, error={dgesture.error}, x={dgesture.x}, y={dgesture.y}")
        return super().dollargesture(common, dgesture)

    def dollarrecord(self, common: CommonEvent, dgesture: DollarGestureEvent) -> None:
        self.printEvent(f"dollarrecord (common, dgesture) touchId={dgesture.touchId}, gestureId={dgesture.gestureId}, numFingers={dgesture.numFingers}, error={dgesture.error}, x={dgesture.x}, y={dgesture.y}")
        return super().dollarrecord(common, dgesture)

    # Аудиоустройства

    def audiodeviceadded(self, common: CommonEvent, adevice: AudioDeviceEvent) -> None:
        self.printEvent(f"audiodeviceadded (common, adevice) which={adevice.which}, iscapture={adevice.iscapture}")
        return super().audiodeviceadded(common, adevice)

    def audiodeviceremoved(self, common: CommonEvent, adevice: AudioDeviceEvent) -> None:
        self.printEvent(f"audiodeviceremoved (common, adevice) which={adevice.which}, iscapture={adevice.iscapture}")
        return super().audiodeviceremoved(common, adevice)

    # Drag and Drop (перетаскивание файлов/текста)

    def dropbegin(self, common: CommonEvent, drop: DropEvent) -> None:
        self.printEvent(f"dropbegin (common, drop) file={drop.file}, windowID={drop.windowID}")
        return super().dropbegin(common, drop)

    def dropfile(self, common: CommonEvent, drop: DropEvent) -> None:
        self.printEvent(f"dropfile (common, drop) file={drop.file}, windowID={drop.windowID}")
        return super().dropfile(common, drop)

    def droptext(self, common: CommonEvent, drop: DropEvent) -> None:
        self.printEvent(f"droptext (common, drop) file={drop.file}, windowID={drop.windowID}")
        return super().droptext(common, drop)

    def dropcomplete(self, common: CommonEvent, drop: DropEvent) -> None:
        self.printEvent(f"dropcomplete (common, drop) file={drop.file}, windowID={drop.windowID}")
        return super().dropcomplete(common, drop)

def main(dir: str) -> int:
    app = App(size=(1000, 600), scene=[MainScene])
    app.start()
