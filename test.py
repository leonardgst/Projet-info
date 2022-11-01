from datetime import datetime


dateNaissance = "12/11/1999"
dateNaissance = datetime.strptime(dateNaissance, "%d/%m/%Y")
print(dateNaissance)

