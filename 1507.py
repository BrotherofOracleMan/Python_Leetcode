class Solution:
    def reformatDate(self, date: str) -> str:
        day,month,year = date.split()
        month_dict = {"Jan":"01", 
                      "Feb":"02", 
                      "Mar":"03", 
                      "Apr":"04", 
                      "May":"05", 
                      "Jun":"06", 
                      "Jul":"07", 
                      "Aug":"08", 
                      "Sep":"09", 
                      "Oct":"10", 
                      "Nov":"11", 
                      "Dec":"12"
                      }
        day = "0"+ day[:1] if len(day) == 3 else day[:2]
        return "{}-{}-{}".format(year,month_dict[month],day) 
