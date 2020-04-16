import pyautogui as pa
import time

pa.hotkey('win')
time.sleep(1)
pa.typewrite("google chrome")
pa.hotkey('enter')
time.sleep(2)

for counter in range (0,6):
	pa.typewrite("ecosia.org")
	pa.hotkey('enter')
	time.sleep(2)
	pa.typewrite("ads")
	pa.hotkey('enter')
	time.sleep(2)
	pa.click()
	pa.hotkey('ctrl', 't')




