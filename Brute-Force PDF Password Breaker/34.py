#python3! - write a program that will decrypt the PDF by trying
# every possible English word until it finds one that works.

# I've tried fixing this program with PyPDF2 same as it's suggested in the book but I
# failed to do so, from what I read is because they haven't upgraded PyPDF2 for a long time

import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("dictionary.txt")] #load password list

for password in tqdm(passwords, "Decrypting PDF"): #iterate over passwords
    try:
        with pikepdf.open('encrypted.pdf', password=password) as pdf: #open pdf file
            print("Password found", password.lower())#password decrypted succesfully
            break

    except pikepdf._qpdf.PasswordError as e:
        continue #if wrong password, continue in the loop
