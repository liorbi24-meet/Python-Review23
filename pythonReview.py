import bonus

def getTitle():
	print("say title:")
	return bonus.getAudio()

def getDiscription():
	print("say discription: ")
	return bonus.getAudio()

def create_youtube_video(title, description):
	hashtags = []
	for i in range(5):
		hashtags.append(input("enter a hashtag: \n"))
	return {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}, "hashtag" : hashtags}


def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video	

def add_comment(youtubevideo, username, comment_text):
	if "comments" in youtubevideo:
		youtubevideo["comments"][username] = comment_text
	return youtubevideo

def similarity_to_video(vid1, vid2):
	counter = 0
	for i in vid1[hashtags]:
		for j in vid2[hashtags]:
			if i == j:
				counter += 1
	return str((counter / 5) * 100) + '%'  

def main():
	title = getTitle()
	discription = getDiscription()
	youtube_video = create_youtube_video(title, discription)
	for i in range(456):
		youtube_video = like(youtube_video)
	print(youtube_video)

if __name__ == "__main__":
	main()