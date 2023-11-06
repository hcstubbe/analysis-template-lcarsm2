# lcars-m2-analysis
This is a template for an analysis scripts for lcars-m2

## Prerequisites
- [R](https://cran.r-project.org/)
- [R Studio](https://posit.co/download/rstudio-desktop/) or similar (optional)
- For decryption (only required once for each dataset):
  - [Python](https://www.python.org/) start.

## Usage
- Download your scientific dataset from the LCARS-M2 web app.
- Place the encypted dataset (`scientific_dataset.csv.enc`) in the data folder.
- Place the key files (`study.key` and `server.pub.key`) in the keys folder (you get the key file from the server admin). This is encryption is an additional layer of security to ensure that (1) the files can only be read by the authorized persons. (2) It ensures that the data is valid, since decryption will fail, if the files have been hampered with (mutual authentication).
- After decryption, the decypted file will be saved as `scientific_dataset.csv` in the data folder.
- Run the script file.
- Adjust the script as needed
- Note: all values are stored as text int the decrypted csv file. Each variable will need to be converted into te respective type as specified by the `variable_type`.
