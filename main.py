# Mail Merge Project
# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    # replace the [name] placeholder with the actual name.
    new_letter = letter.read()
    for name in names_list:
        stripped_name = name.strip("\n")
        personalized_letter = new_letter.replace("name", stripped_name)
        # save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/{stripped_name}_invitation.txt", mode="w") as invitation:
            invitation.write(personalized_letter)
