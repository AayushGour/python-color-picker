import tkinter as tk
import pyautogui
from pynput.mouse import Listener
from tkinter import *
import subprocess


class ColorPicker:
    white = "#ffffff"
    color_picker_frame = None
    color_picker_label = None
    color_picker_start_button = None
    color_picker_code = "000"

    def __init__(self):
        root = Tk()
        self.root = root
        root.title("Color Picker")
        white = ColorPicker.white
        # main frame
        main_frame = tk.Frame(root, bg=white,
                              height=400, width=400)
        main_frame.pack()
        main_frame.pack_propagate(0)
        main_frame.grid_propagate(0)

        # header frame
        header_frame = tk.Frame(
            main_frame, background=white, padx=10, pady=10)
        header_frame.pack(side=TOP)
        header_label = tk.Label(
            header_frame, text="Color Picker", bg=white,  font=("", 20))
        header_label.pack(side=TOP)

        # content frame
        content_frame = tk.Frame(
            main_frame, background=white, padx=10, pady=10)
        content_frame.pack(side=TOP)

        help_label = tk.Label(
            content_frame, text="Pick color from any window\n\nClick on 'Start' to start\n\nLeft / Right click to select color", bg=white, font=("", 12))
        help_label.pack(side=TOP, pady=10)

        color_frame = tk.Frame(content_frame, height=50,
                               width=50, bg=white, borderwidth=3, relief="ridge")
        color_frame.pack(side=TOP, padx=50, pady=15)
        ColorPicker.color_picker_frame = color_frame

        color_label_container = tk.Frame(content_frame, background=white)
        color_label_container.pack(side=TOP, pady=20)

        color_label = tk.Label(color_label_container, text="------",
                               font=("", 12), background=white)
        color_label.grid(row=0, column=0, )
        ColorPicker.color_picker_label = color_label

        copy_color_button = tk.Button(
            color_label_container, text="❐", font=("", 12), command=ColorPicker.copy_to_clipboard)
        copy_color_button.grid(row=0, column=1, padx=5)

        start_button = tk.Button(
            content_frame, text="Start", command=ColorPicker.start_mouse_listener)
        start_button.pack(side=TOP)
        ColorPicker.color_picker_start_button = start_button

        root.geometry("400x400")
        root.mainloop()

    def copy_to_clipboard():
        command = "echo "+ColorPicker.color_picker_code+"|clip"
        subprocess.check_call(command, shell=True)

    def rgb_to_hex(rgb):
        return ('{:02X}{:02X}{:02X}').format(rgb[0], rgb[1], rgb[2])

    def on_move(x, y):
        im = pyautogui.screenshot(region=(x, y, 2, 2))
        pix = im.load()
        color = "#"+ColorPicker.rgb_to_hex(pix[1, 1])
        ColorPicker.color_picker_frame.config(background=color)
        ColorPicker.color_picker_label.config(text=color)

        # print(pix[1, 1])
        # print(x, y)  # Get the width and hight of the image for iterating over
        # print(ColorPicker.rgb_to_hex(pix[1, 1]))

    def on_click(x, y, button, pressed):
        # print(x, y, button, pressed)
        im = pyautogui.screenshot(region=(x, y, 2, 2))
        pix = im.load()
        color = "#"+ColorPicker.rgb_to_hex(pix[1, 1])
        ColorPicker.color_picker_frame.config(background=color)
        ColorPicker.color_picker_label.config(text=color)
        ColorPicker.color_picker_start_button['state'] = NORMAL
        ColorPicker.color_picker_code = color
        # print(pix[1, 1])
        # print(ColorPicker.rgb_to_hex(pix[1, 1]))
        # pynput.mouse.Listener.stop()
        # sys.exit()
        return False

    def start_mouse_listener():
        ColorPicker.color_picker_start_button['state'] = DISABLED
        ColorPicker.color_picker_code = None
        mouse_listener = Listener(
            on_move=ColorPicker.on_move, on_click=ColorPicker.on_click)
        try:
            mouse_listener.start()
        except:
            ColorPicker.color_picker_start_button['state'] = NORMAL
            mouse_listener.stop()
        # with Listener(on_move=ColorPicker.on_move, on_click=ColorPicker.on_click) as listener:
        #     listener.join()
    # try:
    #     mouse_listener.wait()
    # finally:
    #     mouse_listener.stop()
    #         listener.start()
    #     except:
    #         print("Exception Occurred")
    #         listener.stop()

    # pyautogui.displayMousePosition()
    # try:
    #     while True:
    #         x, y = pyautogui.position().x, pyautogui.position().y
    #         im = pyautogui.screenshot(region=(x, y, 2, 2))
    #         # im = Image.open('dead_parrot.jpg')  # Can be many different formats.
    #         pix = im.load()
    #         print(x, y)  # Get the width and hight of the image for iterating over
    #         print(pix[1, 1])
    #         print(rgb_to_hex(pix[1, 1]))
    #         # im.save("./test.png")
    #         time.sleep(0.1)
    # except KeyboardInterrupt:
    #     print("\n")


colorPicker = ColorPicker()
