try:
    f=open("pramod.txt")
    try:
        f.write("wadakjlksanlkjsaj")
    except:
        print("something went wrong")
    finally:
        f.close
except:
    print("file is not show")