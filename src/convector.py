
class Camera:

    name, wired, microphone, mp, resolutions, usb_type = None, None, None, None, None, None
    resolutions_amount = None

    def __init__(self, name, wired, microphone, mp, resolutions, usb_type):
        self.name = name
        self.wired = 0 if wired == "проводная" else 1
        self.microphone = 0 if microphone == "нет микрофона" else 1
        self.mp = mp.replace(' Мп', '')
        self.resolutions = 0
        self.usb_type =  int("Type-C" in usb_type) + int("USB" in usb_type) + 2 * int("jack" in usb_type)
        self.resolutions_amount = len(resolutions)
    
        for r in resolutions:
            try:
                a, b = r.split(" x ")
                self.resolutions = max(self.resolutions, int(a)*int(b))
            except ValueError:
                self.resolutions = resolutions
            


def convector(data):
    result = []

    for item in data:
        info = str(item)[6:-8]
        name, parameters = info.split(" [")
        parameters = parameters.split(", ")
        if parameters[1] != "микрофон": parameters = parameters[:1] + ["нет микрофона"] + parameters[1:]

        camera = Camera(name, parameters[0], parameters[1], parameters[2], parameters[3:-1], parameters[-1])

        result.append(camera)
    
    return result