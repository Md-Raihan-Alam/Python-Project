import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock.configure(text=current_time)
    clock.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
clock = tk.Label(root, font=("times", 50, "bold"), bg="white")
clock.pack(fill="both", expand=1)
update_time()
root.mainloop()
