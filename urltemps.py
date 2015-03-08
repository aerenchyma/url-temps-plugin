import requests # if we can't do this there needs to be more code; can we do this?

class UrlTemps(object):
	def __init__(self, agentConfig,checksLogger,rawConfig):
		self.agentConfig = agentConfig # expecting this to be a string that is comma-separated, e.g. url1,url2,url3
		self.checksLogger = checksLogger
		self.rawConfig = rawConfig # assume these 2nd two go with the territory?

	def manage_url(self,url):
		sub_dict_url = {}
		response = requests.get(url)
		resp = response.json() # this is a Python dict
		#sub_dict_url['name'] = resp["name"]
		keyname_one = "{}_{}".format(resp["name"],resp["sensor"][0]["label"].replace(" ","-"))
		keyname_two = "{}_{}".format(resp["name"],resp["sensor"][1]["label"].replace(" ","-"))
		sub_dict_url[keyname_one] = resp["sensor"][0]["tempf"]
		sub_dict_url[keyname_two] = resp["sensor"][1]["tempf"]
		return sub_dict_url

	def run(self):
		agentconfig_list = self.agentConfig.split(",")
		data = {}
		for url in agentconfig_list:
			data[url] = self.manage_url(url)
		return data

