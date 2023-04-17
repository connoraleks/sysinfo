from tkinter import Canvas, Frame

class RoundedFrame(Frame):
    def __init__(self, master=None, radius=10, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self._canvas = Canvas(self, bd=0, highlightthickness=0, **kwargs)
        self._canvas.grid(sticky="nsew")
        self.radius = radius
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.bind("<Configure>", self.update_corners)

    def update_corners(self, event=None):
        width = self.winfo_width()
        height = self.winfo_height()
        self._canvas.delete("all")

        self._canvas.create_arc((0, 0, self.radius * 2, self.radius * 2), start=90, extent=90, outline="", fill=self["bg"])
        self._canvas.create_arc((width - self.radius * 2, 0, width, self.radius * 2), start=0, extent=90, outline="", fill=self["bg"])
        self._canvas.create_arc((0, height - self.radius * 2, self.radius * 2, height), start=180, extent=90, outline="", fill=self["bg"])
        self._canvas.create_arc((width - self.radius * 2, height - self.radius * 2, width, height), start=270, extent=90, outline="", fill=self["bg"])

        self._canvas.create_rectangle(0, self.radius, width, height - self.radius, outline="", fill=self["bg"])
        self._canvas.create_rectangle(self.radius, 0, width - self.radius, height, outline="", fill=self["bg"])
