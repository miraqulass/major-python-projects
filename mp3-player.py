from tkinter import *
import time
import random
from tkinter import messagebox


def price():
    roo = Tk()
    roo.geometry("600x280+0+0")
    roo.title("Price List")

    # Labels for displaying item and price
    items = ["Drink", "Burger King", "Cherry", "Nacho Fries", "Pizza", "Biscuits", "Roll", "Tea"]
    prices = [10, 30, 15, 20, 30, 10, 10, 5]

    for i in range(len(items)):
        lbl_info = Label(roo, font=('aria', 15, 'bold'), text=items[i], fg="#ED420B", anchor=W)
        lbl_info.grid(row=i, column=0)

        lbl_info = Label(roo, font=('aria', 15, 'bold'), text=str(prices[i]), fg="#ED420B", anchor=W)
        lbl_info.grid(row=i, column=3)

    roo.mainloop()


def clear():
    text.delete(1.0, END)


def quit_fun():
    root.destroy()


def total():
    prices = [int(dringE.get()), int(burger_kingE.get()), int(cherry.get()), int(nacho_fries.get()),
              int(pizza.get()), int(biscuits.get()), int(roll.get()), int(tea.get())]

    # Price list
    item_prices = [10, 30, 25, 20, 30, 10, 10, 5]

    # Calculate cost for each item
    cost = sum([price * item_price for price, item_price in zip(prices, item_prices)])

    # Display cost
    display = cost
    p1_label["text"] = display

    # Calculate service tax
    service_charge = cost / 20
    service_display = service_charge
    p2_label["text"] = service_display

    # Calculate tax
    tax_charge = int(cost / 3)
    p3_label["text"] = tax_charge

    # Calculate sub total
    sub_total = cost
    p4_label["text"] = sub_total

    # Calculate total
    total = display + service_charge + tax_charge
    total_display = total
    p5_label["text"] = total_display

    # Generate a random order number
    order_number = random.randint(1, 10000)
    order_label["text"] = order_number


def reset():
    # Clear entry fields and labels
    dringE.delete(0, END)
    burger_kingE.delete(0, END)
    cherry.delete(0, END)
    nacho_fries.delete(0, END)
    pizza.delete(0, END)
    biscuits.delete(0, END)
    roll.delete(0, END)
    tea.delete(0, END)
    p1_label["text"] = ""
    p2_label["text"] = ""
    p3_label["text"] = ""
    p4_label["text"] = ""
    p5_label["text"] = ""
    order_label["text"] = ""


def clock():
    # Display current time
    current = time.strftime("%H:%M:%S")
    label1["text"] = current
    root.after(1000, clock)


# Main window
root = Tk()
root.geometry("1000x700")
root.minsize(1000, 700)
root.maxsize(1000, 700)
root.title("Restaurant Management")

# Heading labels
heading1 = Label(root, text="Restaurant Management", font="arial 30 bold", fg="#fc5a03")
heading2 = Label(root, text="Miraqulas Restaurant", font="arial 18 bold", fg="#fc5a03")
heading1.place(x=350, y=10)
heading2.place(x=400, y=80)

# Frames for item entry and price display
frame1 = Frame(root, height="420", width="330", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)
frame1.place(x=40, y=140)
frame2 = Frame(root, height="420", width="330", bd=10, bg="#33A9CE", highlightthickness=1, relief=SUNKEN)
frame2.place(x=380, y=140)

# Frames for buttons and calculator display
frame3 = Frame(root, height="100", width="670", bd=10, bg="#ED420B", highlightthickness=1, relief=SUNKEN)
frame3.place(x=40, y=565)
cal_frame = Frame(root, height="500", width="450", bd=10, highlightthickness=1, relief=SUNKEN)
cal_frame.place(x=750, y=150)
text_frame = Frame(root, height="100", width="100")
text_frame.place(x=1000, y=50)

frame_time = Frame(root, height="200", width="200", bd=10, highlightthickness=1, relief=SUNKEN)
frame_time.place(x=100, y=50)

# Price display labels
p1_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
p1_label.place(x=200, y=80)
p2_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
p2_label.place(x=200, y=120)
p3_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
p3_label.place(x=200, y=160)
p4_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
p4_label.place(x=200, y=200)
p5_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
p5_label.place(x=200, y=240)
order_label = Label(frame2, font="arial 14 bold ", bg="#33A9CE")
order_label.place(x=200, y=40)

# Entry fields for item quantities
dringE = Entry(frame1, bd="3")
burger_kingE = Entry(frame1, bd="5")
cherry = Entry(frame1, bd="5")
nacho_fries = Entry(frame1, bd="5")
pizza = Entry(frame1, bd="5")
biscuits = Entry(frame1, bd="5")
roll = Entry(frame1, bd="5")
tea = Entry(frame1, bd="5")

# Place entry fields on frame
dringE.place(x=130, y=35)
burger_kingE.place(x=130, y=80)
cherry.place(x=130, y=125)
nacho_fries.place(x=130, y=170)
pizza.place(x=130, y=215)
biscuits.place(x=130, y=260)
roll.place(x=130, y=305)
tea.place(x=130, y=350)

# Labels for item names
drink_label = Label(frame1, text="Drink", font="arial 12 bold ", bg="#ED420B")
burger_king_label = Label(frame1, text="Burger King", font="arial 12 bold", bg="#ED420B")
cherry_label = Label(frame1, text="Cherry", font="arial 12 bold", bg="#ED420B")
nacho_fries_label = Label(frame1, text="Nacho Fries", font="arial 12 bold", bg="#ED420B")
pizza_label = Label(frame1, text="Pizza", font="arial 12 bold ", bg="#ED420B")
biscuits_label = Label(frame1, text="Biscuits", font="arial 12 bold", bg="#ED420B")
roll_label = Label(frame1, text="Roll", font="arial 12 bold ", bg="#ED420B")
tea_label = Label(frame1, text="Tea", font="arial 12 bold ", bg="#ED420B")

# Place labels on frame
drink_label.place(x=10, y=35)
burger_king_label.place(x=10, y=80)
cherry_label.place(x=10, y=125)
nacho_fries_label.place(x=10, y=175)
pizza_label.place(x=10, y=215)
biscuits_label.place(x=10, y=260)
roll_label.place(x=10, y=305)
tea_label.place(x=10, y=350)

# Calculator display label
data = StringVar()
lbl = Label(cal_frame, text="LABEL", anchor=SE, font=("Verdana", 20), textvariable=data, background="#ffffff", fg="#000000")
lbl.pack(expand=True, fill="both")

# Buttons for calculator
btnrow1 = Frame(cal_frame, bg="#000000")
btnrow1.pack(expand=True, fill="both")
btnrow2 = Frame(cal_frame)
btnrow2.pack(expand=True, fill="both")
btnrow3 = Frame(cal_frame)
btnrow3.pack(expand=True, fill="both")
btnrow4 = Frame(cal_frame)
btnrow4.pack(expand=True, fill="both")


# Define button functions
def btn_clicked(number):
    global val
    val = val + str(number)
    data.set(val)


def btn_operator(operator_symbol):
    global A, operator, val
    A = int(val)
    operator = operator_symbol
    val = val + operator
    data.set(val)


def btn_clear():
    global A, operator, val
    A = 0
    operator = ""
    val = ""
    data.set(val)


def btn_result():
    global A, operator, val
    val2 = val
    if operator == "+":
        B = int((val2.split("+")[1]))
        C = A + B
        data.set(C)
        val = str(C)
    elif operator == "-":
        B = int((val2.split("-")[1]))
        C = A - B
        data.set(C)
        val = str(C)
    elif operator == "*":
        B = int((val2.split("*")[1]))
        C = A * B
        data.set(C)
        val = str(C)
    elif operator == "/":
        B = int((val2.split("/")[1]))
        if B == 0:
            messagebox.showerror("Error", "Divisible by 0 not allowed.")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / B)
            data.set(C)
            val = str(C)


# Create calculator buttons
buttons = [
    ('1', btn_clicked, btnrow1), ('2', btn_clicked, btnrow1), ('3', btn_clicked, btnrow1),
    ('+', btn_operator, btnrow1), ('4', btn_clicked, btnrow2), ('5', btn_clicked, btnrow2),
    ('6', btn_clicked, btnrow2), ('-', btn_operator, btnrow2), ('7', btn_clicked, btnrow3),
    ('8', btn_clicked, btnrow3), ('9', btn_clicked, btnrow3), ('*', btn_operator, btnrow3),
    ('C', btn_clear, btnrow4), ('0', btn_clicked, btnrow4), ('=', btn_result, btnrow4), ('/', btn_operator, btnrow4)
]

# Add buttons to the GUI
for (text, command, frame) in buttons:
    button = Button(frame, text=text, font=("Verdana", 22), relief=GROOVE, border=0, command=lambda t=text: command(t))
    button.pack(side=LEFT, expand=True, fill="both")

# Display current time
label1 = Label(frame_time, font="article 30", bg="black", fg="#ED420B")
label1.grid(row=0, column=0)
clock()

# Buttons for Price, Total, Reset, and Quit
price_btn = Button(frame3, text="Price", command=price, font="arial 15 bold", bd=10)
price_btn.place(x=80, y=10)
total_btn = Button(frame3, text="Total", command=total, font="arial 15 bold", bd=10)
total_btn.place(x=210, y=10)
reset_btn = Button(frame3, text="Reset", command=reset, font="arial 15 bold", bd=10)
reset_btn.place(x=350, y=10)
quit_btn = Button(frame3, text="Quit", command=quit_fun, font="arial 15 bold", bd=5)
quit_btn.place(x=500, y=10)

# Clear button
clear_btn = Button(root, text="Clear", command=clear, font="arial 10 bold", bd=10)
clear_btn.place(x=760, y=450)

root.mainloop()
