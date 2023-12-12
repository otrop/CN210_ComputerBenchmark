from tkinter import *
import tkinter as tk
import subprocess

cpu_score = 0
cpu_runtime = 0
memory_score = 0
memory_runtime = 0
disk_score = 0
disk_runtime = 0
total_score = 0

window = tk.Tk()
window.geometry('900x500')
window.resizable(0,0)
window.title("CN210_Final")

label1 = tk.Label(master=window,  text=f"COMPUTER BENCHMARK", font=("Sukhumvit Set",20)).pack()
label2 = tk.Label(master=window,  text=f"BY ขอจบ 4 ปีได้ไหม", font=("Sukhumvit Set",17)).pack()

#def run_cpu_benchmark_script():
    #result = subprocess.run(["python", "memory_benchmark.py"], capture_output=True, text=True)
    #memory_score = result.stdout.strip()
    #return memory_score


frame = tk.Frame(master=window, width=225, height=80, relief=tk.RAISED)
frame.pack(fill=tk.BOTH, pady=5)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(0, weight=1)
button1 = tk.Button(frame,width=30, height=7 , text=f"CPU")
button1.grid(column=1, row=0)
button2 = tk.Button(frame,width=30, height=7 , text=f"MEMORY")
button2.grid(column=2, row=0)
button3 = tk.Button(frame,width=30, height=7 , text=f"DISK")
button3.grid(column=3, row=0)

box1 = tk.Label(master=window, text=f"CPU Score: {cpu_score}.").pack(pady=5)
box11 = tk.Label(master=window, text=f"CPU Runtime: {cpu_runtime}s.").pack(pady=5)
box2 = tk.Label(master=window, text=f"\nMemory Score: {memory_score}.").pack(pady=5)
box22 = tk.Label(master=window, text=f"Memory Runtime: {memory_runtime}s.").pack(pady=5)
box3 = tk.Label(master=window, text=f"\nDisk Score: {disk_score}.").pack(pady=5)
box33 = tk.Label(master=window, text=f"Disk Runtime: {disk_runtime}s.").pack(pady=5)
box4 = tk.Label(master=window, text=f"\nTotal Score: {total_score}").pack(pady=5)

window.mainloop()