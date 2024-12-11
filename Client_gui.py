import json
import os
import socket
import tkinter as tk

def quit():
    window.destroy()

def name():
    global name
    name = entry.get()
    C_socket.send(name.encode("utf-8"))
    mainMenu()




def mainMenu():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text=f"Welcome {name}", font=("Arial", 14, "bold"))
    label.pack(pady=10)  

    label = tk.Label(window, text="Please select an option:", font=("Arial", 14, "bold"))
    label.pack(pady=10)  

    
    button1 = tk.Button(window, text="Search by headlines", command= search_headlines, width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)  

    
    button2 = tk.Button(window, text="List of sources", command=list_sources, width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    
    button3 = tk.Button(window, text="Quit", command= quit, width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

# Making a headline function page that offer the way to search headlines

def search_headlines():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Please select an option", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="Search by keyword", command=head_keyword,  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="Search by category", command= head_category,  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="Search by country", command= head_country ,width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="List all new headlines", command= lambda: get_info_head("head:All"),  width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="Back to main menu", command=mainMenu,  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)

# making a function for each type of search that need specifc calls

def head_keyword():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Please select the option you want to search", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text="Submit", command=lambda: get_info_head("head:keyword:" + entry.get()), width=20, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    button1= tk.Button(window, text= "Go back", command= search_headlines, width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)


def head_category():
    for widget in window.winfo_children():
        widget.destroy()
    
    

    label = tk.Label(window, text="Please select the option you want to search", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1 = tk.Button(window, text="business", command=lambda: get_info_head("head:category:business"), width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="general", command=lambda: get_info_head("head:category:general"),  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="health", command=lambda: get_info_head("head:category:health"),  width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="science", command=lambda: get_info_head("head:category:science"),  width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="sports", command=lambda: get_info_head("head:category:sports"),  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)

    button6= tk.Button(window, text="technology", command=lambda: get_info_head("head:category:technology"),  width=20, height=2, font=("Arial", 12, "bold"))
    button6.pack(pady=5)

    button7= tk.Button(window, text= "Go back", command= search_headlines, height=2, font=("Arial", 12, "bold"))
    button7.pack(pady=5)


def head_country():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Please select the option you want to search", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="Australia", command=lambda: get_info_head("head:country:au"),  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="Canada", command=lambda: get_info_head("head:country:ca"),  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="Japan", command=lambda: get_info_head("head:country:jp"),  width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="United Arab Emirates", command=lambda: get_info_head("head:country:ar"),  width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="Saudi Arabia", command=lambda: get_info_head("head:country:sa"),  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)

    button6= tk.Button(window, text="South Korea", command=lambda: get_info_head("head:country:kr"),  width=20, height=2, font=("Arial", 12, "bold"))
    button6.pack(pady=5)

    button7= tk.Button(window, text="United States", command=lambda: get_info_head("head:country:us"),  width=20, height=2, font=("Arial", 12, "bold"))
    button7.pack(pady=5)

    button8= tk.Button(window, text="Morocco", command=lambda: get_info_head("head:country:ma"),  width=20, height=2, font=("Arial", 12, "bold"))
    button8.pack(pady=5)

    button9= tk.Button(window, text= "Go back", command= search_headlines, height=2, font=("Arial", 12, "bold"))
    button9.pack(pady=5)



# Making a sources function page that offer the way to search list of sources

def list_sources():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Please select an option", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="Search by category", command=source_category ,  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="Search by country", command=source_country ,  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="Search by language", command=source_language ,  width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="List all", command=lambda: get_info_source("source:All")  ,width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="Back to the main menu", command=mainMenu,  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)


# making a function for each type of search that need specifc calls

def source_category():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Please select the option you want to search", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="business", command=lambda: get_info_source("source:category:business"),  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="general", command=lambda: get_info_source("source:category:general"),  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="health", command=lambda: get_info_source("source:category:health"),  width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="science", command=lambda: get_info_source("source:category:science"),  width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="sports", command=lambda: get_info_source("source:category:sports"),  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)

    button6= tk.Button(window, text="technology", command=lambda: get_info_source("source:category:technology"),  width=20, height=2, font=("Arial", 12, "bold"))
    button6.pack(pady=5)

    button7= tk.Button(window, text= "Go back", command= list_sources, height=2, font=("Arial", 12, "bold"))
    button7.pack(pady=5)


def source_country():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Please select the option you want to search", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="Australia", command=lambda: get_info_source("source:country:au"),  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="Canada", command=lambda: get_info_source("source:country:ca"),  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text="Japan", command=lambda: get_info_source("source:country:jp"),  width=20, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4= tk.Button(window, text="United Arab Emirates", command=lambda: get_info_source("source:country:ar"),  width=20, height=2, font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button5= tk.Button(window, text="Saudi Arabia", command=lambda: get_info_source("source:country:sa"),  width=20, height=2, font=("Arial", 12, "bold"))
    button5.pack(pady=5)

    button6= tk.Button(window, text="South Korea", command=lambda: get_info_source("source:country:kr"),  width=20, height=2, font=("Arial", 12, "bold"))
    button6.pack(pady=5)

    button7= tk.Button(window, text="United States", command=lambda: get_info_source("source:country:us"),  width=20, height=2, font=("Arial", 12, "bold"))
    button7.pack(pady=5)

    button8= tk.Button(window, text="Morocco", command=lambda: get_info_source("source:country:ma"),  width=20, height=2, font=("Arial", 12, "bold"))
    button8.pack(pady=5)

    button9= tk.Button(window, text= "Go back", command= list_sources, height=2, font=("Arial", 12, "bold"))
    button9.pack(pady=5)

def source_language():
    for widget in window.winfo_children():
        widget.destroy()
    
    label = tk.Label(window, text="Please select a language", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    button1= tk.Button(window, text="English", command=lambda: get_info_source("source:language:en"),  width=20, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2= tk.Button(window, text="Arabic", command=lambda: get_info_source("source:language:ar"),  width=20, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3= tk.Button(window, text= "Go back", command= list_sources, height=2, font=("Arial", 12, "bold"))
    button3.pack(pady=5)


# ==============================================================================================================================
# get info for headlines

def get_info_head(word):

    for widget in window.winfo_children():
        widget.destroy()

    C_socket.send(word.encode("utf-8"))
    # receive the input with buffer size of 50 kilobytes and convert it to json dictionary
    response = C_socket.recv(50000).decode("utf-8")

    if not response:
        print("Empty response received")
        return

    data = json.loads(response)  # Convert the JSON string to a Python dictionary

    

    text_widget = tk.Text(window, wrap="word", width=80, height=25)
    text_widget.pack(pady=10, padx=10)

    
    results = min(data['totalResults'], 20)
    

    
    if results == 0:
        text_widget.insert("end", "No data found")
    else:
        for i in range(results):
            text_widget.insert("end",
                f"{i+1} - Source name: {data['articles'][i]['source']['name']}\n"
                f"    Author: {data['articles'][i]['author']}\n"
                f"    Title: {data['articles'][i]['title']}\n\n"
            )

        text_widget.config(state="disabled")

    label = tk.Label(window, text= "Enter the number", font=("Arial", 14, "bold"))
    label.pack(pady=10)
    
    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text= "Submit", command=lambda: (
                        more_details_head(entry.get(), data)
                        if int(entry.get()) < 1 or int(entry.get()) > results
                        else more_details_head(int(entry.get()),data)
                                                                ), width=15, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    button1 = tk.Button(window, text="Go back", command=search_headlines, width = 15, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2 = tk.Button(window, text="Back to main menu", command=mainMenu , width=15 , height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)



def more_details_head(number, data):
    number = int(number)
    for widget in window.winfo_children():
        widget.destroy()
    
    text_widget = tk.Text(window, wrap="word", width=80, height=25)
    text_widget.pack(pady=10, padx=10)

    
    results = min(data['totalResults'], 20)
    

    if results == 0:
        text_widget.insert("end", "No data found")
    else:
        for i in range(results):
            text_widget.insert("end",
                f"{i+1} - Source name: {data['articles'][i]['source']['name']}\n"
                f"   Author: {data['articles'][i]['author']}\n"
                f"   Title: {data['articles'][i]['title']}\n\n"
            )

        text_widget.config(state="disabled")
    
    
    if number < 1 or number > results:
        label = tk.Label(window, text= "Please enter a number within the shown headlines", font=("Arial", 14, "bold"), fg="red")
        label.pack(pady=10)
        
    else:
        text_widget = tk.Text(window, wrap="word", width=80, height=10)
        text_widget.pack(pady=10, padx=10)
        text_widget.insert("end",
            f"Source name: {data['articles'][number-1]['source']['name']}\n"
            f"Author: {data['articles'][number-1]['author']}\n"
            f"Title: {data['articles'][number-1]['title']}\n"
            f"URL:, {data['articles'][number-1]['url']}\n"
            f"Description:, {data['articles'][number-1]['description']}\n"
            f"Publish Date:, {data['articles'][number-1]['publishedAt'][:10]}\n"
            f"Publish Time:, {data['articles'][number-1]['publishedAt'][11:19]}\n"
            )
        
        label = tk.Label(window, text= "Enter the number", font=("Arial", 14, "bold"))
        label.pack(pady=10)
        
    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text= "Submit", command=lambda: more_details_head(entry.get(),data), width=15, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    button1 = tk.Button(window, text="Go back", command=search_headlines, width=15, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2 = tk.Button(window, text="Back to main menu", command=mainMenu, width=15, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)

# ===================================================================================================================================
# get info for source


def get_info_source(word):

    for widget in window.winfo_children():
        widget.destroy()

    C_socket.send(word.encode("utf-8"))
    # receive the input with buffer size of 50 kilobytes and convert it to json dictionary
    response = C_socket.recv(50000).decode("utf-8")

    if not response:
        print("Empty response received")
        return

    data = json.loads(response)  # Convert the JSON string to a Python dictionary

    

    text_widget = tk.Text(window, wrap="word", width=80, height=25)
    text_widget.pack(pady=10, padx=10)

    
    results = min(len(data['sources']), 20)
    

    
    if results == 0:
        text_widget.insert("end", "No data found")
    else:
        for i in range(results):
            text_widget.insert("end",
                f"{i+1} - Source name: {data['sources'][i]['name']}\n\n"
                )
            
        
    text_widget.config(state="disabled")

    label = tk.Label(window, text= "Enter the number", font=("Arial", 14, "bold"))
    label.pack(pady=10)
    
    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text= "Submit", command=lambda: (
                        more_details_source(entry.get(), data)
                        if int(entry.get()) < 1 or int(entry.get()) > results
                        else more_details_source(int(entry.get()),data)
                                                                ),width=15, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    button1 = tk.Button(window, text="Go back", command=list_sources, width=15, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2 = tk.Button(window, text="Back to main menu", command=mainMenu, width=15, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)



def more_details_source(number,data):
    number = int(number)
    for widget in window.winfo_children():
        widget.destroy()
    
    text_widget = tk.Text(window, wrap="word", width=80, height=25)
    text_widget.pack(pady=10, padx=10)

    results = min(len(data['sources']), 20)

    if results == 0:
        text_widget.insert("end", "No data found")
    else:
        for i in range(results):
            text_widget.insert("end",
                f"{i+1} - Source name: {data['sources'][i]['name']}\n\n"
            )

    text_widget.config(state="disabled")
    
    if number < 1 or number > results:
        label = tk.Label(window, text= "Please enter a number within the shown headlines", font=("Arial", 14, "bold"), fg="red")
        label.pack(pady=10)
        
    else:
        text_widget = tk.Text(window, wrap="word", width=80, height=10)
        text_widget.pack(pady=10, padx=10)
        text_widget.insert("end",
            f"Source name: {data['sources'][number-1]['name']}\n"
            f"Country: {data['sources'][number-1]['country']}\n"
            f"Description: {data['sources'][number-1]['description']}\n"
            f"URL:, {data['sources'][number-1]['url']}\n"
            f"Category:, {data['sources'][number-1]['category']}\n"
            f"Language:, {data['sources'][number-1]['language']}\n"
            )
    
        label = tk.Label(window, text= "Enter the number", font=("Arial", 14, "bold"))
        label.pack(pady=10)

    
    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text= "Submit", command=lambda: more_details_source(entry.get(),data), width=15, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    button1 = tk.Button(window, text="Go back", command=list_sources, width=15, height=2, font=("Arial", 12, "bold"))
    button1.pack(pady=5)

    button2 = tk.Button(window, text="Back to main menu", command=mainMenu, width=15, height=2, font=("Arial", 12, "bold"))
    button2.pack(pady=5)


host = "127.0.0.1"
port = 62894

try:
    # create socket
    C_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    C_socket.connect((host, port))
    print("Connected to the server.")

    window = tk.Tk()
    window.title("NewsAPI Implementation")

    window.geometry("800x800+100+100")

    label = tk.Label(window, text="Enter your name:", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    entry = tk.Entry(window, width=30, font=("Arial", 13, "bold"))
    entry.pack(pady=5)

    button = tk.Button(window, text= "Submit", command=name, width=15, height=2, font=("Arial", 12, "bold"))
    button.pack(pady=5)

    window.mainloop()

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

    try:
        C_socket.close()  # Close the socket connection if it's open
        print("Socket closed.")
    except Exception as socket_error:
        print(f"Error closing the socket: {socket_error}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Program terminated.")