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
        self.printEvent(f"sensorupdate (common, sensor)")
        return super().sensorupdate(common, sensor)

    # События клавиатуры

    def keydown(self, common: CommonEvent, key: KeyboardEvent) -> None:
        self.printEvent(f"keydown (common, key)")
        return super().keydown(common, key)

    def keyup(self, common: CommonEvent, key: KeyboardEvent) -> None:
        self.printEvent(f"keyup (common, key)")
        return super().keyup(common, key)

    def textediting(self, common: CommonEvent, edit: TextEditingEvent) -> None:
        """
        SDL_TEXTEDITING
        Редактирование текста (IME, композиция)
        """

    def textinput(self, common: CommonEvent, text: TextInputEvent) -> None:
        """
        SDL_TEXTINPUT
        Ввод текста (после завершения IME)
        """

    def keymapchanged(self, common: CommonEvent) -> None:
        """
        SDL_KEYMAPCHANGED
        Раскладка клавиатуры изменилась системой
        """

    def textediting_ext(self, common: CommonEvent, editExt: TextEditingExtEvent) -> None:
        """
        SDL_TEXTEDITING_EXT
        Расширенное редактирование текста (IME)
        """

    # События мыши

    def mousemotion(self, common: CommonEvent, motion: MouseMotionEvent) -> None:
        """
        SDL_MOUSEMOTION
        Перемещение мыши
        """

    def mousebuttondown(self, common: CommonEvent, button: MouseButtonEvent) -> None:
        """
        SDL_MOUSEBUTTONDOWN
        Кнопка мыши нажата
        """

    def mousebuttonup(self, common: CommonEvent, button: MouseButtonEvent) -> None:
        """
        SDL_MOUSEBUTTONUP
        Кнопка мыши отпущена
        """

    def mousewheel(self, common: CommonEvent, wheel: MouseWheelEvent) -> None:
        """
        SDL_MOUSEWHEEL
        Прокрутка колеса мыши
        """

    # Джойстик (классический API)
    def joyaxismotion(self, common: CommonEvent, jaxis: JoyAxisEvent) -> None:
        """
        SDL_JOYAXISMOTION
        Движение оси джойстика
        """

    def joyballmotion(self, common: CommonEvent, jball: JoyBallEvent) -> None:
        """
        SDL_JOYBALLMOTION
        Движение трекбола
        """

    def joyhatmotion(self, common: CommonEvent, jhat: JoyHatEvent) -> None:
        """
        SDL_JOYHATMOTION
        Изменение POV-переключателя (hat)
        """

    def joybuttondown(self, common: CommonEvent, jbutton: JoyButtonEvent) -> None:
        """
        SDL_JOYBUTTONDOWN
        Кнопка джойстика нажата
        """

    def joybuttonup(self, common: CommonEvent, jbutton: JoyButtonEvent) -> None:
        """
        SDL_JOYBUTTONUP
        Кнопка джойстика отпущена
        """

    def joydeviceadded(self, common: CommonEvent, jdevice: JoyDeviceEvent) -> None:
        """
        SDL_JOYDEVICEADDED
        Джойстик подключён
        """

    def joydeviceremoved(self, common: CommonEvent, jdevice: JoyDeviceEvent) -> None:
        """
        SDL_JOYDEVICEREMOVED
        Джойстик отключён
        """
        
    def joybatteryupdated(self, common: CommonEvent, jbattery: JoyBatteryEvent) -> None:
        """
        SDL_JOYBATTERYUPDATED
        Изменился уровень заряда джойстика
        """

    # Контроллеры (Game Controller API, SDL2)

    def controlleraxismotion(self, common: CommonEvent, caxis: ControllerAxisEvent) -> None:
        """
        SDL_CONTROLLERAXISMOTION
        Движение оси контроллера
        """

    def controllerbuttondown(self, common: CommonEvent, cbutton: ControllerButtonEvent) -> None:
        """
        SDL_CONTROLLERBUTTONDOWN
        Кнопка контроллера нажата
        """

    def controllerbuttonup(self, common: CommonEvent, cbutton: ControllerButtonEvent) -> None:
        """
        SDL_CONTROLLERBUTTONUP
        Кнопка контроллера отпущена
        """

    def controllerdeviceadded(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        """
        SDL_CONTROLLERDEVICEADDED
        Контроллер подключён
        """

    def controllerdeviceremoved(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        """
        SDL_CONTROLLERDEVICEREMOVED
        Контроллер отключён
        """

    def controllerdeviceremapped(self, common: CommonEvent, cdevice: ControllerDeviceEvent) -> None:
        """
        SDL_CONTROLLERDEVICEREMAPPED
        Раскладка контроллера обновлена
        """

    def controllertouchpaddown(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        """
        SDL_CONTROLLERTOUCHPADDOWN
        Тачпад контроллера нажат
        """

    def controllertouchpadmotion(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        """
        SDL_CONTROLLERTOUCHPADMOTION
        Палец движется по тачпаду контроллера 
        """

    def controllertouchpadup(self, common: CommonEvent, ctouchpad: ControllerTouchpadEvent) -> None:
        """
        SDL_CONTROLLERTOUCHPADUP
        Палец отпущен с тачпада контроллера
        """

    def controllersensorupdate(self, common: CommonEvent, csensor: ControllerSensorEvent) -> None:
        """
        SDL_CONTROLLERSENSORUPDATE
        Обновились данные сенсора контроллера
        """

    # Сенсорный ввод и жесты

    def fingerdown(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        """
        SDL_FINGERDOWN
        Палец коснулся экрана
        """

    def fingerup(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        """
        SDL_FINGERUP
        Палец поднят
        """

    def fingermotion(self, common: CommonEvent, tfinger: TouchFingerEvent) -> None:
        """
        SDL_FINGERMOTION
        Палец движется
        """

    def multigesture(self, common: CommonEvent, mgesture: MultiGestureEvent) -> None:
        """
        SDL_MULTIGESTURE
        Мультитач-жест (щипок, вращение)
        """

    def dollargesture(self, common: CommonEvent, dgesture: DollarGestureEvent) -> None:
        """
        SDL_DOLLARGESTURE
        Распознан долларовый жест (1-жест)
        """

    def dollarrecord(self, common: CommonEvent, dgesture: DollarGestureEvent) -> None:
        """
        SDL_DOLLARRECORD
        Записан долларовый жест
        """

    # Аудиоустройства

    def audiodeviceadded(self, common: CommonEvent, adevice: AudioDeviceEvent) -> None:
        """
        SDL_AUDIODEVICEADDED
        Аудиоустройство подключено
        """

    def audiodeviceremoved(self, common: CommonEvent, adevice: AudioDeviceEvent) -> None:
        """
        SDL_AUDIODEVICEREMOVED
        Аудиоустройство отключено
        """

    # Drag and Drop (перетаскивание файлов/текста)

    def dropbegin(self, common: CommonEvent, drop: DropEvent) -> None:
        """
        SDL_DROPBEGIN
        Начало перетаскивания
        """

    def dropfile(self, common: CommonEvent, drop: DropEvent) -> None:
        """
        SDL_DROPFILE
        Файл перетащен в окно
        """

    def droptext(self, common: CommonEvent, drop: DropEvent) -> None:
        """
        SDL_DROPTEXT
        Текст перетащен в окно
        """

    def dropcomplete(self, common: CommonEvent, drop: DropEvent) -> None:
        """
        SDL_DROPCOMPLETE
        Перетаскивание завершено
        """

def main(dir: str) -> int:
    app = App(size=(1000, 600), scene=[MainScene])
    app.start()
