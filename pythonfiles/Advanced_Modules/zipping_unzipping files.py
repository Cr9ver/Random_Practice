import zipfile
import shutil

# with open('file1.txt', 'w+') as file:
#     file.write("One file")

# with open('file2.txt', 'w+') as file:
#     file.write("two file")

# comp_file = zipfile.ZipFile('comp_file.zip', 'w')
# comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# zip_obj.extractall('extracted_content')
# zip_obj.close()

dir_to_zip = "C:\Users\OLAKUDA1\Documents\pythonfiles\Advanced_Modules\extracted_content"
output_filename = 'example'

shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')