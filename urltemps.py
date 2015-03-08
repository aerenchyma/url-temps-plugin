import requests # if we can't do this there needs to be more code; can we do this?

class UrlTemps(object):
	def __init__(self, agentConfig,checksLogger,rawConfig):
		self.agentConfig = agentConfig # expecting this to be a string that is comma-separated, e.g. url1,url2,url3
		self.checksLogger = checksLogger
		self.rawConfig = rawConfig # assume these 2nd two go with the territory?

	def manage_url(self,url):
		sub_dict_url = {}
		#response = requests.get(url)
		#resp = response.json() # this is a Python dict
		test_data = {"name":"RA3E-124804","date":"03/07/15 22:24:08","uptime":"0d 22:28:37","scale":0,"macaddr":"00:80:A3:93:AA:CF","serial":"RA3E-124804","devtype":85,"refresh":"60","disp":0,"interval":"300","version":"v1.2.1","port":80,"ip":"192.168.5.181","sensor":[{"label":"Sensor 1","tempf":"75.20","tempc":"24.00","highf":"81.05","highc":"27.25","lowf":"39.86","lowc":"4.37","alarm":0,"type":16,"enabled":1},{"label":"Sensor 2","tempf":"32.00","tempc":"0.00","highf":"32.00","highc":"0.00","lowf":"32.00","lowc":"0.00","alarm":0,"type":0,"enabled":0}],"switch_sen":[{"label":"Sensor 3","enabled":1,"alarm":1,"status":0}]}
		resp = test_data
		#sub_dict_url['name'] = resp["name"]
		keyname_one = "{}_{}".format(resp["name"],resp["sensor"][0]["label"].replace(" ","-"))
		keyname_two = "{}_{}".format(resp["name"],resp["sensor"][1]["label"].replace(" ","-"))
		sub_dict_url[keyname_one] = float(resp["sensor"][0]["tempf"])
		sub_dict_url[keyname_two] = float(resp["sensor"][1]["tempf"])
		return sub_dict_url

	def run(self):
		agentconfig_list = self.agentConfig.split(",")
		data = {}
		for url in agentconfig_list:
			data[url] = self.manage_url(url)
		return data # a Python dictionary with key:val pairs url:dictionary with the sensor temps

####

test_data = {"name":"RA3E-124804","date":"03/07/15 22:24:08","uptime":"0d 22:28:37","scale":0,"macaddr":"00:80:A3:93:AA:CF","serial":"RA3E-124804","devtype":85,"refresh":"60","disp":0,"interval":"300","version":"v1.2.1","port":80,"ip":"192.168.5.181","sensor":[{"label":"Sensor 1","tempf":"75.20","tempc":"24.00","highf":"81.05","highc":"27.25","lowf":"39.86","lowc":"4.37","alarm":0,"type":16,"enabled":1},{"label":"Sensor 2","tempf":"32.00","tempc":"0.00","highf":"32.00","highc":"0.00","lowf":"32.00","lowc":"0.00","alarm":0,"type":0,"enabled":0}],"switch_sen":[{"label":"Sensor 3","enabled":1,"alarm":1,"status":0}]}
x = UrlTemps("test,testx,testy","test2","test3")
print x.run()