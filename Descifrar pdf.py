import pikepdf
pdf = pikepdf.open('Caso Gap.pdf')  
## pdf = pikepdf.open('C:\\Users\Onepiece\Project py\Dialnet-TecnicasDeAutomatizacionAvanzadasEnProcesosIndustr-60.pdf')  
pdf.save('Caso Gap_new.pdf')    