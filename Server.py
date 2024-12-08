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
        print('='*30)
        print(f"Accepted connection from {client_name}")
        
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=client_handling, args=(client_socket, client_name))
        client_thread.start()

def client_handling(client_socket, client_name):
    API = "9d73eeefa6dc4ec8a2fe74a16501503d"
    try:
        while True:
            request = client_socket.recv(2048).decode("utf-8")
            # check if the request was to disconnect connection
            if request == 'quit':
                break  # Client disconnected
            # check if the request was for headlines
            if request[:4] == 'head':
                url = 'https://newsapi.org/v2/top-headlines'
                # check what menu option the user chose to search by for headlines
                if request[5:12] == 'keyword':
                    params = {
                        "q":request[13:], 
                        "apiKey": API
                    }
                elif request[5:13] == 'category':
                    params = {
                        "category": request[14:], 
                        "apiKey": API 
                    }
                elif request[5:12] == 'country':
                    params = {
                        "country": request[13:], 
                        "apiKey": API
                    }
                else:
                    params = {
                        "apiKey": API,
                        "language": "en"
                    }

                response = requests.get(url,params=params)

                save_json(response.json(),client_name,request)
                print('='*30)
                print("The requester name:" , client_name)
                print("Option: Source")
                print("Request parameters:", request)

                if response.status_code == 200:
                    client_socket.send(response.text.encode("utf-8"))
                else:
                    client_socket.send(f"API Error: {response.status_code}".encode("utf-8"))
            
            
            # Check if the client wanted to search by sources
            elif request[:6] == 'source':
                url = 'https://newsapi.org/v2/top-headlines/sources'

                # check what menu option the client wanted to search by for sources

                if request[7:15] == 'category':
                    params = {
                        "category":request[16:], 
                        "apiKey": API
                    }
                elif request[7:14] == 'country':
                    params = {
                        "country": request[15:], 
                        "apiKey": API
                    }
                elif request[7:15] == 'language':
                    params = {
                        "language": request[16:], 
                        "apiKey": API
                    }
                else:
                    params = {
                        "apiKey": API,
                    }

                response = requests.get(url,params=params)

                save_json(response.json(),client_name,request[7:])
                print('='*30)
                print("The requester name:" , client_name)
                print("Option: Source")
                print("Request parameters:", request)

                if response.status_code == 200:
                        client_socket.send(response.text.encode("utf-8"))
                else:
                    client_socket.send(f"API Error: {response.status_code}".encode("utf-8"))

            # if it was something else, in this case quit. We terminate the connection
            

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print(client_name,"connection closed.")

def save_json(data,client_name,option):
    current_directory = os.getcwd()

    directory = os.path.join(current_directory, "json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f"{client_name}_{option}_B11.json"

    file_path = os.path.join(directory, file_name)

    with open(file_path, 'w') as file:
        json.dump(data, file)



if __name__ == "__main__":
    start_server()







