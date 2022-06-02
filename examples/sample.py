import snipy

# Sample file, will be removed

inter = snipy.Interface()

while True:
    try:
        inter.recv()
    except KeyboardInterrupt:
        break
    else:
        print("Exit now..")