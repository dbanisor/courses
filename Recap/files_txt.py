
""" OPENING A FILE AND READING FROM IT """

with open("example_files/text_example.txt") as file:
    content = file.read()
    print(content)

""" WRITING TO A FILE & REPLACING THE PREVIOUS CONTENT 
                    the mode "w" also creates the file if it doesn't exist. """

with open("example_files/text_example.txt", "w") as file:
    file.write("A fourth line.")

""" WRITING TO A FILE & ADDING NEW CONTENT """

with open("example_files/text_example.txt", "a") as file:
    file.write("\nA fourth line.")
