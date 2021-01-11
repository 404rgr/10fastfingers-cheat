import re, os, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep

_WebDriver_ = './geckodriver' # path your web driver

class pausi:
	def __init__(self):
		self.tidur = raw_input("Sleep[example: 1] :: ")
		self.browser = ''
		self.check_web_driver()
		self.run()
	def get_word(self, source=''):
		regex = re.findall('<span wordnr="(.+?)" class="(highlight)?">(.+?)</span>', source)
		text = ''
		for x in regex:
			text = text+' '+x[2]
		return text.strip()+' '
	def check_web_driver(self):
		try:
			self.browser = webdriver.Firefox(executable_path=_WebDriver_)
		except Exception as e:
			print "Sepetrinya anda belum setting webdriver anda!"
			print "Baca README.md"
			exit()
	def run(self):
		try:
			tidur = int(self.tidur)
		except:
			tidur = int(0)
		size1 = [900, 555, 750, 950]
		size2 = [500, 800, 850, 860]
		self.browser.set_window_size(random.choice(size1), random.choice(size1))
		self.browser.get('https://10fastfingers.com/typing-test/indonesian')
		sleep(3)
		html_source = self.browser.page_source
		texts = self.get_word(html_source)
		# pausi.git@gmail.com
		sp = texts.split(' ')
		element = self.browser.find_element_by_xpath('//*[@id="inputfield"]')
		# # element.send_keys(str(texts))
		# counts = 1
		for spl in sp:
			# print counts
			# if counts == 80:
			# 	exit()
			# 	break
			# else:
				# counts +=1
				# element.send_keys(str(spl))
				print spl
				lst = list(spl)
				for t in lst:
					element.send_keys(str(t))
				sleep(tidur)
				element.send_keys(str(' '))
print '*'*40+'''
	https://github.com/404rgr/10fastfingers-cheat
	10fastfingers.com Cheat
	dikodekan oleh Zeerx7
	pada 11-01-2021
'''+'*'*40
pausi()
