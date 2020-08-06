'''
identifying photo folders on HDD

go through every folder and find potential photo folders
'''



print('scanning drive for photo folders...')
for foldername, subfolders, filenames in os.walk('C:\\'):
    num_photos = 0
    num_non_photos = 0
    for filename in filenames:
        if not filename.endswith(('.jpg', '.JPG', '.png', '.PNG')):
            num_non_photos += 1
            continue
        else:
            try:
                photo = Image.open(os.path.join(foldername, filename))
                height, width = photo.size
                if height and width > 500:
                    num_photos += 1
                else:
                    num_non_photos += 1
            except OSError:
                num_non_photos += 1
    if num_photos > num_non_photos:
        print(foldername)
