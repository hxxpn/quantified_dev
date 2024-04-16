
from AppKit import NSWorkspace
from pynput import keyboard, mouse


def on_press(key):
    print(f'pressing {key=}')

def on_click(x,y,button, pressed):
    print(f"mouse coords at: ({x}, {y})")


def main():
    print('Quantified dev daemon starting....')

    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()

    print('Closing down dev daemon, bai!')


if __name__ == '__main__':
    main()