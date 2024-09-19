import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Camera Preview with Coordinates")
        
        self.resolution = (1280, 720)
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        
        self.label = tk.Label(master, text=f"Resolution: {self.resolution[0]}x{self.resolution[1]}")
        self.label.pack()
        
        self.canvas = tk.Canvas(master, width=self.resolution[0], height=self.resolution[1])
        self.canvas.pack()
        
        self.lines = []
        self.points = []
        
        self.coordinates_label = tk.Label(master, text="Lines' coordinates: ")
        self.coordinates_label.pack()

        self.textbox1 = tk.Entry(master, width=80)
        self.textbox1.pack(pady=5)
        
        self.copy_button1 = tk.Button(master, text="Copy line-crossing-Entry Coordinates", command=self.copy_textbox1)
        self.copy_button1.pack(pady=5)       

        self.textbox2 = tk.Entry(master, width=80)
        self.textbox2.pack(pady=5)
        
        self.copy_button2 = tk.Button(master, text="Copy line-crossing-Exit Coordinates", command=self.copy_textbox2)
        self.copy_button2.pack(pady=5)
                        
        # Add this line after creating the second copy button and before the third textbox
        self.description_label = tk.Label(master, text="Please copy the coordinates to ../deepstream-occupancy-analytics/configs/nvdsanalytics_config.txt Line69 & 70")
        self.description_label.pack(pady=5)
        
        self.update_frame()
        self.canvas.bind("<Motion>", self.show_coordinates)
        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.clear_lines)
        
        self.resolution_var = tk.StringVar(value=f"{self.resolution[0]}x{self.resolution[1]}")
        self.resolution_entry = tk.Entry(master, textvariable=self.resolution_var)
        self.resolution_entry.pack()
        self.resolution_button = tk.Button(master, text="Set Resolution", command=self.set_resolution)
        self.resolution_button.pack()
        
    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            self.photo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = Image.fromarray(self.photo)
            self.photo = ImageTk.PhotoImage(self.photo)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            for line in self.lines:
                self.canvas.create_line(line[0], line[1], line[2], line[3], fill="red", width=2)
            for point in self.points:
                self.canvas.create_oval(point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3, fill="blue")
        self.master.after(10, self.update_frame)
    
    def show_coordinates(self, event):
        x, y = event.x, event.y
        self.master.title(f"Coordinates: ({x}, {y})")
    
    def add_point(self, event):
        if len(self.points) < 8:
            self.points.append((event.x, event.y))
            self.canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="blue")
            if len(self.points) % 2 == 0:
                self.lines.append((*self.points[-2], *self.points[-1]))
                self.canvas.create_line(self.points[-2], self.points[-1], fill="red", width=2)
                self.update_coordinates_label()

    def clear_lines(self, event):
        self.lines = []
        self.points = []
        self.canvas.delete("all")
        self.update_coordinates_label()
    
    def update_coordinates_label(self):
        text1 = ""
        text2 = ""
        if len(self.lines) > 0:
            text1 = ";".join(f"{line[0]};{line[1]};{line[2]};{line[3]}" for line in self.lines[:2])
        if len(self.lines) > 2:
            text2 = ";".join(f"{line[0]};{line[1]};{line[2]};{line[3]}" for line in self.lines[2:4])
        self.textbox1.delete(0, tk.END)
        self.textbox1.insert(0, text1)
        self.textbox2.delete(0, tk.END)
        self.textbox2.insert(0, text2)
    
    def copy_textbox1(self):
        text = self.textbox1.get()
        if text:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)
            self.master.update()  # ?¤@¨BÚÌ«O°Å?ªO?®e³Q§ó·s
    
    def copy_textbox2(self):
        text = self.textbox2.get()
        if text:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)
            self.master.update()  # ?¤@¨BÚÌ«O°Å?ªO?®e³Q§ó·s
    
    def set_resolution(self):
        resolution = self.resolution_var.get()
        try:
            width, height = map(int, resolution.split('x'))
            self.resolution = (width, height)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            self.canvas.config(width=width, height=height)
            self.label.config(text=f"Resolution: {width}x{height}")
        except:
            tk.messagebox.showerror("Invalid Resolution", "Please enter a valid resolution (e.g., 1280x720).")

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()

