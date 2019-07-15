import os

# Function to rename multiple files
def main():
    # ask user for some info about photos on run.
    print("Please follow the instructions below. You will be asked some "
          "identifying info about your photos. If you do not know or "
          "wish not to fill it out, just press ENTER without leaving a "
          "response. The only required question is the first one. Once"
          "you have filled out a response, press ENTER to submit it.")
    directory = str(input("Please enter the directory of your photos"))
    location = input("Please enter the location where these photos were taken.")
    date = input("Please enter the date when these photos were taken.")
    credit = input("What are the initials of the photographer?")

    i = 0
    for filename in os.listdir(directory):
        newName = directory + "/" + str(location) + str(date) + str(credit) + str(i) + ".jpg"
        oldName = directory + "/" + filename

        os.rename(oldName, newName)
        i += 1
    print("Done!")

if __name__ == '__main__':
    main()
