import rauth
import time

def main():
	#locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
	locations = [(39.98,-82.98)]
	api_calls = []
	for lat,long in locations:
		params = get_search_parameters(lat,long)
		api_calls.append(get_results(params))
		#Be a good internet citizen and rate-limit yourself
		time.sleep(1.0)
		
	##Do other processing	

def get_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = "b6QDLmFXAPdYGpkhcJb_fA"
	consumer_secret = "egb22LOu9VO4g5ca0WXpkA-R8C4"
	token = "qcOKKAAJ3McnvRgPkt47LYS7nZs7tHpt"
	token_secret = "taMNb3tGNhuLCxnf7p0lfnmuf9A"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	#print request.text
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
        print data["region"]
        businesses_id =  data["businesses"][0]["id"]
	#print data
	print len(data["businesses"])

        request = session.get("https://api.yelp.com/v2/business/"+businesses_id)

        print "\n\n\n\n\n\n\n\n"
        print request.text
	
	return data
		
def get_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "Loews Hollywood Hotel"
	#params["cll"] = "{},{}".format(str(lat),str(long))
	#params["radius_filter"] = "2000"
        params["category_filter"] = "hotels"
	params["limit"] = "1"
	params["location"] = "90028"

	return params

if __name__=="__main__":
	main()
