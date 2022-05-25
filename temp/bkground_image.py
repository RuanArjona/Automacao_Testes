from tkinter import *
root = Tk() 
root.geometry("484x159") 
bg = PhotoImage(file = "setor-de-testes.png") 
canvas1 = Canvas( root, width = 484, 
                 height = 159) 
  
#canvas1.pack(fill = "both", expand = TRUE) 
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
button1 = Button( root, text = "Atualiza MDE") 
button1_canvas = canvas1.create_window( 100, 10,  
                                       anchor = "nw", 
                                       window = button1) 
root.mainloop() 
