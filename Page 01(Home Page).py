import mysql.connector
try:
    conn=None
    conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Isuri#02",
    db="riverviewhotel"
    )
    if conn is not None:
        print("Connection is established")
    else:
        print("Connection failed")
        
    import tkinter as tk
    from tkinter import *
    import mysql.connector

    root=tk.Tk()
    root.geometry("1800x800")
    root.title("Home Page")

    #backgroud
    bg_image=tk.PhotoImage(file="bg.png")
    canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    

    def home_page():
        def bookings_page():
            hotel_name_label.destroy()
            welcome_text_label.destroy()
            bookings_button.destroy()
            #Arriving Date
            arriving_date_label=Label(root, background="#FFEBCD", text="Arriving Date:", font=("Times", 25))
            arriving_date_label.place(x=300, y=50)
            arriving_date_entry=Entry(root, width=25)
            arriving_date_entry.place(x=320, y=100)
        
            #Departure Date
            departure_date_label=Label(root, background="#FFEBCD", text="Departure Date:", font=("Times", 25))
            departure_date_label.place(x=800, y=50)
            departure_date_entry=Entry(root, width=25)
            departure_date_entry.place(x=820, y=100)

            #Staying Options
            ac_check=Checkbutton(root, background="#FFEBCD",  text="AC", font=("Times", 25))
            ac_check.place(x=350, y=200)
            
            single_label=Label(root,background="#FFEBCD", text="1. Single -", font=("Arial", 18))
            single_label.place(x=400, y=300)
            single_entry=Entry(root, width=10)
            single_entry.place(x=550, y=305)
            
            double_label=Label(root,background="#FFEBCD", text="2. Double -", font=("Arial", 18))
            double_label.place(x=400, y=350)
            double_entry=Entry(root, width=10)
            double_entry.place(x=550, y=355)
            
            nonac_check=Checkbutton(root, background="#FFEBCD",  text="NON-AC", font=("Times", 25))
            nonac_check.place(x=850, y=200)
            single_nonac_label=Label(root,background="#FFEBCD", text="1. Single -", font=("Arial", 18))
            single_nonac_label.place(x=900, y=300)
            single_nonac_entry=Entry(root, width=10)
            single_nonac_entry.place(x=1050, y=305)
            double_nonac_label=Label(root,background="#FFEBCD", text="2. Double -", font=("Arial", 18))
            double_nonac_label.place(x=900, y=350)
            double_nonac_entry=Entry(root, width=10)
            double_nonac_entry.place(x=1050, y=355)

            def catch_bookings_page_entries():
                try:
                    arriving_date = arriving_date_entry.get()
                    departure_date = departure_date_entry.get()
                    single_ac = int(single_entry.get())
                    double_ac = int(double_entry.get())
                    single_nonac = int(single_nonac_entry.get())
                    double_nonac = int(double_nonac_entry.get())
                except ValueError as er:
                    print(er)

            def available_rooms():
                arriving_date_label.destroy()
                arriving_date_entry.destroy()
                departure_date_label.destroy()
                departure_date_entry.destroy()
                ac_check.destroy()
                single_label.destroy()
                single_entry.destroy()
                double_label.destroy()
                double_entry.destroy()
                nonac_check.destroy()
                single_nonac_label.destroy()
                single_nonac_entry.destroy()
                double_nonac_label.destroy()
                double_nonac_entry.destroy()
                back_button1.destroy()
                see_availability_button.destroy()

                options_label=tk.Label(root, bg="#FFEBCD", text="OPTIONS --> ", font=("ActivaCapsSSK", 40))
                options_label.place(x=64, y=57)

                room_type_options_label=tk.Label(root, bg="#FFEBCD", text="__Room Type Options__", font=("Adobe Garamond Pro Bold", 25))
                room_type_options_label.place(x=440, y=10)

                ac_label=tk.Label(root, bg="#FFEBCD", text="AC", font=("Times", 20))
                ac_label.place(x=400, y=90)

                single_label2=Label(root,background="#FFEBCD", text="Single", font=("Times", 20))
                single_label2.place(x=720, y=90)
                double_label2=Label(root,background="#FFEBCD", text="Double", font=("Times", 20))
                double_label2.place(x=820, y=90)

                rflr_label=tk.Label(root, bg="#FFEBCD", text="River Facing Luxary Room         \n   65000/= per night", font=("Adobe Fangsong Std R", 18))
                rflr_label.place(x=305, y=150)

                gflr_label=tk.Label(root, bg="#FFEBCD", text="Garden Facing Luxary Room       \n   55000/= per night", font=("Adobe Fangsong Std R", 18))
                gflr_label.place(x=305, y=250)

                gfslr_label=tk.Label(root, bg="#FFEBCD", text="Garden Facing Semi Luxary Room \n   40000/= per night", font=("Adobe Fangsong Std R", 17))
                gfslr_label.place(x=305, y=350)

                nonac_label=tk.Label(root, bg="#FFEBCD", text="NON-AC", font=("Times", 20))
                nonac_label.place(x=385, y=450)

                rflr_nonac_label=tk.Label(root, bg="#FFEBCD", text="River Facing Room                     \n   30000/= per night", font=("Adobe Fangsong Std R", 18))
                rflr_nonac_label.place(x=305, y=510)

                gflr_nonac_label=tk.Label(root, bg="#FFEBCD", text="Garden Facing Room                       \n   25000/= per night", font=("Adobe Fangsong Std R", 17))
                gflr_nonac_label.place(x=305, y=610)

                #Entries to get the counts of particular room types
                entry1=tk.Entry(root, width=10)
                entry1.place(x=720, y=160)
                entry2=tk.Entry(root, width=10)
                entry2.place(x=820, y=160)
                entry3=tk.Entry(root, width=10)
                entry3.place(x=720, y=260)
                entry4=tk.Entry(root, width=10)
                entry4.place(x=820, y=260)
                entry5=tk.Entry(root, width=10)
                entry5.place(x=720, y=360)
                entry6=tk.Entry(root, width=10)
                entry6.place(x=820, y=360)
                entry7=tk.Entry(root, width=10)
                entry7.place(x=720, y=520)
                entry8=tk.Entry(root, width=10)
                entry8.place(x=820, y=520)
                entry9=tk.Entry(root, width=10)
                entry9.place(x=720, y=620)
                entry10=tk.Entry(root, width=10)
                entry10.place(x=820, y=620)

                #Initializing as global variables
                room_charges_amount=0
                total_room_charges_amount_label=None

                def catch_available_rooms_entries():
                    global room_charges_amount
                    try:
                        entry1_value = int(entry1.get())
                        entry2_value = int(entry2.get())
                        entry3_value = int(entry3.get())
                        entry4_value = int(entry4.get())
                        entry5_value = int(entry5.get())
                        entry6_value = int(entry6.get())
                        entry7_value = int(entry7.get())
                        entry8_value = int(entry8.get())
                        entry9_value = int(entry9.get())
                        entry10_value = int(entry10.get())
                    except ValueError as err:
                        print(err)
                        return

                    #calculating room charges per one night
                    rates = [65000, 65000, 55000, 55000, 40000, 40000, 30000, 30000, 25000, 25000]

                    room_charges_amount = (entry1_value * rates[0] +
                                           entry2_value * rates[1] +
                                           entry3_value * rates[2] +
                                           entry4_value * rates[3] +
                                           entry5_value * rates[4] +
                                           entry6_value * rates[5] +
                                           entry7_value * rates[6] +
                                           entry8_value * rates[7] +
                                           entry9_value * rates[8] +
                                           entry10_value * rates[9])

                    room_charges_amount_label.config(text=room_charges_amount)
                

                room_charges_amount_label = tk.Label(root, background="white", font=("Arial",18))
                room_charges_amount_label.place(x=1300, y=108)

                calculate_button1 = tk.Button(root, activebackground="#9ACD32", text="Calculate", font=("Times", 18), command=catch_available_rooms_entries)
                calculate_button1.place(x=1000, y=100)
                    
                #| -line partion
                line_label=tk.Label(root, bg="#FFEBCD", text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", font=("Adobe Fangsong Std R", 25))
                line_label.place(x=950, y=80)

                def back2():
                    options_label.destroy()
                    room_type_options_label.destroy()
                    ac_label.destroy()
                    single_label2.destroy()
                    double_label2.destroy()
                    rflr_label.destroy()
                    gflr_label.destroy()
                    gfslr_label.destroy()
                    nonac_label.destroy()
                    rflr_nonac_label.destroy()
                    gflr_nonac_label.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    entry3.destroy()
                    entry4.destroy()
                    entry5.destroy()
                    entry6.destroy()
                    entry7.destroy()
                    entry8.destroy()
                    entry9.destroy()
                    entry10.destroy()
                    line_label.destroy()
                    reg_billing_button.destroy()
                    back_button2.destroy()
                    calculate_button1.destroy()
                    bookings_page()

                back_button2=tk.Button(root, activebackground="#9ACD32", text="       back       ", font=("Times", 20), command=back2)
                back_button2.place(x=1130, y=530)

                def reg_and_billing_page():
                    options_label.destroy()
                    room_type_options_label.destroy()
                    ac_label.destroy()
                    single_label2.destroy()
                    double_label2.destroy()
                    rflr_label.destroy()
                    gflr_label.destroy()
                    gfslr_label.destroy()
                    nonac_label.destroy()
                    rflr_nonac_label.destroy()
                    gflr_nonac_label.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    entry3.destroy()
                    entry4.destroy()
                    entry5.destroy()
                    entry6.destroy()
                    entry7.destroy()
                    entry8.destroy()
                    entry9.destroy()
                    entry10.destroy()
                    line_label.destroy()
                    reg_billing_button.destroy()
                    back_button2.destroy()
                    calculate_button1.destroy()

                    reg_and_billing_label=tk.Label(root, bg="#FFEBCD", text="Registration & Billing ", font=("ActivaCapsSSK", 35))
                    reg_and_billing_label.place(x=50, y=50)

                    registration_label=tk.Label(root, bg="#FFEBCD", text="__Registration__", font=("Adobe Garamond Pro Bold", 25))
                    registration_label.place(x=300, y=165)

                    name_label=tk.Label(root, bg="#FFEBCD", text="Name     :", font=("Arial",20))
                    name_label.place(x=315, y=260)
                    nic_label=tk.Label(root, bg="#FFEBCD", text="NIC        :", font=("Arial",20))
                    nic_label.place(x=315, y=360)
                    address_label=tk.Label(root, bg="#FFEBCD", text="Address :", font=("Arial",20))
                    address_label.place(x=315, y=460)
                    con_num_label=tk.Label(root, bg="#FFEBCD", text="Contact No:", font=("Arial",18))
                    con_num_label.place(x=315, y=560)

                    #Entries to get the values of registration form
                    name_entry=tk.Entry(root, width=70)
                    name_entry.place(x=450, y=270)
                    nic_entry=tk.Entry(root, width=70)
                    nic_entry.place(x=450, y=370)
                    address_entry=tk.Entry(root, width=70)
                    address_entry.place(x=450, y=470)
                    con_num_entry=tk.Entry(root, width=70)
                    con_num_entry.place(x=450, y=570)

                    def catch_registration_entries():
                        name_entry_value=name_entry.get()
                        nic_entry_value=nic_entry.get()
                        address_entry_value=address_entry.get()
                        con_num_entry_value=con_num_entry.get()


                    #| -line partion2
                    line_label2=tk.Label(root, bg="#FFEBCD", text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", font=("Adobe Fangsong Std R", 25))
                    line_label2.place(x=945, y=50)

                    #Receipt
                    receipt_label=tk.Label(root, bg="#FFEBCD", text="__Receipt__", font=("Adobe Garamond Pro Bold", 25))
                    receipt_label.place(x=1100, y=20)

                    room_charges_label=tk.Label(root, bg="#FFEBCD", text="Room Chargers:", font=("Arial",20))
                    room_charges_label.place(x=980, y=100)
                    stay_night_count_label=tk.Label(root, bg="#FFEBCD", text="Staying Nights Count:", font=("Arial",20))
                    stay_night_count_label.place(x=980, y=200)
                    total_room_charges_label=tk.Label(root, bg="#FFEBCD", text="Total Room Charges:", font=("Arial",20))
                    total_room_charges_label.place(x=980, y=300)
                    additional_charges_label=tk.Label(root, bg="#FFEBCD", text="Add. Chargers:", font=("Arial",20))
                    additional_charges_label.place(x=980, y=400)
                    total_label=tk.Label(root, bg="#FFEBCD", text="Total       :", font=("Arial",20))
                    total_label.place(x=980, y=500)

                    #Entries to get the values of receipt form
                    stay_night_count_entry=tk.Entry(root, width=25)
                    stay_night_count_entry.place(x=1300, y=208)

                    additional_charges_entry=tk.Entry(root, width=25)
                    additional_charges_entry.place(x=1300, y=408)

                    def catch_receipt_form_entries():
                        global room_charges_amount, total_room_charges_amount
                        try:
                            stay_night_count = int(stay_night_count_entry.get())
                            total_room_charges_amount = stay_night_count * room_charges_amount
                            total_room_charges_amount_label.config(text=total_room_charges_amount)  #Access global label variable
                        except ValueError as errr:
                            print(errr)
                            return
                        
                    total_room_charges_amount_label=tk.Label(root, background="white", font=("Arial",18))
                    total_room_charges_amount_label.place(x=1300, y=308)

                    calculate_button2 = tk.Button(root, activebackground="#9ACD32", text="Calculate", font=("Times", 12), command=catch_receipt_form_entries)
                    calculate_button2.place(x=1460, y=200)
                    

                    def back3():
                        reg_and_billing_label.destroy()
                        registration_label.destroy()
                        name_label.destroy()
                        nic_label.destroy()
                        address_label.destroy()
                        con_num_label.destroy()
                        name_entry.destroy()
                        nic_entry.destroy()
                        address_entry.destroy()
                        con_num_entry.destroy()
                        line_label2.destroy()
                        receipt_label.destroy()
                        room_charges_label.destroy()
                        additional_charges_label.destroy()
                        total_label.destroy()
                        stay_night_count_label.destroy()
                        total_room_charges_label.destroy()
                        stay_night_count_entry.destroy()
                        total_room_charges_amount_label.destroy()
                        calculate_button2.destroy()
                        room_charges_amount_label.destroy()
                        additional_charges_entry.destroy()
                        available_rooms()
                        back_button3.destroy()
                        exit_button.destroy()

                    back_button3=tk.Button(root, activebackground="#9ACD32", text="             Back                 ", font=("Times", 18), command=back3)
                    back_button3.place(x=1100, y=600)

                    '''def exitt():
                        #destroying reg_and_billing_page
                        back3()
                        
                        #destroying available_rooms page
                        back2()

                        #destroying bookings_page
                        back1()'''

                    exit_button=tk.Button(root, activebackground="#9ACD32", text="                Exit                ", font=("Times", 18))
                    exit_button.place(x=1100, y=700)
                    

                #calling catch_available_rooms_entries function and reg_and_billing_page function
                def call_above_2functions2():
                    catch_available_rooms_entries()
                    reg_and_billing_page()

                reg_billing_button=tk.Button(root, background="#9ACD32", text=" Registration\nand\nBilling ", font=("Times", 20), command=call_above_2functions2)
                reg_billing_button.place(x=1130, y=250)
                

            #calling catch_bookings_page_entries function and available_rooms function
            def call_above_2functions1():
                catch_bookings_page_entries()
                available_rooms()
                

            see_availability_button = tk.Button(root, background="#9ACD32", text="See Room-Availability", font=("Times", 25), command=call_above_2functions1)
            see_availability_button.place(x=1050, y=600)
                
            def back1():
                arriving_date_label.destroy()
                arriving_date_entry.destroy()
                departure_date_label.destroy()
                departure_date_entry.destroy()
                ac_check.destroy()
                single_label.destroy()
                single_entry.destroy()
                double_label.destroy()
                double_entry.destroy()
                nonac_check.destroy()
                single_nonac_label.destroy()
                single_nonac_entry.destroy()
                double_nonac_label.destroy()
                double_nonac_entry.destroy()
                see_availability_button.destroy()
                home_page()
                back_button1.destroy()

            back_button1=tk.Button(root, activebackground="#9ACD32", text="Back", font=("Times", 25), command=back1)
            back_button1.place(x=710, y=500)
            

        #River View Hotel
        hotel_name_label=tk.Label(root, bg="#FFEBCD", text="RIVER VIEW HOTEL", font=('Algerian', 60))
        hotel_name_label.place(x=40, y=50)
        #Welcome Text
        welcome_text_label=tk.Label(root, background="#DB7093", text=" Unlock Seamles Hospitality, Where \nEvery Click Ushers in\nComfort and Convenience.", font=("Ariston-Normal-Italic", 40))
        welcome_text_label.place(x=400, y=200)
        #Bookings Button
        bookings_button=tk.Button(root, activebackground="#9ACD32", text="Bookings", font=("Times", 25), command=bookings_page)
        bookings_button.place(x=760, y=500)

        



    home_page()
    root.mainloop()
except mysql.connector.Error as err:
    print("Connection Faild. Error is ", err)

