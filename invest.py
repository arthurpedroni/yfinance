import invest as yf
import matplotlib.pyplot as plt

# Defina os símbolos das ações que você deseja obter dados
symbols = ['PETR4.SA', 'VALE3.SA','ABEV3.SA','BBAS3.SA','BBDC4.SA','POMO3.SA','RAPT4.SA','ITUB4.SA','B3SA3.SA','EMBR3.SA','VIVT3.SA','PETZ3.SA','OIBR3.SA','CMIG4.SA','GGBR4.SA','SUZB3.SA','ITSA4.SA','SAPR4.SA','CLSC4.SA','AZUL4.SA']

# Lista para armazenar os dados históricos de cada ação
historical_data = []

# Obtenha os dados históricos de cada ação
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='12mo')
    historical_data.append(data)

# Plotagem dos preços de fechamento
plt.figure(figsize=(10, 6))

for i, data in enumerate(historical_data):
    plt.plot(data.index, data['Close'], label=symbols[i])

plt.title(f'Preços de Fechamento de ações')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento (BRL)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()