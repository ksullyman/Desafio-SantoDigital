#para iniciar a aplicação use: uvicorn server:app --reload

#fastapi é o pacote, e o FastAPI é a classe do pacote 

from fastapi import FastAPI
from pydantic import BaseModel


#cnxn = pyodbc.connect(conn_str)
#cursor = cnxn.cursor()

#Modelo do produto
class Produto(BaseModel):
    nome: str
    num_produto: str
    cor: str
    preco_padrao: float

app = FastAPI()#aqui é uma instância criada para a classe FastAPI


@app.post('/produtos/')# rota, post para enviar informações
def criar_products(produto: Produto):# produt sendo tipado como produto e gerando o corpo
    try:
        query = """
            INSERT INTO Product.Produto (Nome, num_produto, Cor, preco_padrao)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(
            query,
            produto.nome,
            produto.num_produto,
            produto.Cor,
            produto.preco_padrao,
        )
        #cnxn.commit()
        return {"message": "Produto criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #return produt #rota sem parêmetro


@app.get('/produtos/')#é um mapeamento do tipo GET e ('/products') indica o caminho ou rota quer vai acionar a função
def products():
    return {'mensagem': 'produto cadastrado com sucesso!'} #rota com parâmentros nome