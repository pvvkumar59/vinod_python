import socket

# def localhostname():
#     localhost = socket.gethostname()
#     local_ip = socket.gethostbyname(localhost)
#     print("local hostname is: {} and ip is: {} ".format(localhost,local_ip))
#
# def remotehostname():
#     r_host = ["google.com", "facebook.com", "twitter.com"]
#     # r_host = raw_input("enter input: ")
#     for i in r_host:
#         r_ipadd = socket.gethostbyname(i)
#         try:
#             print ("remote ip_add is: {}".format(r_ipadd))
#         except socket.error, err_msg:
#             print("error")
#
# def banner_grabbing():
soc = socket.socket()
# ip_ad = "192.168.40.1"
# port = 139
soc.connect(("192.168.2.27", 139))
print (soc.recv(1000))
# soc.close()


# localhostname()
# remotehostname()
# banner_grabbing()