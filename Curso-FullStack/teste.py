import tkinter as tk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, padx=20, pady=20,
          fill=tk.BOTH, expand=True)

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, padx=20, pady=20,
          fill=tk.BOTH, expand=True)

root.mainloop()