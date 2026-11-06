import time
import shutil
import json
import os

arquivo='temas.txt'

try:
	with open(arquivo,'r',encoding='utf-8')as f:
		temas = json.load(f)

except FileNotFoundError:
	temas={}
largura = shutil.get_terminal_size().columns

while True:
	os.system('clear')
	print(f"\n{'Opções:':-^{largura}}\n \n{'0 : Sair':^{largura}}\n{'1 : Excluir tema':^{largura}}\n{'2 : Adicionar':^{largura}}\n")
	k=3
	print("Temas:".center(largura,'-'))
	print('')
	for i in temas:
		print(f"{k} : {i}\n".center(largura))
		k+=1
	print(''.center(largura,'-'))

	try:
		resposta_user=int(input("-> "))
	except:
		os.system('clear')
		continue

	if resposta_user==0:
		os.system("clear")
		break

	if resposta_user==1:
		while True:
			j=1
			os.system("clear")
			print("Opções: ".center(largura,'-'))
			print('')
			print("0 : Voltar".center(largura))

			for tema in temas:
				print(f'{j} : {tema}'.center(largura))
				j+=1
			print('')


			try:
				acao=int(input(f"{'Qual tema deseja apagar?':-^{largura}}\n-> "))
			except:
				os.system('clear')
				continue

			if acao-1 not in range(len(temas)) and acao!=0:
				os.system('clear')
				print(f"{str(acao) + ' é um numero invalido':^{largura}}")
				time.sleep(2)
				os.system('clear')
				break

			if acao==0:
				os.system('clear')
				break
			os.system("clear")
			print(f"\n{'Deseja apagar o tema: '+list(temas)[acao-1]+'?':-^{largura}} ")
			print("1 : Sim".center(largura))
			print(f"0 : Não\n".center(largura))
			print(''.center(largura,'-'))

			try:
				permissao=int(input("-> "))

			except:
				os.system('clear')
				continue

			if permissao==1:
				os.system('clear')
				print(f"\n{'Tema '+list(temas)[acao-1]+' apagado':^{largura}}\n")
				temas.pop(list(temas)[acao-1])
				time.sleep(2)
				os.system('clear')
				continue
			elif permissao==0:
				os.system('clear')
				continue

			else:
				os.system('clear')
				print('Nenhuma ação feita'.center(largura))
				time.sleep(2)
				os.system('clear')
	if resposta_user==2:
		while True:
			os.system("clear")
			print('')
			print(f"{'Qual tema deseja adicionar?':-^{largura}}\n")

			try:
				tema_adicionar=input(f"Digite o tema ou 0 para voltar -> ")
			except:
				os.system('clear')
				continue

			if len(tema_adicionar)==1 and '0' in tema_adicionar:
				os.system('clear')
				break

			print(f"\n{'Deseja adicionar '+tema_adicionar+' aos Temas?':-^{largura}}\n")

			try:
				add_ok=int(input(f"{'1 : Sim':^{largura}}\n{'0 : Não':^{largura}}\n\n{'':-^{largura}}\n-> "))
			except:
				os.system('clear')
				continue

			if add_ok==1:
				temas.setdefault(tema_adicionar,[])
				os.system("clear")

				break
			else:
				os.system("clear")

				break


	if resposta_user-3 in range(len(temas)):
		while True:
			os.system("clear")
			print(f"\n{'Opções:':-^{largura}}\n \n{'0 : Voltar':^{largura}}\n{'1 : Adicionar repertorio':^{largura}}\n{'2 : Excluir repertorio':^{largura}}")
			print(f"\n{'Repertorios do tema '+list(temas)[resposta_user-3]+':':-^{largura}}\n")
			h=3
			for tema in temas[list(temas)[resposta_user-3]]:
				print(f"{str(h)+' : '+tema:^{largura}}\n")
				h+=1
			print(''.center(largura,'-'))
			try:
				repertorio_ok=int(input("-> "))
			except:
				os.system('clear')
				continue

			if repertorio_ok==0:
				os.system("clear")

				break

			elif repertorio_ok==1:
				os.system('clear')

				try:
					add_repertorio=input(f"\n{'Digite o novo repertorio ou 0 para voltar:':-^{largura}}\n-> ")

				except:
					os.system('clear')
					continue

				if '0' in add_repertorio and len(add_repertorio)==1:
					continue

				try:
					add_repertorio_ok=int(input(f"\n{'Adicionar '+add_repertorio+' aos repertorios?':-^{largura}}\n\n{'1 : SIm':^{largura}}\n{'0 : Não':^{largura}}\n\n{'':-^{largura}}\n-> "))

				except:
					os.system('clear')
					continue

				if add_repertorio_ok==1:
					temas[list(temas)[resposta_user-3]].append(add_repertorio)
					os.system("clear")
					print(f"{'Repertorio '+add_repertorio+' adicionado':^{largura}}")
					time.sleep(2)
					os.system('clear')
					continue


			elif repertorio_ok==2:
				os.system('clear')
				print(f"\n{'Digite o numero da posição do repertorio a ser apagado ou 0 para voltar':-^{largura}}\n")
				t=1
				print('0 : Voltar\n'.center(largura))
				for tema in temas[list(temas)[resposta_user-3]]:
					print(f'{t} : {tema}\n'.center(largura))
					t+=1
				print(f"{'':-^{largura}}")

				try:
					remover_repertorio=int(input("-> "))
				except:
					os.system('clear')
					continue

				if remover_repertorio==0:
					os.system('clear')
					continue

				os.system('clear')

				try:
					confirmar_remocao=int(input(f"\n{'Deseja remover o repertorio '+temas[list(temas)[resposta_user-3]][remover_repertorio-1]+'?':-^{largura}}\n\n{'1 : Sim':^{largura}}\n{'0 : Não':^{largura}}\n\n{'':-^{largura}}\n->  "))
				except:
					os.system('clear')
					continue



				os.system('clear')

				if confirmar_remocao==1:
					os.system("clear")
					print(f'{"Repertorio "+temas[list(temas)[resposta_user-3]][remover_repertorio-1]+" removido":^{largura}}')
					temas[list(temas)[resposta_user-3]].pop(remover_repertorio-1)
					time.sleep(2)
					os.system('clear')
					continue
				else:
					os.system("clear")
					continue

with open(arquivo,'w',encoding='utf-8')as f:
	json.dump(temas,f,ensure_ascii=False,indent=4)
