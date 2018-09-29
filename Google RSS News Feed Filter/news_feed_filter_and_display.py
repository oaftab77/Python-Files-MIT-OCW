import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# DO NOT CHANGE
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

class NewsStory(object):  
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate
        



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

class PhraseTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger.lower()
    def get_trigger(self):
        return self.trigger
    def is_phrase_in(self, text):
        flag = False
        var = self.trigger
        text = text.lower()
        text_new = ""
        trigger_no_spaces = var.replace(" ", "")
        for char in text:
            if char.isalpha() or char == " ":
                text_new = text_new + char 
        while text_new.count("  ") > 0:
            text_new = text_new.replace("  ", " ")
        text_new = text_new + " "
        if (self.trigger + " ") in text_new or (trigger_no_spaces in text_new and trigger_no_spaces not in text):
            flag = True
        return flag


class TitleTrigger(PhraseTrigger):
    
    def evaluate(self, NewsStory):
        title = NewsStory.get_title()
        return self.is_phrase_in(title)
        


class DescriptionTrigger(PhraseTrigger):
    
    def evaluate(self, NewsStory):
        description = NewsStory.get_description()
        return self.is_phrase_in(description)

# TIME TRIGGERS

# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time_string):
        temp_time = datetime.strptime(time_string, "%d %b %Y %H:%M:%S")
        self.time = temp_time.replace(tzinfo = None)

# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        key_time = NewsStory.get_pubdate()
        key_time = key_time.replace(tzinfo = None)
        if  key_time < self.time:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        key_time = NewsStory.get_pubdate()
        key_time = key_time.replace(tzinfo = None)
        if key_time > self.time:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):        
        return (not self.trigger.evaluate(story))
        

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger_boolean1, trigger_boolean2):
        self.trigger1 = trigger_boolean1
        self.trigger2 = trigger_boolean2
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) and self.trigger2.evaluate(story))

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger_boolean1, trigger_boolean2):
        self.trigger1 = trigger_boolean1
        self.trigger2 = trigger_boolean2
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) or self.trigger2.evaluate(story))
#======================
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered_stories.append(story)
                
    
    return filtered_stories



#======================
# User-Specified Triggers
#======================
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    
    temp = []
    final_list = []
    dict_temp = {}
    
    for command in lines:
        temp = command.split(",")
        if temp[1] == "TITLE":
            dict_temp[temp[0]] = (TitleTrigger(temp[2]))
        elif temp[1] == "DESCRIPTION":
            dict_temp[temp[0]] = (DescriptionTrigger(temp[2]))
        elif temp[1] == "AFTER":
            dict_temp[temp[0]] = (AfterTrigger(temp[2]))
        elif temp[1] == "BEFORE":
            dict_temp[temp[0]] = (BeforeTrigger(temp[2]))
        elif temp[1] == "NOT":
            dict_temp[temp[0]] = (NotTrigger(dict_temp[temp[2]]))
        elif temp[1] == "AND":
            dict_temp[temp[0]] = (AndTrigger(dict_temp[temp[2]], dict_temp[temp[3]]))
        elif temp[1] == "OR":
            dict_temp[temp[0]] = (OrTrigger(dict_temp[temp[2]]), dict_temp[temp[3]])
        if temp[0] == "ADD":
            n = 0
            for i in range(len(temp) - 1):
                final_list.append(dict_temp[temp[n + 1]])
    return final_list

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    # print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
# =============================================================================
#         t1 = TitleTrigger("election")
#         t2 = DescriptionTrigger("Trump")
#         t3 = DescriptionTrigger("Clinton")
#         t4 = AndTrigger(t2, t3)
#         triggerlist = [t1, t4]
# =============================================================================

        #DO NOT CHANGE THIS NEXT LINE
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

