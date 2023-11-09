# lcars-m2-analysis
This is a template for an analysis scripts for lcars-m2

## Prerequisites
- [R](https://cran.r-project.org/)
- [R Studio](https://posit.co/download/rstudio-desktop/) or similar (optional)

#### Optional: if sodium needs compiliation:
- [libsodium](https://doc.libsodium.org/) if you need to comile the packe (e.g. on some linux distros)

## Usage
- Download your scientific dataset from the LCARS-M2 web app.
- Place the encypted dataset (`scientific_dataset.csv.enc`) in the data folder.
- Place the key files (`study.key` and `server.pub.key`) in the keys folder (you get the key file from the server admin). This encryption is an additional layer of security to ensure that (1) the files can only be read by the authorized persons. (2) It ensures that the data is valid, since decryption will fail, if the files have been hampered with (mutual authentication).
- After decryption, the decrypted file will be saved as `scientific_dataset.csv` in the data folder.
- Adjust the script as needed
- Note: all values are stored as text in the decrypted csv file. Each variable will need to be converted into the respective type as specified by the `variable_type`.
