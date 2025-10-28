import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Establish MySQL connection
try:
    db = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Isuri#02",
        db="riverviewhotel"
    )
    cursor = db.cursor()
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    print("Error while connecting to MySQL database:", err)

def check_availability():
    availability_window = tk.Toplevel(root)
    availability_window.title("Check Availability")
    availability_window.geometry("600x700")
    availability_window.configure(bg="#E6F3FF")

    # Labels and Entry widgets for check-in and check-out dates
    checkin_label = tk.Label(availability_window, bg="#E6F3FF", font=("Times", 15), text="Check-in Date :")
    checkin_label.place(x=100, y=60)

    checkin_entry = tk.Entry(availability_window)
    checkin_entry.place(x=350, y=60)

    checkout_label = tk.Label(availability_window, bg="#E6F3FF", font=("Times", 15), text="Check-out Date :")
    checkout_label.place(x=100, y=160)

    checkout_entry = tk.Entry(availability_window)
    checkout_entry.place(x=350, y=160)

    def check_availability_submit():
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()

        if checkin_date and checkout_date:
            try:
                cursor.execute("SELECT COUNT(*) FROM reservation WHERE checkout_date > %s AND checkin_date < %s", (checkin_date, checkout_date))
                overlap_count = cursor.fetchone()[0]
            
                if overlap_count == 0:
                    messagebox.showinfo("Availability", f"Rooms are available from {checkin_date} to {checkout_date}.")
                else:
                    messagebox.showinfo("Availability", f"Sorry, rooms are not available from {checkin_date} to {checkout_date}.")
            except mysql.connector.Error as err:
                print("Error checking availability:", err)
        else:
            messagebox.showerror("Error", "Please enter both check-in and check-out dates.")


    submit_button = tk.Button(availability_window, activebackground="dark blue", font=("Times", 14), text="Check Availability", command=check_availability_submit)
    submit_button.place(x=200, y=300)

def make_reservation():
    reservation_window = tk.Toplevel(root)
    reservation_window.title("Make Reservation")
    reservation_window.geometry("600x700")
    reservation_window.configure(bg="#E6F3FF")

    checkin_label = tk.Label(reservation_window, bg="#E6F3FF", font=("Times", 15), text="Check-in Date :")
    checkin_label.place(x=100, y=50)

    checkin_entry = tk.Entry(reservation_window)
    checkin_entry.place(x=350, y=50)

    checkout_label = tk.Label(reservation_window, bg="#E6F3FF", font=("Times", 14),  text="Check-out Date :")
    checkout_label.place(x=100, y=150)

    checkout_entry = tk.Entry(reservation_window)
    checkout_entry.place(x=350, y=150)

    room_count_label = tk.Label(reservation_window, bg="#E6F3FF", font=("Times", 15), text="Room Count :")
    room_count_label.place(x=100, y=250)

    room_count_entry = tk.Entry(reservation_window)
    room_count_entry.place(x=350, y=250)

    nights_count_label = tk.Label(reservation_window, bg="#E6F3FF", font=("Times", 15), text="Nights Count :")
    nights_count_label.place(x=100, y=350)

    nights_count_entry = tk.Entry(reservation_window)
    nights_count_entry.place(x=350, y=350)

    room_type_label = tk.Label(reservation_window, bg="#E6F3FF", font=("Times", 15),  text="Room Type :")
    room_type_label.place(x=100, y=450)

    room_types = ["AC Single", "AC Double", "Non-AC Single", "Non-AC Double"]
    room_type_var = tk.StringVar(reservation_window)
    room_type_var.set(room_types[0])

    room_type_menu = tk.OptionMenu(reservation_window, room_type_var, *room_types)
    room_type_menu.place(x=350, y=450)

    def make_reservation_submit():
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        room_type = room_type_var.get()
        room_count = int(room_count_entry.get())
        nights_count = int(nights_count_entry.get())

        '''if checkin_date and checkout_date and room_count:
            messagebox.showinfo("Reservation", f"Reservation made for {room_count} {room_type} room(s) from {checkin_date} to {checkout_date} and your Reservation id is {last_insert_id}.")
        else:
            messagebox.showerror("Error", "Please enter check-in date, check-out date, and room count.")'''

        #INSERT
        try:
            insert_sql = "INSERT INTO reservation (checkin_date, checkout_date, room_type, room_count, nights_count) VALUES (%s, %s, %s, %s, %s)"
            values = (checkin_date, checkout_date, room_type, room_count, nights_count)
            cursor.execute(insert_sql, values)
            db.commit()
            print("Insert Successful")
        except mysql.connector.Error as err:
            print("Insert Faild. Error is ", err)

        # Retrieve the last auto-incremented value
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_insert_id = cursor.fetchone()[0]

        if last_insert_id:
            messagebox.showinfo("Reservation", f"Your Reservation ID is {last_insert_id}.")
        else:
            messagebox.showerror("Error", "Please enter check-in date, check-out date, and room count.")


        

    def open_receipt():
        receipt_window = tk.Toplevel(root)
        receipt_window.title("Receipt")
        receipt_window.geometry("600x800")
        receipt_window.configure(bg="#E6F3FF")

        # Retrieve reservation details
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        room_type = room_type_var.get()
        room_count = int(room_count_entry.get())
        nights_count = int(nights_count_entry.get())
        #calculation
        if room_type == "AC Single":
            x = 20000
        elif room_type == "AC Double":
            x = 40000
        elif room_type == "Non-AC Single":
            x = 15000
        else:
            x = 30000

        room_charges = x * room_count * nights_count

        receipt_label_1 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 18), text="__Receipt__")
        receipt_label_1.place(x=200, y=50)

        receipt_label_2 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Check-in Date        : {checkin_date}")
        receipt_label_2.place(x=100, y=100)

        receipt_label_3 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Check-out Date       : {checkout_date}")
        receipt_label_3.place(x=100, y=160)

        receipt_label_4 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Room Type            : {room_type}")
        receipt_label_4.place(x=100, y=220)

        receipt_label_5 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Room Count           : {room_count}")
        receipt_label_5.place(x=100, y=280)

        receipt_label_6 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text="Additional Charges:")
        receipt_label_6.place(x=100, y=340)

        additional_charges_entry = tk.Entry(receipt_window, font=("Times", 15))
        additional_charges_entry.place(x=300, y=340)
        additional_charges_entry.insert(0, "0.00")  # Set default value

        def total_charges():
            total_charges = room_charges + float(additional_charges_entry.get())
            receipt_label_7.config(text=f"Total Charges        : {total_charges:.2f} rs")

        receipt_label_7 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text="")
        receipt_label_7.place(x=100, y=460)

        total_charges_button = tk.Button(receipt_window, activebackground="dark blue", font=("Times", 14), text="Calculate Total Charges", command=total_charges)
        total_charges_button.place(x=160, y=400)


    submit_button = tk.Button(reservation_window, activebackground="dark blue", width=20, font=("Times", 14), text="Make Reservation", command=make_reservation_submit)
    submit_button.place(x=200, y=550)

    receipt_button = tk.Button(reservation_window, activebackground="dark blue", width=20, font=("Times", 14), text="Print Receipt", command=open_receipt)
    receipt_button.place(x=200, y=600)

def update_reservation():
    reservation_update_window = tk.Toplevel(root)
    reservation_update_window.title("Update Reservation")
    reservation_update_window.geometry("600x700")
    reservation_update_window.configure(bg="#E6F3FF")

    reservation_id_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 15), text="Reservation ID :")
    reservation_id_label.place(x=100, y=30)

    reservation_id_entry = tk.Entry(reservation_update_window)
    reservation_id_entry.place(x=350, y=30)

    checkin_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 15), text="Check-in Date :")
    checkin_label.place(x=100, y=100)

    checkin_entry = tk.Entry(reservation_update_window)
    checkin_entry.place(x=350, y=100)

    checkout_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 14),  text="Check-out Date :")
    checkout_label.place(x=100, y=160)

    checkout_entry = tk.Entry(reservation_update_window)
    checkout_entry.place(x=350, y=160)

    room_count_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 15), text="Room Count :")
    room_count_label.place(x=100, y=250)

    room_count_entry = tk.Entry(reservation_update_window)
    room_count_entry.place(x=350, y=250)

    nights_count_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 15), text="Nights Count :")
    nights_count_label.place(x=100, y=350)

    nights_count_entry = tk.Entry(reservation_update_window)
    nights_count_entry.place(x=350, y=350)

    room_type_label = tk.Label(reservation_update_window, bg="#E6F3FF", font=("Times", 15),  text="Room Type :")
    room_type_label.place(x=100, y=450)

    room_types = ["AC Single", "AC Double", "Non-AC Single", "Non-AC Double"]
    room_type_var = tk.StringVar(reservation_update_window)
    room_type_var.set(room_types[0])

    room_type_menu = tk.OptionMenu(reservation_update_window, room_type_var, *room_types)
    room_type_menu.place(x=350, y=450)

    def update_reservation_submit():
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        room_type = room_type_var.get()
        room_count = int(room_count_entry.get())
        nights_count = int(nights_count_entry.get())
        reservation_id = int(reservation_id_entry.get())

        if reservation_id:
            messagebox.showinfo("Reservation", f"Updated for {reservation_id}.")
        else:
            messagebox.showerror("Error", "Please enter details to update.")


        #UPDATE
        try:
            update_sql="UPDATE reservation SET checkin_date=%s, checkout_date=%s, room_type=%s, room_count=%s, nights_count=%s WHERE reservation_id=%s"
            values=(checkin_date, checkout_date, room_type, room_count, nights_count, reservation_id)
            cursor.execute(update_sql, values)
            db.commit()
            print("Update Successful")
        except mysql.connector.Error as err:
            print("Update Faild. Error is ", err)

    def open_receipt():
        receipt_window = tk.Toplevel(root)
        receipt_window.title("Receipt")
        receipt_window.geometry("600x800")
        receipt_window.configure(bg="#E6F3FF")

        # Retrieve reservation details
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        room_type = room_type_var.get()
        room_count = int(room_count_entry.get())
        nights_count = int(nights_count_entry.get())
        #calculation
        if room_type == "AC Single":
            x = 20000
        elif room_type == "AC Double":
            x = 40000
        elif room_type == "Non-AC Single":
            x = 15000
        else:
            x = 30000

        room_charges = x * room_count * nights_count

        receipt_label_1 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 18), text="__Receipt__")
        receipt_label_1.place(x=200, y=50)

        receipt_label_2 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Check-in Date        : {checkin_date}")
        receipt_label_2.place(x=100, y=100)

        receipt_label_3 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Check-out Date       : {checkout_date}")
        receipt_label_3.place(x=100, y=160)

        receipt_label_4 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Room Type            : {room_type}")
        receipt_label_4.place(x=100, y=220)

        receipt_label_5 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text=f"Room Count           : {room_count}")
        receipt_label_5.place(x=100, y=280)

        receipt_label_6 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text="Additional Charges:")
        receipt_label_6.place(x=100, y=340)

        additional_charges_entry = tk.Entry(receipt_window, font=("Times", 15))
        additional_charges_entry.place(x=300, y=340)
        additional_charges_entry.insert(0, "0.00")  # Set default value

        def total_charges():
            total_charges = room_charges + float(additional_charges_entry.get())
            receipt_label_7.config(text=f"Total Charges        : {total_charges:.2f} rs")

        receipt_label_7 = tk.Label(receipt_window, bg="#E6F3FF", font=("Times", 15), text="")
        receipt_label_7.place(x=100, y=460)

        total_charges_button = tk.Button(receipt_window, activebackground="dark blue", font=("Times", 14), text="Calculate Total Charges", command=total_charges)
        total_charges_button.place(x=160, y=400)

    submit_button = tk.Button(reservation_update_window, activebackground="dark blue", width=20, font=("Times", 14), text="Update Reservation", command=update_reservation_submit)
    submit_button.place(x=200, y=550)

    receipt_button = tk.Button(reservation_update_window, activebackground="dark blue", width=20, font=("Times", 14), text="Print New Receipt", command=open_receipt)
    receipt_button.place(x=200, y=600)


def delete_reservation():

    reservation_delete_window = tk.Toplevel(root)
    reservation_delete_window.title("Delete Reservation")
    reservation_delete_window.geometry("600x700")
    reservation_delete_window.configure(bg="#E6F3FF")

    reservation_id_label = tk.Label(reservation_delete_window, bg="#E6F3FF", font=("Times", 15), text="Reservation ID :")
    reservation_id_label.place(x=100, y=100)

    reservation_id_entry = tk.Entry(reservation_delete_window)
    reservation_id_entry.place(x=350, y=100)

    def delete_reservation_submit():
        reservation_id = int(reservation_id_entry.get())

    # DELETE
        try:
            delete_sql = "DELETE FROM reservation WHERE reservation_id=%s"
            cursor.execute(delete_sql, (reservation_id,))
            db.commit()
            print("Delete Successful")
        except mysql.connector.Error as err:
            print("Delete Failed. Error is ", err)

    submit_button = tk.Button(reservation_delete_window, activebackground="dark blue", width=20, font=("Times", 14), text="Delete Reservation", command=delete_reservation_submit)
    submit_button.place(x=200, y=550)




def guest_information():
    guest_info_window = tk.Toplevel(root)
    guest_info_window.title("Guest Information")
    guest_info_window.geometry("600x700")
    guest_info_window.configure(bg="#E6F3FF")

    # Labels and Entry widgets for guest information
    name_label = tk.Label(guest_info_window, bg="#E6F3FF", font=("Times", 15),  text="Name :")
    name_label.place(x=100, y=60)

    name_entry = tk.Entry(guest_info_window)
    name_entry.place(x=350, y=60)

    address_label = tk.Label(guest_info_window, bg="#E6F3FF", font=("Times", 15),  text="Address :")
    address_label.place(x=100, y=160)

    address_entry = tk.Entry(guest_info_window)
    address_entry.place(x=350, y=160)

    contact_label = tk.Label(guest_info_window, bg="#E6F3FF", font=("Times", 15),  text="Contact Number :")
    contact_label.place(x=100, y=260)

    contact_entry = tk.Entry(guest_info_window)
    contact_entry.place(x=350, y=260)

    def save_guest_info():
        name = name_entry.get()
        address = address_entry.get()
        contact_number = contact_entry.get()

        if name and address and contact_number:
            messagebox.showinfo("Success", "Guest information saved successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")


        #INSERT
        try:
            insert_sql = "INSERT INTO guest (name, address, contact_number) VALUES (%s, %s, %s)"
            values = (name, address, contact_number)
            cursor.execute(insert_sql, values)
            db.commit()
            print("Insert Successful")
        except mysql.connector.Error as err:
            print("Insert Faild. Error is ", err)
           

    save_button = tk.Button(guest_info_window, activebackground="dark blue", font=("Times", 14), width=20, text="Save", command=save_guest_info)
    save_button.place(x=180, y=360)

root = tk.Tk()
root.title("Hotel Management System")
root.geometry("1200x700")
root.configure(bg="white")

label_title = tk.Label(root, background="white", text="__Welcome to River View Hotel__", font=("Times", 25))
label_title.place(x=380, y=50)

button_check_availability = tk.Button(root, activebackground="dark blue", text="Check Availability", font=("Times", 15), width=25, command=check_availability)
button_check_availability.place(x=470, y=200)

button_make_reservation = tk.Button(root, activebackground="dark blue", text="Make Reservation", font=("Times", 15), width=25, command=make_reservation)
button_make_reservation.place(x=470, y=300)

button_update_reservation = tk.Button(root, activebackground="dark blue", text="Update Reservation", font=("Times", 15), width=25, command=update_reservation)
button_update_reservation.place(x=470, y=400)

button_delete_reservation = tk.Button(root, activebackground="dark blue", text="Delete Reservation", font=("Times", 15), width=25, command=delete_reservation)
button_delete_reservation.place(x=470, y=500)

button_guest_info = tk.Button(root, activebackground="dark blue", text="Guest Information", font=("Times", 15), width=25, command=guest_information)
button_guest_info.place(x=470, y=600)

root.mainloop()
