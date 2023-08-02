import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Hermie Adventures")
window.geometry("600x600")

class Instant_Frame_Probably(tk.Frame):
    def __init__(self, master, photo):
        tk.Frame.__init__(self, master)

        self.image = Image.open(photo).convert("RGBA")

        width, height = self.image.size
        self.left = 0
        self.upper = 0
        lower = height
        right = width/2

        cropped_image = self.image.crop([self.left, self.upper, right, lower])
        self.revived_hermie = cropped_image.copy()
        self.background_image = ImageTk.PhotoImage(cropped_image)

        self.background = tk.Label(self, image = self.background_image)
        self.background.pack(fill = tk.BOTH, expand=tk.YES)
        #self.background.bind('<Configure>', self.resize_hermie)
        #window.bind("<Up>", self.jump)
        overall_hermster_size = (int(32 * 3), int(32 * 3))
        self.image = self.revived_hermie.resize((overall_hermster_size))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

        self.x = 0
        self.y = 0
        self.hermie_canvas = tk.Canvas(window, width=32, height=32)
        self.hermie_canvas.pack()
        self.moving_hermie = self.hermie_canvas.create_image(self.x, self.y, anchor=tk.NW, image = self.background_image)

    def Instant_Crop_Lol(self):
        pass

    def resize_hermie(self, event):
        new_width_hermster = event.width
        new_height_hermster = event.height
        print(event.width, event.height)
        if event.width <= 1920:
            overall_hermster_size = (int(new_width_hermster * 0.05), int(new_height_hermster * 0.10))
        self.image = self.revived_hermie.resize((overall_hermster_size))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image = self.background_image)

def jump(event):
    global e
    #self.y = 20
   # self.hermie_canvas.move(self.moving_hermie, self.x, self.y)
   # self.
  #  print(self.hermie_canvas.move)
    e.place(y = 80)


e = Instant_Frame_Probably(window, "Hermie_Crawling.png")
e.pack(fill = tk.BOTH, expand = tk.YES)
window.bind("<Up>", jump)

window.mainloop()
