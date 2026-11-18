from status import kontrollera_status
#testing
print("Test 1:", kontrollera_status("up"))
print("Test 2:",kontrollera_status("down"))
print("Test 3:",kontrollera_status("unknown"))

print("Test 4:",kontrollera_status("fel") == False)#printing invalid status
