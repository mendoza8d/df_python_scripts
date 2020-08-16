import pikepdf
pdf = pikepdf.open('10019031_Foro2_NEW.pdf')    
## pdf.save('10019031_Foro2_old.pdf', encryption=pikepdf.Encryption(owner=password, user=password, R=4)) 
## you can change the R from 4 to 6 for 256 aes encryption
no_extracting = pikepdf.Permissions(extract=False)
pdf.save('10019031_Foro2_old.pdf',encryption=pikepdf.Encryption(user="12345",owner="12345678",allow=no_extracting))