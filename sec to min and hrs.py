class Time:
    
    # Method to convert seconds into minutes
    def toMinutes(self, seconds):
        return seconds // 60
    
    # Method to convert seconds into hours
    def toHours(self, seconds):
        return seconds // 3600


# Main program
seconds = int(input().strip())

obj = Time()

minutes = obj.toMinutes(seconds)
hours = obj.toHours(seconds)

print(minutes)
print(hours)
