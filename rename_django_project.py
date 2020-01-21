import argparse
import os

GLOBAL_FILES_NAME = ['manage.py', 'settings.py', 'wsgi.py', 'urls.py']


def rename_project(path, old_name, new_name):

	#Join in path
	os.chdir(path)
	file_list = os.listdir(path='.')
	
	#For rename manage.py
	for file_path in file_list:
		for name in GLOBAL_FILES_NAME:
			if file_path == name:
				file = open(file_path, 'r')
				file_text = file.read()
				file.close()

				if old_name in file_text:
					file_text = file_text.replace(old_name, new_name)
				
				file = open(file_path, 'w')
				file.write(file_text)
				file.close()

				print(file_path + ' modified')

	#For other files
	os.chdir(old_name)
	file_list = os.listdir(path='.')

	for file_path in file_list:
		for name in GLOBAL_FILES_NAME:
			if file_path == name:
				file = open(file_path, 'r')
				file_text = file.read()
				file.close()

				if old_name in file_text:
					file_text = file_text.replace(old_name, new_name)
				
				file = open(file_path, 'w')
				file.write(file_text)
				file.close()

				print(file_path + ' modified')

	#Rename folders
	os.chdir(path='..')
	os.renames(old_name, new_name)
	print(old_name + ' folder modified')
	os.chdir(path='..')
	os.renames(old_name, new_name)
	print(old_name + ' folder modified')

def main():

	parser = argparse.ArgumentParser(description='Created by Wultes [GitHub: github.com/wultes]')
	parser.add_argument('path', help='Project path [Example: /home/Wultes/RenameDjangoProject/]')
	parser.add_argument('old_name', help='Old name project !The register must match the original name of the project.')
	parser.add_argument('new_name', help='New name project')

	args = parser.parse_args()

	rename_project(args.path, args.old_name, args.new_name)


if __name__ == '__main__':
	main()
