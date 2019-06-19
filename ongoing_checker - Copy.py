import os.path, json, telegram
from jikanpy import Jikan

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
jk = Jikan()


def list_creator():
	list = []
	for i in days:
		schedule = jk.schedule(i)
		for j in schedule[i]:
			list.append(j['mal_id'])
	return list

def json_write(file_name, list):
        with open(file_name, 'w') as jlist:
                json.dump(list, jlist)

def checking():

	lname="anime.json"
	initial_list=[]
	latest_list=[]
	finished_list=[]
	token = 'TOKEN'
	chat_id = 'CHAT_ID'
	bot = telegram.Bot(token)

	if os.path.exists(lname) :
		with open(lname) as jlist:
			initial_list = json.load(jlist)
		latest_list = list_creator()
		finished_list = set(initial_list) - set(latest_list)
	
		if finished_list == set():
			exit()
		else:
			for i in finished_list:
				temp = jk.anime(i)
				bot.sendMessage(chat_id, 'The anime : {} with MAL id : {} has finished airing'.format(temp['title'], temp['mal_id']))
		json_write(lname, latest_list)
		exit()

	else:
		initial_list = list_creator()
		json_write(lname, initial_list)
		exit()

if __name__ == '__main__':
	checking()

