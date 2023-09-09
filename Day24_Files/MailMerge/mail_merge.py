
with open("./Names/invited_names.txt") as names:
    invited_names = names.read().split("\n")

with open("./Letter/letter.txt") as letter:
    invite_letter = letter.read()

for name in invited_names:
    with open(f"./Output/letter_to_{name}.txt", mode="w") as out_letter:
        out_letter.write(invite_letter.replace("[name]", name.strip()))

