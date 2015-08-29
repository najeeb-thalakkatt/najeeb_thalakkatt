__author__ = 'NajeebT'

import uuid


class Movie(object):

    """
    This class will have all the details of a movie
    """

    def __init__(self, name, run_time, language, lead_actor, genre):
        """
        :param name:
        :param run_time:
        :param language:
        :param lead_actor:
        :param genre:
        :return:
        """
        self.id = str(uuid.uuid1())
        self.name = name
        self.run_time = run_time
        self.language = language
        self.lead_actor = lead_actor
        self.genre = genre
