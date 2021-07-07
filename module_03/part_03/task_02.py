def count_word(string):
	punctuation = ['.',',','-','!']
	list_word = []

	for i in punctuation:
		string = string.replace(i,'')

	string = string.replace('  ',' ')
	words = string.split(' ')

	for w in words:
		if len(w) < 5 and w not in list_word:
			list_word.append(w)
	return list_word


string = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градиций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с ума, то ли я - того...
На столе записка от нее смятая
Ты знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

print(count_word(string)) 