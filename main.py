age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

total_wks = 90 * 52
current_age_wks = int(age) * 52

result = total_wks - current_age_wks

print(f"You have {result} weeks left.")
