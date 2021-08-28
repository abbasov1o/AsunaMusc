def handleAudioFile():
    pass


MESSAGE_TYPE = {
    'condition': lambda message: message.audio != None,
    'function': handleAudioFile
}
