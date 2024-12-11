import google.generativeai as genai
import os
import openpyxl
import openpyxl.workbook
import random
import time

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
def process(file):
    retry = 2
    while retry > 0:
        try:
            myfile = genai.upload_file("./" + file)
            result = model.generate_content(
            [myfile, "\n\n", "Can you make this code better only replying with the new code?"]
        )
            with open("./" + file, "w") as text_file:
                text_file.write(result.text)
            retry = 0
        except Exception as e:
            retry = retry - 1
            print(f"\033[1;31mAn exception occurred: {e}. Retrying in 2 seconds...\033[0m")
            time.sleep(2)
start_time = time.time()
workbook = openpyxl.load_workbook("filesWithSmells.xlsx")
sheet = workbook.active
cols = sheet.columns
responses = []
for col in range(1,18):
    colValues = []
    for row in sheet:
        if row[col].value != 'NA':
            colValues.append(row[col].value)
    if len(colValues) < 21:
        responses = responses + colValues
    else:
        choices = random.choices(colValues, k=22)
        responses = responses + choices
setFiles = set(responses)

for (index, file) in enumerate(setFiles):
    file_time = time.time()
    process(file)
    print(str(index) + ". " + str(time.time() - file_time) + " seconds")
    time.sleep(5)
print("script finished in: " + str(time.time() - start_time) + " seconds")
