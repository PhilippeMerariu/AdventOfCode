file = open('input2.txt')
line = file.readline()

safe_levels = 0
bad_reports = []

def isSafe(lvls):
    slope = 0
    for i in range(len(lvls)-1):
        if sorted(lvls) == lvls:
            slope = 1
        elif sorted(lvls, reverse=True) == lvls:
            slope = -1
        else:
            return False
        if abs(lvls[i] - lvls[i+1]) < 1 or abs(lvls[i] - lvls[i+1]) > 3:
            return False
    return True

while line:
    levels = line.strip('\n').split(' ')
    levels = [int(x) for x in levels]
    if isSafe(levels) :
        safe_levels += 1
    else:
        bad_reports.append(levels)
    line = file.readline()
file.close()

for report in bad_reports:
    orig_report = report.copy()
    for k in range(len(report)):
        report = orig_report.copy()
        report.pop(k)
        if isSafe(report):
            safe_levels += 1
            break

print(f"ANSWER = {safe_levels}")

# less than 446
