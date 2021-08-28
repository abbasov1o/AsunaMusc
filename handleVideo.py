def handleVideo():
    pass


MESSAGE_TYPE = {
    'condition': lambda message: message.video != None,
    'function': handleVideo
}
