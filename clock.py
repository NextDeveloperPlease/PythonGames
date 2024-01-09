class time:
    def __init__(self):
        self.hour = 0
        self.minutes = 0
    
    def get_time(self):
        return [self.hour, self.minutes]
    
    def convert(duration):
        hour = duration // 60
        minutes = duration % 60
        return [hour, minutes]

    def update(self, duration): #duration is in minutes
        self.hour = self.hour + duration // 60
        self.minutes = (self.minutes + duration) % 60
        print(f'Hours: {self.hour}\nMinutes: {self.minutes}')
    