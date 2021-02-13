import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('''მოგესალმებით დროის მანქანაში
ეს არის Facebook -ის დორის მანქანა შეიყვანთ
ჩატის ბმულს, თარიღს და თქვენ დაბრუნდებით უკან!
''')

mobile_facebook_url = 'https://m.facebook.com/messages/read/?fbid={}&_rdr&last_message_timestamp={}&pagination_direction=1&show_delete_message_button&refid=12'
get_fb_id = lambda x: (x.split('.com/t/')[1] if '/' not in x.split('.com/t/')[1] else x.split('.com/t/')[1].split('/')[0])
url_is_correct = lambda x: (x if '://messenger.com/t/' in x or '://www.messenger.com/t/' in x else False)

def run():
	url = url_is_correct(input('(?) გთხოოვთ შეიყვანოთ Messenger -ის ბმული: '))
	if url:
		fb_id = get_fb_id(url)
		try:
			year = int(input('(?) შეიყვანეთ წელი: '))
			month = int(input('(?) შეიყვანეთ თვე: '))
			day = int(input('(?) შეიყვანეთ დღე: '))

			timestamp = int(time.mktime((year, month, day, 8, 44, 4, 4, 362, 0)))
			print('\nთუ ამ ტექსტს ხედავ ესეიგი ბმულის გენერირება\nწარმატებით დასრულდა! ეწვიეთ ქვემოთ მითითებულ\nბმულს და ნახეთ წარსული ;))\n\nბმული: %s' % mobile_facebook_url.format(fb_id, timestamp)) 
		except ValueError:
			print('\n(~) გთხოოვთ შეიყვნოთ რიცხები')
			sys.exit(0)
	else:
		print('(~) გთხოოვთ შეიყვანოთ სწორი ბმული')
		sys.exit(0)

if __name__ == '__main__':
	try:
		run()
	except KeyboardInterrupt:
		print('\n(!) დაფიქსირდა CTRL + C')
		sys.exit(0)
	except Exception as e:
		print('\n(~) შეცდომა: %s' % e) 