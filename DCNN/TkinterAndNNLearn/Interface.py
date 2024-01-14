import tkinter as tki


root = tki.Tk()

greeting = tki.Label(text="Привет, Tkinter!", fg='white', bg='black',
                     width=12, height=2)
greeting.place(x=10, y=120)


def Hello(event):
    print("Yet another hello world")


btn = tki.Button(root, text="Click me", width=10, height=3,
                 bg="white", fg="black")
btn.bind("<Button-1>", Hello)
btn.place(x=10, y=60)

tki.Button(root, text='1').grid(row=1, column=1)
tki.Button(root, text='6').grid(row=1, column=2)
tki.Button(root, text='__7__').grid(row=2, column=1, columnspan=2)

tki.Button(root, text='1').place(x=50, y=10, width=30)
tki.Button(root, text='2').place(x=85, y=20, height=15)
btn3 = tki.Button(root, text='__3__')
btn3.bind('<Button-1>', lambda x: root.destroy())
btn3.place(x=70, y=38)

entry = tki.Entry(fg="yellow", bg="blue", width=30)
entry.place(x=10, y=150)

text = entry.get()
print(text)
entry.insert(0, 'type ')
entry.delete(0, tki.END)
print(text)

box = tki.Text()
box.place(x=1, y=200)
text = box.get('2.0', tki.END)
print(text)
box.insert('1.0', 'Hi there!\n\nI\'m here!\n\n\n\n\n\n')
box.delete('1.0', '2.0')
box.insert(tki.END, 'What are you doing here?')

frame_a = tki.Frame()
frame_b = tki.Frame()

label_a = tki.Label(master=frame_a, text="I'm in Frame A")
label_a.place(x=150, y=20)
label_b = tki.Label(master=frame_b, text="I'm in Frame B")
label_b.place(x=200, y=20)

frame_a.place(x=150, y=20)
frame_b.place(x=200, y=20)

root.mainloop()
