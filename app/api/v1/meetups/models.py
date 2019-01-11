import uuid
from datetime import datetime

MEETUPS = []

class Meetup(object):
    def __init__(self, *args, **kwargs):
        self.meetups = MEETUPS

    def __repr__(self):
        return "<Meetup: {}>".format(self.title)

    def get_all_meetups(self):
        '''function to get all the meetups'''
        if len(self.meetups) == 0:
            res = {
                "message":"No meetups found",
                "status_code":404
            }
            return res
        else:
            return self.meetups

    def create_meetup(self,meetup_id,topic,time,venue,descriprion,images,tags,):
        '''a func to post a meetup by the admin'''
        meetup = {
            "created_on":datetime.now(),
            "meetup_date":time,
            "meetup_venue":venue,
            "meetup_details":descriprion,
            "images":images,
            "tag":tags,
            "meetup_topic":topic,
            "meetup_id":uuid.uuid4(),
            "rsvps":0,
        }
        self.meetups.append(meetup)

        return meetup["meetup_id"]

    def get_meetup(self,m_id):
        '''a func to get a specific meetup given the id'''
        meetup = [meetup for  meetup in self.meetups if meetup["id"]==m_id ][0]
        
        return meetup

    def get_rsvps_for_meetup(self,meetup_id):
        '''a func to get all the rsvps submitted for a specific meetup'''
        meetup = self.get_meetup(meetup_id)
        rsvps = meetup['rsvps']

        return rsvps

