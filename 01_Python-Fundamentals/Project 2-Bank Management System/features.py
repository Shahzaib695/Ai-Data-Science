def write_features():
    features = [
        "Creating Bank Account",
        "Depositing Money",
        "Withdrawing Money",
        "Seeing details",
        "Editing Details",
        "Deleting The Account"
    ]
    with open("notes.txt",'w') as n:
        n.write("\n".join(features))
def read_features():
    with open("notes.txt",'r') as n:
        content = n.read()
        print(content)
write_features()
read_features()
