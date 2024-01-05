import myChatGPT
import newsMethods

COMPANY_NAME = "Apple"
STOCK_SYMBOL = "AAPL"

# scarica news da finviz, restituisce un pandas dataframe
news_df = newsMethods.get_news(STOCK_SYMBOL)
title_df = news_df.Title # solo i titoli
url_df = news_df.Link # solo gli url

# testo da far precedere a tutti gli articoli per spiegare a ChatGPT cosa fare
intro = "ti fornisco in inglese una notizia di finanza e voglio una sentiment analisys del test a riguardo del titolo di " + COMPANY_NAME + " rappresentato con un valore reale compreso tra -1 e 1. Isola all'interno del testo solo le parti che parlano di " + COMPANY_NAME + ", non mi interessano le altre aziende coinvolte. Voglio solo ed esclusivamente il numero compreso fra -1 e 1 come risposta, non parole. Ecco la notizia:\n"

intro_debug = "ti fornisco in inglese una notizia di finanza e voglio una sentiment analisys del test a riguardo del titolo di " + COMPANY_NAME + " rappresentato con un valore reale compreso tra -1 e 1. Isola all'interno del testo solo le parti che parlano di " + COMPANY_NAME + ", non mi interessano le altre aziende coinvolte. Rispondimi con la valutazione fra -1 e 1 e con una brevissima spiegazione. Ecco la notizia: \n"

# definizione oggetto di classe myChatGPT
interpreter = myChatGPT.myChatGPT(company_name=COMPANY_NAME, stock_sym=STOCK_SYMBOL)

for i in range(3):
    url = url_df[i]
    text = newsMethods.extract_text(url) # ottiene il testo
    print (title_df[i]) # stampa il solo titolo dell'articolo
    # print(text) # stampa tutto il testo: puo' essere molto lungo
    
    message = intro_debug + text # assembla il messaggio da dare a ChatGPT
    interpreter.send(message=message) # invia a ChatGPT
    print("\n")
    
# della stampa della sentiment si occupa la classe myChatGPT
# attenzione perche' non salva i risultati su file, vanno copiati a mano se si vogliono salvare!
