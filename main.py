# Mail Merge Project
PLACEHOLDER = "[name]"
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    # replace the [name] placeholder with the actual name.
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        personalized_letter = letter.replace(PLACEHOLDER, stripped_name)
        # save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/{stripped_name}_invitation.txt", mode="w") as invitation:
            invitation.write(personalized_letter)
