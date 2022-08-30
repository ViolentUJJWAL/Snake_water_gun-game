import random,time
from playsound import playsound

def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch('SAPI.SpVoice')
      speak.Speak(str)

while True:
	print("_______________WELCOME TO Game World_______________")
	time.sleep(0.5)
	print("Snake__Water__Gun Game")
	time.sleep(0.5)
	l=['snake','water','gun']
	sl=["s/S","w/W","g/G"]
	cp=0
	up=0
	brs=0
	rou=5
	i=0
	rl=1
	while rl==1:
		cos=input('''
			1. for 5 Round
			2. for 10 Round
			3. for Customise Round
			Q and othar means Exit
			-''')

		if cos=='1':
			rou=5
			rl=0
		elif cos=='2':
			rou=10
			rl=0
		elif cos=="3":
			rouc=int(input('Enter round :'))
			if 0<rouc<51:
				rou=rouc
				rl=0
			else:
				print('Round is over the limit')
				speak('Round is over the limit')
		else:
			yn=input('for EXIT Y/N -')
			if yn=='y' or yn=="Y":
				print('EXIT')
				exit();
	playsound("C:\\Users\\UJJWAL\\Music\\WIN_sound_effect_no_copyright(128k).mp3")
	while i<rou:
		print(f'\nRound {i+1}')
		for a in range(len(l)):
			print(f'{a+1} or {sl[a]} for {l[a]}')
			time.sleep(0.5)
		speak('snake,water,Gun')
		u=input("Enter :")
		if u=="1" or u=="2" or u=="3" or u=="s" or u=="w" or u=="g" or u=="S" or u=="W" or u=="G" :
			if u=="1" or u=="2" or u=="3":
				u=int(u)
			elif u=="s" or u=="w" or u=="g" or u=="S" or u=="W" or u=="G":
				if u=="s" or u=="S":
					u=1
				elif u=="w" or u=="W":
					u=2
				elif u=="g" or u=="G":
					u=3
			uc=l[u-1]
			print(f'Your Choice :{uc}')
			rc=random.choice(l)
			print(f"Computer choice :{rc}")
			if uc=="snake":
				if rc=='water':
					print('The snake drinks the water')
					print('--=>  you are win')
					speak('The snake drinks the water, you are win')
					time.sleep(1)
					up=up+1
				elif rc=='gun':
					print('The gun shoots the snake')
					print("--=>  computer are win")
					speak("The gun shoots the snake, computer are win")
					time.sleep(1)
					cp=cp+1
				else:
					print('--=>  both are same')
					speak('both are same')
					brs=brs+1
					time.sleep(1)
			elif uc=="water":
				if rc=='snake':
					print('The snake drinks the water')
					print('--=>  computer are win')
					speak('The snake drinks the water, computer are win')
					time.sleep(1)
					cp=cp+1
				elif rc=='gun':
					print('Gun has no effect on water')
					print("--=>  you are win")
					speak("Gun has no effect on water, you are win")
					time.sleep(1)
					up=up+1
				else:
					print('--=>  both are same')
					speak('both are same')
					brs=brs+1
					time.sleep(1)
			elif uc=="gun":
				if rc=='water':
					print('Gun has no effect on water')
					print('--=>  computer are win')
					speak("Gun has no effect on water, computer are win")
					time.sleep(1)
					cp=cp+1
				elif rc=='snake':
					print('The gun shoots the snake')
					print("--=>  you are win")
					speak("The gun shoots the snake, you are win")
					time.sleep(1)
					up=up+1
				else:
					print('--=>  both are same')
					speak('both are same')
					brs=brs+1
					time.sleep(1)
			i=i+1
		else:
			print("Wrong choice")
			speak("Wrong choice")
	print(f'\n---> Your score is {up}\n---> Computer score is {cp} \n---> {brs} times both are same')
	speak(f'Your score is {up}, Computer score is {cp}, {brs} times both are same')
	time.sleep(2)
	print("__________Thankyou for playing __________-----credited by violent ujjwal")
	speak("Thankyou for playing, credited by violent ujjwal")
	print('')
