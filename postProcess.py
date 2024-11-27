import google.generativeai as genai
import os
import openpyxl
import openpyxl.workbook

# genai.configure(api_key="AIzaSyDcWMI2YvyzmzqCibVOFYNN3hc2BzMG1Ls")
# myfile = genai.upload_file("/Users/eduardoleite/Documents/projects/testSmellsC/testSmellsC/repos/libdb/test/micro/source/b_latch.c")

# model = genai.GenerativeModel("gemini-1.5-flash")
# # response = model.generate_content("Write a story about a magic backpack.")
# result = model.generate_content(
#     [myfile, "\n\n", "Can you make this code better only replying with the new code?"]
# )
# print(result)
# with open("Output.c", "w") as text_file:
#     text_file.write(result.text)
# file_name = myfile.name
# myfile = genai.get_file(file_name)
# print(myfile)
# print(response.text)
workbook = openpyxl.load_workbook("filesWithSmells.xlsx")
sheet = workbook.active
cols = sheet.columns
newWorkBook = openpyxl.Workbook()
newSheet = newWorkBook.active
responses = []
for col in range(1,18):
    print(col)
    colValues = []
    for row in sheet:
        if row[col].value != 'NA':
            colValues.append(row[col].value)
    newSheet.append(colValues)
    print("type:" + str(colValues[0]))
    print(len(colValues))

newWorkBook.save("final2.xlsx")
# print(namesFiltered)
