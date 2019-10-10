import PIL
import appex
import console
import sys

def main():
	img = None
	args = sys.argv
	if appex.is_running_extension():
		img = appex.get_image()
	else:
		print('running in Pythonista, using test image.')
		img = PIL.Image.open('test:Mandrill')
		
	if img != None:
		print(img)
		i0 = img.resize((1600,1600), PIL.Image.ANTIALIAS)
		i0.show()
		print('1600x1600')
		i1 = img.resize((800,800), PIL.Image.ANTIALIAS)
		i1.show()
		print('800x800')
		i2 = img.resize((112,112), PIL.Image.ANTIALIAS)
		i2.show()
		print('112x112')
		i3 = img.resize((56,56), PIL.Image.ANTIALIAS)
		i3.show()
		print('56x56')
		i4 = img.resize((28,28), PIL.Image.ANTIALIAS)
		i4.show()
		print('28x28')

if __name__ == '__main__':
	main()
