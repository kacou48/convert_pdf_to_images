from pdf2image import convert_from_path

poppler_path = r"poppler-0.68.0/bin" #je defini un chemin relatif
images = convert_from_path('pdf_name.pdf', poppler_path=poppler_path) # nom du pdf et le chemin du poppler

x = 1
for image in images:
    print('processing...')
    image.save(f'images/output{x}.png', 'PNG') # enregistrer dans un dossier image
    x +=1
    print(f'page {x-1}')

print("execution terminée")