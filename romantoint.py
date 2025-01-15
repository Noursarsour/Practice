def romanToInt(s):
        dic= {
        "I": 1,
        "V": 5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000 }
        total = 0
        n = len(s)     
        for i in range(n):
            # Check if the next character exists and is larger than the current one
            if i < n - 1 and dic[s[i]] < dic[s[i + 1]]:
                total -= dic[s[i]]  # Subtract the current value
            else:
                total += dic[s[i]]  # Add the current value
        
        return total