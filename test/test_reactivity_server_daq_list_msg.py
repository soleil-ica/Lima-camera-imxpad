#client example
import socket
import time
import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.16.6.150', 3456))
client_socket.settimeout(1)
my_list = ['GetDetectorStatus']
while 1:
    try :
        print "---------------------"
        for msg in my_list:
            data_out = msg
            wait_time_ms = 10.0
            time.sleep(float(wait_time_ms/1000.0))#wait 
            print "wait", wait_time_ms, "ms"
            start_time = time.time()
            client_socket.send((data_out).encode())
            horodatage = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]#microsec, [:-3] #millis
            print "["+horodatage+"]" + " >> : " + data_out               
            data_in = client_socket.recv(1024)
            elapsed_time = (time.time() - start_time)*1000
            print "elapsed time is %.3f (ms)" %(elapsed_time)
            horodatage = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]#microsec, [:-3] #millis
            print "["+horodatage+"]" + " << : " + data_in  
    except socket.timeout as e:
        data_in = ""
        print(e)    
    
client_socket.close()    
