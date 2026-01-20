import re
import matplotlib.pyplot as plt

file = open("mbox.txt", 'r')

months = [0]
days = [0]

for line in file:
    line = line.strip()

    new_email = re.search(r'^From\s+\S+\s+(\w{3})\s+(\w{3})', line)

    if new_email:
        day = new_email.group(1)
        month = new_email.group(2)

        days.append(day)
        months.append(month)

file.close()

plt.figure()
plt.hist(months, bins=len(set(months)))
plt.xlabel('Months')
plt.ylabel('Number of Emails')
plt.title('Emails Sent by Month')
plt.show()

plt.figure()
plt.hist(days, bins=len(set(days)))
plt.xlabel('Days')
plt.ylabel('Number of Emails')
plt.title('Emails Sent by Day')
plt.show()
