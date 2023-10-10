
class Camera:

    name, wired, microphone, mp, resolutions, usb_type = None, None, None, None, None, None
    resolutions_amount = None

    def __init__(self, name, wired, microphone, mp, resolutions, usb_type):
        self.name = name
        self.wired = wired
        self.microphone = microphone
        self.mp = mp
        self.resolutions = resolutions
        self.usb_type = usb_type
        self.resolutions_amount = len(resolutions)

def convector(data):
    result = []

    for item in data:
        info = str(item)[6:-8]
        name, parameters = info.split(" [")
        parameters = parameters.split(", ")
        if parameters[1] != "микрофон": parameters = parameters[:1] + ["нет микрофона"] + parameters[1:]
        result.append(Camera(name, parameters[0], parameters[1], parameters[2], parameters[3:-1], parameters[-1]))
    
    return result