class Solution:
    def checkIPv4address(self,IP: str) -> str:
        vals = IP.split(".")
        for val in vals:
            if len(val) == 0 or len(val) > 3:
                return "Neither"
                
            if (len(val) > 1 and val[0] == '0') or not val.isdigit() or int(val) > 255:
                return "Neither"
        return "IPv4"
    
    def checkIPv6address(self, IP:str) -> str:
        vals = IP.split(":")
        allowedcharacters = "1234567890abcdefABCDEF"
        for val in vals:
            if len(val) == 0 or len(val) > 4:
                return "Neither"
            if not all([c in allowedcharacters for c in val]):
                return "Neither"
        return "IPv6"
    
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3:
            return self.checkIPv4address(IP)
        elif IP.count(":") == 7:
            return self.checkIPv6address(IP)
        else:
            return "Neither"
