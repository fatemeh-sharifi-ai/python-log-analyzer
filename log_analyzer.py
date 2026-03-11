from datetime import datetime

def parse_timestamp(time_str):
    formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M;%S.%f", "%Y/%m/%d %H:%M:%S"]
    for fmt in formats:
        try:
            return datetime.strptime(time_str, fmt)
        except ValueError:
            continue
    return None 

def analyze_logs(filename, threshold=3, time_window=60):
    failedcounts={}
    failedtimes={}
    
    try:
        with open(filename, "r", encoding="utf-8-sig") as file:
            for line in file:
                line=line.strip()
                
                if not line: 
                    continue
                parts=line.split(" - ")
                
                if len(parts) != 3:
                    continue
                time_str=parts[0].strip()
                ip=parts[1].strip()
                action=parts[2].strip()
                
                timestamp = parse_timestamp(time_str)
                
                if timestamp is None:
                    continue
                if action== "login failed":
                    failedcounts[ip]=failedcounts.get(ip, 0)+1
                    failedtimes.setdefault(ip, []).append(timestamp)
        print("Failed login counts:")
        for ip,count in failedcounts.items():
            print(f"{ip}: {count}")
            
        print("\nSuspicious IPs:")
        suspicious_found= False
        
        for ip,count in failedcounts.items():
            if count>=threshold:
                print(f"{ip} -> {count} failed attempts")
                suspicious_found= True
        if not suspicious_found:
            print("No suspicious activity detected.")
            
        if failedcounts:
            top_ip=max(failedcounts, key=failedcounts.get)
            print("\nTop attacking IP:")
            print(f"{top_ip} -> {failedcounts[top_ip]} failed attempts")
        
        print("\nBrute-force analysis:")
        brute_force_found= False
        
        for ip, times in failedtimes.items():
            times.sort()
            
            for i in range(len(times) - threshold + 1):
                delta=(times[i + threshold - 1] - times[i]).total_seconds()
                
                if delta <= time_window:
                    print("Possible brute-force attack detected")
                    print(f"IP: {ip}")
                    print(f"Failures: {threshold}")
                    print(f"Within seconds: {int(delta)}\n")
                    brute_force_found= True
                    break
        if not brute_force_found:
            print("No brute-force pattern detected.")
            
    except FileNotFoundError:
        print("Error: log file not found.")
        
def main():
    filename= input("Enter log file name: ")
    analyze_logs(filename)
    
main()