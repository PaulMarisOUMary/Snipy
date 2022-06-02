import snipy

# Sample file, will be removed

inter = snipy.Interface()

while True:
    try:
        print(inter.recv())
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(type(e), e)
        break
inter.close()