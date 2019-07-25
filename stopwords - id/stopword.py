# 
# Melakukan Proses Stopword Removal
# Dan Menambah Stoplist 
# Dengan Python Sastrawi


# import StopWordRemoverFactory class
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
 
factory = StopWordRemoverFactory()

# Menambah Stopword 
more_stopword = ['dengan', 'saya']
data = factory.get_stop_words()+more_stopword

stopword = factory.create_stop_word_remover()
# Kalimat
kalimat = 'dengan menggunakan python dan library sastrawi saya dapat melakukan proses stopword removal'
stop = stopword.remove(kalimat)
print(stop)