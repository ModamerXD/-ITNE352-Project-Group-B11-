import socket
import json

# server details

host = "127.0.0.1"
port = 62894

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as C_socket:
    C_socket.connect((host, port))
    print("Connected to the server.")

    print("What is your name?")
    name = input()
    C_socket.send(name.encode("utf-8"))
    print('='*100)
    
    while True:
        print("Main menu. Choose by typing the number")
        print("1- Search headlines")
        print("2- List of sources")
        print("3- Quit")
        option = int(input())
        if option == 1:
            while True:
                print('='*100)
                print("Search headlines menu. Choose by typing the number")
                print("1- Search for keywords")
                print("2- Search by category")
                print("3- Search by country")
                print("4- List all new headlines")
                print("5- Back to main menu")
                head = int(input())

                if head == 1:
                    keyword = input("Enter the key word to search: ")
                    C_socket.send("head:keyword:{}".format(keyword).encode("utf-8"))
                elif head == 2:
                    while True:
                        print('='*100)
                        print("Enter the number of category to search")
                        print("1- Business")
                        print("2- General")
                        print("3- Health")
                        print("4- Science")
                        print("5- Sports")
                        print("6- Technology")

                        category = int(input("Enter the number:"))

                        if category == 1:
                            C_socket.send("head:category:business".encode("utf-8"))
                            break
                        elif category == 2:
                            C_socket.send("head:category:general".encode("utf-8"))
                            break
                        elif category == 3:
                            C_socket.send("head:category:health".encode("utf-8"))
                            break
                        elif category == 4:
                            C_socket.send("head:category:science".encode("utf-8"))
                            break
                        elif category == 5:
                            C_socket.send("head:category:sports".encode("utf-8"))
                            break
                        elif category == 6:
                            C_socket.send("head:category:technology".encode("utf-8"))
                            break
                        else:
                            print("Invalid number, please try again")


                elif head == 3:
                    while True:
                        print('='*100)
                        print("Enter the number of the country")
                        print("1- Australia")
                        print("2- Canada")
                        print("3- Japan")
                        print("4- United Arab Emirates")
                        print("5- Saudi Arabia")
                        print("6- South Korea")
                        print("7- United States")
                        print("8- Morocco")
                        country = int(input("Number: "))
                        if country == 1:
                            C_socket.send("head:country:au".encode("utf-8"))
                            break
                        elif country == 2:
                            C_socket.send("head:country:ca".encode("utf-8"))
                            break
                        elif country == 3:
                            C_socket.send("head:country:jp".encode("utf-8"))
                            break
                        elif country == 4:
                            C_socket.send("head:country:ae".encode("utf-8"))
                            break
                        elif country == 5:
                            C_socket.send("head:country:sa".encode("utf-8"))
                            break
                        elif country == 6:
                            C_socket.send("head:country:kr".encode("utf-8"))
                            break
                        elif country == 7:
                            C_socket.send("head:country:us".encode("utf-8"))
                            break
                        elif country == 8:
                            C_socket.send("head:country:ma".encode("utf-8"))
                            break
                        else:
                            print("Invalid number, please try again")

                elif head == 4:
                    C_socket.send("head:category:All".encode("utf-8"))

                elif head == 5:
                    break

                else:
                    print("Invalid number, please try again")
                    continue
                
                
                response = C_socket.recv(20000).decode("utf-8")
                
                data = json.loads(response)  # Convert the JSON string to a Python dictionary
                    
                
                print('='*100)
                print("Choose a number from the following articles to view more details of it")
                if len(data['articles']) == 0:
                    print("No data found")
                else:
                    for i in range(len(data['articles'])):
                        print(str((i+1))+'-\tSource name:', data['articles'][i]['source']['name'])
                        print("\tAuthor: ", data['articles'][i]['author'])                        
                        print("\tTitle: ", data['articles'][i]['title'])

                        
                print(str((len(data['articles'])+1))+"- Back to headlines menu")

                while True:

                    number = int(input("\nChoose number: "))
    
                    if number == (len(data['articles'])+1):
                        break

                    elif number >0 and number <= len(data['articles']):
                        print('='*100)
                        print("Source name:", data['articles'][number-1]['source']['name'])
                        print("Author:", data['articles'][number-1]['author'])
                        print("Title:", data['articles'][number-1]['title'])
                        print("URL:", data['articles'][number-1]['url'])
                        print("Description:", data['articles'][number-1]['description'])
                        print("Publish Date:", data['articles'][number-1]['publishedAt'][:10])
                        print("Publish time:", data['articles'][number-1]['publishedAt'][11:19])
                        break
                    
                    else: 
                        print("Invalid number, try again")



        elif option == 2:
            while True:
                print('='*100)
                print("Search headlines menu. Choose by typing the number")
                print("1- Search by category")
                print("2- Search by country")
                print("3- Search by language")
                print("4- List all")
                print("5- Back to the main menu")
                source = int(input())      

                if source == 1:
                    while True:
                        print('='*100)
                        print("Enter the number of category to search")
                        print("1- Business")
                        print("2- General")
                        print("3- Health")
                        print("4- Science")
                        print("5- Sports")
                        print("6- Technology")

                        category = int(input("Enter the number:"))

                        if category == 1:
                            C_socket.send("source:category:business".encode("utf-8"))
                            break
                        elif category == 2:
                            C_socket.send("source:category:general".encode("utf-8"))
                            break
                        elif category == 3:
                            C_socket.send("source:category:health".encode("utf-8"))
                            break
                        elif category == 4:
                            C_socket.send("source:category:science".encode("utf-8"))
                            break
                        elif category == 5:
                            C_socket.send("source:category:sports".encode("utf-8"))
                            break
                        elif category == 6:
                            C_socket.send("source:category:technology".encode("utf-8"))
                            break
                        else:
                            print("Invalid number, please try again")

                elif source == 2:
                    while True:
                        print('='*100)
                        print("Enter the number of the country")
                        print("1- Australia")
                        print("2- Canada")
                        print("3- Japan")
                        print("4- United Arab Emirates")
                        print("5- Saudi Arabia")
                        print("6- South Korea")
                        print("7- United States")
                        print("8- Morocco")
                        country = int(input("Enter the number: "))
                        if country == 1:
                            C_socket.send("source:country:au".encode("utf-8"))
                            break
                        elif country == 2:
                            C_socket.send("source:country:ca".encode("utf-8"))
                            break
                        elif country == 3:
                            C_socket.send("source:country:jp".encode("utf-8"))
                            break
                        elif country == 4:
                            C_socket.send("source:country:ae".encode("utf-8"))
                            break
                        elif country == 5:
                            C_socket.send("source:country:sa".encode("utf-8"))
                            break
                        elif country == 6:
                            C_socket.send("source:country:kr".encode("utf-8"))
                            break
                        elif country == 7:
                            C_socket.send("source:country:us".encode("utf-8"))
                            break
                        elif country == 8:
                            C_socket.send("source:country:ma".encode("utf-8"))
                            break
                        else:
                            print("Invalid number, please try again")

                elif source == 3:

                    while True:
                        print('='*100)
                        print("Enter the number of the language")
                        print("1- English")
                        print("2- Arabic")
                        language = int(input("Enter the number: "))

                        if language == 1:
                            C_socket.send("source:language:en".encode("utf-8"))
                            break
                        elif language == 2:
                            C_socket.send("source:language:ar".encode("utf-8"))
                            break
                        else:
                            print("Invalid number, please try again")
                elif source == 4:
                    C_socket.send("source:category:All".encode("utf-8"))
                

                elif source == 5:
                    break

                else:
                    print("Invalid number, please try again")
                    continue


                response = C_socket.recv(50000).decode("utf-8")
                
                data = json.loads(response)  # Convert the JSON string to a Python dictionary

                
                print('='*100)
                print("Choose a number from the following sources to view more details of it")
                if len(data['sources']) == 0:
                    print("No data found")
                else:
                    for i in range(len(data['sources'])):
                        print(str((i+1))+'-\tSource name:', data['sources'][i]['name'])

                print(str((len(data['sources'])+1))+"- Back to sources menu")

                while True:
                    number = int(input("\nChoose number: "))

                    if number == len(data['sources'])+1:
                        break
                    
                    elif number >0 and number <= len(data['sources']):
                        print('='*100)
                        print("Source name:", data['sources'][number-1]['name'])
                        print("Country:", data['sources'][number-1]['country'])
                        print("Description", data['sources'][number-1]['description'])
                        print("URL:", data['sources'][number-1]['url'])
                        print("Category:", data['sources'][number-1]['category'])
                        print("Language:", data['sources'][number-1]['language'])
                        break
                    else:
                        print("Invalid number, please try again")


        elif option == 3:
            C_socket.send('quit'.encode("utf-8"))
            break
        else:
            print("Invalid number, choose again")

        print('='*100)
