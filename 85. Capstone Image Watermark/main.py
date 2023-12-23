import pathlib
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import Tk, Label, Button, Entry, Radiobutton, filedialog, StringVar, messagebox

FONT_NAME = "Arial"
filetypes = (
        ('images', '*.jpg;*.png;*.jpeg;*.pcx|*.gif|*.icns|*.tga|*.tiff|*.webp'),
    )
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'orange']

global input_e
global output_e
global watermark_choice
global watermark_image_l
global watermark_image_e
global watermark_image_b
global watermark_text_l
global watermark_text_e

def open_input() -> None:
    input_path = filedialog.askopenfilename(filetypes=filetypes)
    if input_path:
        file_type = pathlib.Path(input_path).suffix
        output_path = input_path[:input_path.rfind(file_type)] + '_watermarked' + file_type
        input_e.insert(0, input_path)
        output_e.insert(0, output_path)

def open_watermark_image() -> None:
    watermark_path = filedialog.askopenfilename(filetypes=filetypes)
    if watermark_path:
        watermark_image_e.insert(0, watermark_path)

def check_watermark() -> None:
    if watermark_choice.get() == 'text':
        if pathlib.Path(input_e.get()).is_file() and output_e.get() != "" and watermark_text_e.get() != '':
            put_watermark()
        else:
            messagebox.showerror(title='Error!', message="Provide necessary information (image path, output image path, watermark text)", parent=main_window)
    if watermark_choice.get() == 'image':
        if pathlib.Path(input_e.get()).is_file() and output_e.get() != "" and pathlib.Path(input_e.get()).is_file() :
            put_watermark()
        else:
            messagebox.showerror(title='Error!', message="Provide necessary information (image path, output image path, watermark image path)", parent=main_window)

def hide_watermark_widgets(var_name, var_index, operation) -> None:
    print(f"Var_name: {var_name}, var_index: {var_index}, operation: {operation}, watermark_choice: {watermark_choice.get()}")
    if watermark_choice.get() == 'text':
        watermark_image_l.grid_remove()
        watermark_image_e.grid_remove()
        watermark_image_b.grid_remove()
        watermark_text_l.grid(column=0, row=6, sticky="E")
        watermark_text_e.grid(column=1, row=6, columnspan=2)

    if watermark_choice.get() == 'image':
        watermark_image_l.grid(column=0, row=5, sticky="E")
        watermark_image_e.grid(column=1, row=5, columnspan=2)
        watermark_image_b.grid(column=3, row=5, sticky="W")
        watermark_text_l.grid_remove()
        watermark_text_e.grid_remove()

def put_watermark() -> None:
    transparency = 64
    if watermark_choice.get() == 'text':
        input_image = Image.open(input_e.get()).convert("RGBA")
        
        txt = Image.new('RGBA', input_image.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt)

        w, h = input_image.size
        x, y = w // 2, h // 2
        font_size = 50

        font = ImageFont.truetype("arial.ttf", int(font_size))

        draw.text((x, y), watermark_text_e.get(), fill=(255, 0, 0, transparency), font=font, anchor='ms', stroke_width=2)
        
        watermarked_image = Image.alpha_composite(input_image, txt)
        watermarked_image.save(output_e.get())

        input_image.close()

        messagebox.showinfo(message=f"Watermarked image was successfully saved at:\n{output_e.get()}")

    if watermark_choice.get() == 'image':
        size_fraction = 0.15
        margin = 0.05
        input_image = Image.open(input_e.get())
        watermark_image = Image.open(watermark_image_e.get())
        watermark_aspect_ratio = watermark_image.size[0] / watermark_image.size[1]
        w, h = input_image.size
        watermark_w, watermark_h = int(w * size_fraction), int(h * size_fraction)
        watermark_image.thumbnail((watermark_w, watermark_h))
        watermark_image.putalpha(transparency)

        position_x = int(w - watermark_w - w * margin)
        position_y = int(h - watermark_h - h * margin)

        input_image.paste(watermark_image, (position_x, position_y), mask=watermark_image)
        
        input_image.save(output_e.get())

        input_image.close()
        watermark_image.close()

        messagebox.showinfo(message=f"Watermarked image was successfully saved at:\n{output_e.get()}")

if __name__ == '__main__':
    main_window = Tk()
    main_window.title("Put Watermark")
    main_window.config(padx=20, pady=30)

    input_l = Label(text="Input image:")
    input_l.grid(column=0, row=0, sticky="E")
    input_e = Entry(width=50)
    input_e.grid(column=1, row=0, columnspan=2)
    input_b = Button(text="Open input image", command=open_input, font=(FONT_NAME, 11, 'normal'))
    input_b.grid(column=3, row=0, sticky="W")
    output_l = Label(text="Output image:")
    output_l.grid(column=0, row=1, sticky="E")
    output_e = Entry(width=50)
    output_e.grid(column=1, row=1, columnspan=2)

    watermark_choice = StringVar(master=main_window, value='text')
    watermark_choice.trace_add(mode='write', callback=hide_watermark_widgets)
    watermark_text_color = StringVar(master=main_window, value='red')

    choice_l = Label(master=main_window, text="Choose watermark method:", font=(FONT_NAME, 11, "bold"))
    choice_l.grid(column=1, row=2, sticky='W')
    picture_r = Radiobutton(master=main_window, text="Picture", variable=watermark_choice, value='image', font=(FONT_NAME, 11, "bold"))
    picture_r.grid(column=1, row=3, sticky='W')
    text_r = Radiobutton(master=main_window, text="Text", variable=watermark_choice, value='text', font=(FONT_NAME, 11, "bold"))
    text_r.grid(column=1, row=4, sticky='W')

    watermark_image_l = Label(master=main_window, text="Watermark image:")
    watermark_image_e = Entry(master=main_window, width=50)
    watermark_image_b = Button(master=main_window, text="Open watermark image", command=open_watermark_image, font=(FONT_NAME, 11, 'normal'))

    watermark_text_l = Label(master=main_window, text="Watermark text:")
    watermark_text_l.grid(column=0, row=6, sticky="E")
    watermark_text_e = Entry(master=main_window, width=39, font=(FONT_NAME, 11, "bold"), fg="red")
    watermark_text_e.insert(0, "Input WaterMarkt Text Here")
    watermark_text_e.grid(column=1, row=6, columnspan=2)

    put_watermark_b = Button(master=main_window, text="Put watermark", font=(FONT_NAME, 14, "bold"), command=check_watermark)
    put_watermark_b.grid(column=1, row=7, columnspan=2, pady=20)

    main_window.mainloop()
