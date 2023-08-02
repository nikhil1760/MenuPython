import tkinter as tk
import subprocess as g

def option_1():
    print("You selected Option 1.")
    g.getoutput("notepad")

def option_2():
    print("You selected Option 2.")
    g.getoutput("chrome")

def option_3():
    print("You selected Option 3.")
    g.getoutput("chrome /incognito")

def option_4():
    print("You selected Option 4.")
    g.getoutput("chrome www.youtube.com")

def option_5():
    print("You selected Option 5.")
    g.getoutput("start firefox")

def option_6():
    print("You selected Option 6.")
    g.getoutput("start firefox -private")

def option_7():
    print("You selected Option 7.")
    g.getoutput("start iexplore")

def option_8():
    print("You selected Option 8.")
    g.getoutput("start iexplore -private")

def option_9():
    print("You selected Option 9.")
    g.getoutput("calc")

def option_10():
    print("You selected Option 10.")
    g.getoutput("control panel")

def option_11():
    print("You selected Option 11.")
    g.getoutput("explorer")


def option_12():
    print("You selected Option 11.")
    g.getoutput("mspaint")


def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Menu Example")

# Create a label
label = tk.Label(root, text="Welcome to the Menu!", font=("Helvetica", 16))
label.pack(pady=20)

# Create buttons for menu options
btn_option_1 = tk.Button(root, text="notepad", command=option_1)
btn_option_1.pack(pady=5)

btn_option_2 = tk.Button(root, text="Open chrome", command=option_2)
btn_option_2.pack(pady=5)

btn_option_3 = tk.Button(root, text="Open Chrome incognito", command=option_3)
btn_option_3.pack(pady=5)

btn_option_4 = tk.Button(root, text="Open youtube", command=option_4)
btn_option_4.pack(pady=5)

btn_option_5 = tk.Button(root, text="Open firefox", command=option_5)
btn_option_5.pack(pady=5)

btn_option_6 = tk.Button(root, text="Open firefox incognito", command=option_6)
btn_option_6.pack(pady=5)

btn_option_7 = tk.Button(root, text="Open Internet explorer", command=option_7)
btn_option_7.pack(pady=5)

btn_option_8 = tk.Button(root, text="Open Internet explorer incognito", command=option_8)
btn_option_8.pack(pady=5)

btn_option_9 = tk.Button(root, text="Open calculator", command=option_9)
btn_option_9.pack(pady=5)

btn_option_10 = tk.Button(root, text="Open control panel", command=option_10)
btn_option_10.pack(pady=5)

btn_option_11 = tk.Button(root, text="Open file explorer", command=option_11)
btn_option_11.pack(pady=5)

btn_option_12 = tk.Button(root, text="Open paint", command=option_12)
btn_option_12.pack(pady=5)


# Create an exit button
btn_exit = tk.Button(root, text="Exit", command=exit_program)
btn_exit.pack(pady=10)

# Start the main event loop
root.mainloop()