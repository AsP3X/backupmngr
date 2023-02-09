import json

class TimeCalculator:
    def convert_to_dhms(self, seconds):
        days = seconds // (24 * 3600)
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return {'days': int(days), 'hours': int(hours), 'minutes': int(minutes), 'seconds': int(seconds)}