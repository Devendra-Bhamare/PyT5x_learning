# write a code to ask the user which browser he wants to run automation

browser_name = input("Write a browser name\n")
match browser_name:
    case "firefox":
        print("started the b")
    case "chrome":
        print(" the b")
    case "edge":
        print("started the b")

    case _:
        print("not found")
