# while loop break
name = str();

while True:
    name =  input("Enter name: ");
    if name == "":
        print("Please enter a name");
    elif name == "Sean":
        print("Hello, Sean. You are amazing");
        break;
    else:
        print("Hello, ", name);
        break;