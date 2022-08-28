from mycroft import MycroftSkill, intent_file_handler


class SignalBeamChangelightstoyellow(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('changelightstoyellow.beam.signal.intent')
    def handle_changelightstoyellow_beam_signal(self, message):
        self.speak_dialog('changelightstoyellow.beam.signal')


def create_skill():
    return SignalBeamChangelightstoyellow()

