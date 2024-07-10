def cadastro():
	# Dados do livro
	t = input('Titulo do livro: ')
	a = input('Autor do livro: ')
	while True:
		try:	
			p = int(input('Ano de publicação: '))
			break
		except ValueError:
			print('ERRO. Insira um valor válido.')
	while True:
		try:	
			c = int(input('Número de cópias disponíveis: '))
			break
		except ValueError:
			print('ERRO. Insira um valor válido.')
	# Cadastro
	with open("teste93.txt", "a") as file:
		file.write(f'{t}:{a}:{p}:{c}\n')
	print('Livro cadastrado!')

def consulta():
	while True:
		print(""" Insira o modo da busca
	[ 1 ] Título
	[ 2 ] Autor
	[ 3 ] Ano de publicação
	[ 4 ] Sair""" )
		o = input('Insira a opção: ')
		if o == "1":
			# Solicitação em input do title do livro
			tb = input('Insira o título que deseja consultar: ')
			# Consulta pelo livro
			with open("teste93.txt", "r") as file:
				linhas = file.readlines()
				for i, linha in enumerate(linhas):
					t, a, p, c = linha.strip().split(':')
					if tb == t:
						# Exibição
						print('-='*30)
						print(f'Título do livro: {t}')
						print(f'Autor do livro: {a}')
						print(f'Ano de publicação: {p}')
						print(f'Número de cópias disponíveis: {c}')
						print('-='*30)
						break
					else:
						print('-='*30)
						print('Livro não encontrado!')
						print('-='*30)
						break
		if o == "2":
			# Solicitação em input do autor do livro
			au = input('Insira o autor do livro que deseja consultar: ')
			# Consulta pelo livro
			with open("teste93.txt", "r") as file:
				linhas = file.readlines()
				for i, linha in enumerate(linhas):
					t, a, p, c = linha.strip().split(':')
					if au == a:
						# Exibição
						print('-='*30)
						print(f'Título do livro: {t}')
						print(f'Autor do livro: {a}')
						print(f'Ano de publicação: {p}')
						print(f'Número de cópias disponíveis: {c}')
						print('-='*30)
						break
					else:
						print('-='*30)
						print('Livro não encontrado!')
						print('-='*30)
						break
		if o == "3":
			# Solicitação em input do ano de publicação do livro
			ano = input('Insira o ano de publicação do livro que deseja consultar: ')
			# Consulta pelo livro
			with open("teste93.txt", "r") as file:
				linhas = file.readlines()
				for i, linha in enumerate(linhas):
					t, a, p, c = linha.strip().split(':')
					if ano == p:
						# Exibição
						print('-='*30)
						print(f'Título do livro: {t}')
						print(f'Autor do livro: {a}')
						print(f'Ano de publicação: {p}')
						print(f'Número de cópias disponíveis: {c}')
						print('-='*30)
						break
					else:
						print('-='*30)
						print('Livro não encontrado!')
						print('-='*30)
						break
		if o == "4":
			print('Encerrando...')
			break

def emprestimo():
	# Solicitação ao usuário enviar o título do livro
	l = input('Insira o livro que deseja pegar: ')
	#Busca pelo livro
	with open('teste93.txt', "r") as file:
		linhas = file.readlines()
		for i, linha in enumerate(linhas):
			# t = title, a = autor, p = ano de publicação, c = número de cópias
			t, a, p, c = linha.strip().split(':')
			valor = c
			if l == t:
				# Exibição
				print(f'''
	[ Nome do livro ] : {t}
	[ Autor do livro ] : {a}
	[ Ano de publicação ] : {p}
	[ Número de cópias ] : {c}''')
				# Solicitação ao usuário enviar a quantidade que deseja pegar
				q = int(input('Insira a quantidade que deseja pegar: '))
				valor = int(valor)
				# Subtração do valor total - quantidade que o usuário pegou
				s = valor - q
				if q < valor:
					# Abre o arquivo e reescreve as informações agora com a quantidade de livros alterada
					with open('teste93.txt', "w") as file:
						file.write(f'{t}:{a}:{p}:{s}\n')
					print('Pego com sucesso')
				else:
					print('Nao é possivel pegar um número maior do que a quantidade total.')

def devolucao():
	title = input('Insira o título do livro: ')
	with open('teste93.txt', 'r') as file:
		linhas = file.readlines()
		for i, linha in enumerate(linhas):
			t, a, p, q = linha.strip().split(':')
			if title == t:
				print('\nLIVRO ENCONTRADO')
				print(f'''
	Título: {t}
	Autor: {a}
	Ano de lançamento: {p}
	Quantidade: {q}''')
				quantidade = int(input('Insira a quantidade que deseja devolver: '))
				q = int(q)
				s = quantidade + q
				with open('teste93.txt', 'w') as file:
					file.write(f'{t}:{a}:{p}:{s}')
				print('Devolvido com sucesso!')
				
# Menu		
def main():
	while True:
		print("""
	[ 1 ] Cadastro de livros
	[ 2 ] Consulta de livros
	[ 3 ] Empréstimo de livros
	[ 4 ] Devolução de livros
	[ 5 ] Sair""")
		o = input('Insira a opção: ')
		if o == "1":
			cadastro()
		elif o == "2":
			consulta()
		elif o == "3":
			emprestimo()
		elif o == "4":
			devolucao()
		elif o == "5":
			break
main()
