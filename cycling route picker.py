#cycling route picker
import tkinter as tk
import random as r
root = tk.Tk()
root.geometry("1920x1080")
root.title("cycling")
n= 0 
def on_click():
    
    #define random function
    routes = ["intervals at WCH", "Mt Faber 3 laps", "Mt Faber single + coffee base", "Changi village", "Marina Bay Loop from JE", "Bedok Jetty", "Changi Airport", "ECP Length"]
    resultant = r.choice(routes)

    label = tk.Label(root, text=(resultant), font =("Arial,1000"))
    label.pack(pady=20) 
    n = n+1
    
           
            
            



button = tk.Button(root, text="Click for route", command=on_click)
button.pack(pady=20)






root.mainloop()
