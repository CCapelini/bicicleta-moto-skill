from mycroft import MycroftSkill, intent_file_handler


class BicicletaMoto(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('moto.bicicleta.intent')
    def handle_moto_bicicleta(self, message):
        self.speak_dialog('moto.bicicleta')


def create_skill():
    return BicicletaMoto()

