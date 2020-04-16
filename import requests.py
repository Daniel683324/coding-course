import requests, bs4

for movie_num in range(1900, 2300):
	url = 'https://cineplex.com.au/movie/' + str(movie_num)



	res = requests.get(url)

	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	body = soup.body

	try:
	h2_item = body.select(".movie-header > h2")
	h2_item_str = str(h2_item)[4:-5]

	except:
	print ('something went wrong')
	else:	
	print (h2_item_str)

print ('and this is to go even further beyond')

# print (str(h2_item) [4:-4])
# with open('result.txt', 'w+') as file:
# 	file.write(h2_item_str)
