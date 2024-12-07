import socket
import threading
import requests
import json
import os


def start_server():
    # Create socket
    sock_p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Bind socket to server ip
    host = "127.0.0.1"
    port = 62894
    sock_p.bind((host,port))

    # Now we let the the server listen up to 10 queued connections
    sock_p.listen(10)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = sock_p.accept()
        client_name = client_socket.recv(2048).decode("utf-8")
        print(f"Accepted connection from {client_name}")
        
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=client_handling, args=(client_socket, client_name))
        client_thread.start()

def client_handling(client_socket, client_name):
    try:
        while True:
            request = client_socket.recv(2048).decode("utf-8")
            # check if the request was to disconnect connection
            if request == 'quit':
                break  # Client disconnected
            print(f"Received request: {request}")
            # check if the request was for headlines
            if request[:4] == 'head':
                url = 'https://newsapi.org/v2/top-headlines'
                # check what menu option the user chose to search by for headlines
                if request[5:12] == 'keyword':
                    params = {
                        "q":request[13:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                elif request[5:13] == 'category':
                    params = {
                        "category": request[14:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                elif request[5:12] == 'country':
                    params = {
                        "country": request[13:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                else:
                    params = {
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }

                response = requests.get(url,params=params)

                save_json(response.json(),client_name,'Headlines')

                if response.status_code == 200:
                    client_socket.send(response.text.encode("utf-8"))
                else:
                    client_socket.send(f"API Error: {response.status_code}".encode("utf-8"))
            
            
            # Check if the client wanted to search by sources
            elif request[:6] == 'source':
                url = 'https://newsapi.org/v2/top-headlines/sources'

                # check what menu option the client wanted to search by for sources

                if request[8:16] == 'category':
                    params = {
                        "category":request[17:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                elif request[8:15] == 'country':
                    params = {
                        "country": request[16:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                elif request[8:16] == 'language':
                    params = {
                        "language": request[17:], 
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }
                else:
                    params = {
                        "apiKey": "9d73eeefa6dc4ec8a2fe74a16501503d" 
                    }

                response = requests.get(url,params=params)

                save_json(response.json(),client_name,'Sources')

                if response.status_code == 200:
                        client_socket.sendall(response.encode("utf-8"))
                else:
                    client_socket.send(f"API Error: {response.status_code}".encode("utf-8"))

            # if it was something else, in this case quit. We terminate the connection
            

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

def save_json(data,client_name,option):
    # directory path to save user data (json files)
    directory = "C:/University/Semester 5/ITNE352/Project/github/-ITNE352-Project-Group-B11-/json"

    file_name = client_name+'_'+option+'_B11'

    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  



if __name__ == "__main__":
    start_server()







