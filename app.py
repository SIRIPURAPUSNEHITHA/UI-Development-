import tkinter as tk
from tkinter import filedialog
from visualization import visualize_point_cloud

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Point Cloud Files", "*.ply *.pcd *.xyz")])
    if file_path:
        visualize_point_cloud(file_path)

# Create the UI
root = tk.Tk()
root.title("Open3D Point Cloud Viewer")
root.geometry("300x150")

label = tk.Label(root, text="Open3D Point Cloud Viewer", font=("Arial", 14))
label.pack(pady=10)

btn_open = tk.Button(root, text="Open Point Cloud", command=open_file, font=("Arial", 12))
btn_open.pack(pady=20)

root.mainloop()
