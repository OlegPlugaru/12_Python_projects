import PyPDF2


# Open the PDF file
file = open("python101/upwork/DIRECTORIO_2022.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(file)

# Initialize variables to store the information
companies = []

# Loop through each page of the PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    print(page.extract_text())

    # Split the text into lines
    lines = page.extract_text().split("\n")

    # Loop through each line
    for line in lines:
        company = {}
        if "A" in line:

            company["Company name"] = line.split("  ")[0].strip()
            print(company["Company name"])
        elif "Sector:" in line:
            company["Sector"] = line.split(":")[1].strip()
        elif "Phone/fax:" in line:
            company["Phone/fax"] = line.split(".")[1].strip()
        if "www" in line:
            company["www"] = line.split(".")[0].strip()
        if "E-mail:" in line:
            company["Company email"] = line.split(":")[1].strip()
        elif "Number of employees:" in line:
            company["Number of employees"] = line.split(":")[1].strip()
        elif "Contacts information:" in line:
            company["Contacts information"] = line.split(":")[1].strip()

        # If all the information has been collected for a company, add it to the list of companies
        if len(company) == 7:
            companies.append(company)
file.close()
# Write the information to an Excel file
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write the header row
worksheet.append(
    [
        "Company name",
        "Sector",
        "Phone/fax",
        "www",
        "Company email",
        "Number of employees",
        "Contacts information",
    ]
)

# Write the data for each company
for company in companies:
    worksheet.append(
        [
            company["Company name"],
            company["Sector"],
            company["Phone/fax"],
            company["Website url"],
            company["Company email"],
            company["Number of employees"],
            company["Contacts information"],
        ]
    )

# Save the Excel file
workbook.save("companies.xlsx")

# Close the PDF file
file.close()
