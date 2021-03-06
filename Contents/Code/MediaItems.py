class ProgrammeLatestEpisode:

	id = ""
	date = ""
	time = ""
	
	def __init__(self, id = None, date = None, time = None):
	
		self.id = id
		self.date = date
		self.time = time


class ProgrammeAdditionalInfo:

	text = ""
	uri = ""
	episodeCount = ""
	additionHeaderText = ""
	additionalSynopsisText = ""
	channel = ""

	def __init__(self, 
		text = None,
		uri = None,
		episodeCount = None,
		additionHeaderText = None,
		additionalSynopsisText = None,
		channel = None
	):
		self.text = text
		self.uri = uri
		self.episodeCount = episodeCount
		self.additionHeaderText = additionHeaderText
		self.additionalSynopsisText = additionalSynopsisText
		self.channel = channel


class Programme:

	id = ""
	title = ""
	pageUri = ""
	imageUri = ""
	genres = ""
	shortSynopsis = ""
	longSynopsis = ""
	latestEpisode = ProgrammeLatestEpisode()
	additionalInfo = ProgrammeAdditionalInfo()

	def __init__(self, 
		id = None,
		title = None,
		pageUri = None,
		imageUri = None,
		genres = None,
		shortSynopsis = None,
		longSynopsis = None,
		additionInfoText = None,
		additionInfoUri = None,
		additionInfoEpisodeCount = None,
		additionHeaderText = None,
		additionalSynopsisText = None,
		channel = None,
		latestEpisodeId = None,
		latestEpisodeDate = None,
		latestEpisodeTime = None
	):
		self.id = id
		self.title = title
		self.pageUri = pageUri
		self.imageUri = imageUri
		self.genres = genres
		self.shortSynopsis = shortSynopsis
		self.longSynopsis = longSynopsis
		self.latestEpisode = ProgrammeLatestEpisode(id=latestEpisodeId,date=latestEpisodeDate,time=latestEpisodeTime)
		self.additionalInfo = ProgrammeAdditionalInfo(text=additionInfoText,uri=additionInfoUri,episodeCount=additionInfoEpisodeCount,additionHeaderText=additionHeaderText,additionalSynopsisText=additionalSynopsisText,channel=channel)

	def summary(self):
		return self.shortSynopsis +'\n\n' + 'Last Shown: ' + self.latestEpisode.date + ' ' + self.latestEpisode.time

	def toXML(self):
		XML = "<EPISODE>"
		XML += createXMLString(self.id,"ID")
		XML += createXMLString(self.title,"TITLE")
		XML += createXMLString(self.pageUri,"PAGEURI")
		XML += createXMLString(self.imageUri,"IMAGEURI")
		XML += "</EPISODE>"
		
		return XML


class EpisodeAdditionalInfo:

	channel = ""
	channelLogoUrl = ""

	def __init__(self, channel = None, channelLogoUrl = None):
	
		self.channel = channel
		self.channelLogoUrl = channelLogoUrl


class EpisodeDenton:

	dentonId = ""
	customerRating = ""

	def __init__(self, dentonId = None, customerRating = None):
		self.dentonId = dentonId
		self.customerRating = customerRating


class Episode:

	id = ""
	title = ""
	seasonNumber = ""
	episodeNumber = ""
	genres = ""
	duration = ""
	lastBroadcast = ""
	lastBroadcastTime = ""
	daysRemaining = ""
	shortSynopsis = ""
	LongSynopsis = ""
	posterFrameUri = ""
	additionalInfo = EpisodeAdditionalInfo()
	denton = EpisodeDenton()

	def __init__(self, 
		id = None, 
		title = None,
		seasonNumber = None,
		episodeNumber = None,
		genres = None,
		duration = None,
		lastBroadcast = None,
		lastBroadcastTime = None,
		daysRemaining = None,
		shortSynopsis = None,
		LongSynopsis = None,
		posterFrameUri = None,
		channel = None,
		channelLogoUrl = None,
		dentonId = None,
		customerRating = None
	):

		self.id = id
		self.title = title
		self.seasonNumber = seasonNumber
		self.episodeNumber = episodeNumber
		self.genres = genres
		self.duration = duration
		self.lastBroadcast = lastBroadcast
		self.lastBroadcastTime = lastBroadcastTime
		self.daysRemaining = daysRemaining
		self.shortSynopsis = shortSynopsis
		self.LongSynopsis = LongSynopsis
		self.posterFrameUri = posterFrameUri
		self.additionalInfo = EpisodeAdditionalInfo(channel=channel,channelLogoUrl=channelLogoUrl)
		self.denton = EpisodeDenton(dentonId=dentonId,customerRating=customerRating)
		
	def titleDisplay(self):
		title = self.title
		if self.seasonNumber and self.episodeNumber:
			title += ' (Season: ' + self.seasonNumber + ", Ep: " + self.episodeNumber +")"
		return title
		
	def summary(self):
		summary = ''
		if self.shortSynopsis:
			summary += self.shortSynopsis
		if self.daysRemaining:
			summary += '\n\nDays Remaining: ' + self.daysRemaining
		return summary
		
	def subtitle(self):
		return self.lastBroadcast
		
	def durationMilliseconds(self):
		if self.duration:
			return int(self.duration) * 60 * 1000
		else:
			return None

###################################################
#Helper Methods
###################################################
def createXMLString(VALUE,TAG): 
	if VALUE != None:
		XML = "<"+TAG+">"+VALUE+"</"+TAG+">"
	else:
		XML = "</"+TAG+">"
	return XML