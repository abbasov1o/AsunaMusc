def handleAudioMessage():
    pass


MESSAGE_TYPE = {
    'condition': lambda message: message.voice != None,
    'function': handleAudioMessage
}
