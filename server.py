from flask import jsonify,request
from init import app,db,ma
from models import *;

@app.route('/marcas',methods=['GET'])
def listarMarcas():
    marcas=Marca.query.all()
    if marcas:
        resposta=marcas_schema.dump(marcas)
        return jsonify(resposta),200
    else:
        return errorHandler("Não existe marca cadastrada")

@app.route('/marcas',methods=['PUT'])
def atualizarMarca():
    id_marca=request.json['id_marca']
    nome=request.json['nome']
    if id_marca and nome:
        marca=Marca.query.get(id_marca)
        if marca:
            marca.nome=nome
            db.session.commit()
            return marca_schema.jsonify(marca),200
        else:
            return errorHandler('Marca não encontrada')
    else:
        return errorHandler('Erro na atualização - Sem dados de marca/nome')

@app.route('/marcas/<id_marca>',methods=['GET'])
def localizarMarcaPorID(id_marca):
    marca=Marca.query.get(id_marca)
    if marca:
        return marca_schema.jsonify(marca),200
    else:
        return errorHandler("Marca não encontrada")
@app.route('/marcas', methods=['POST'])
def inserirMarca():
    nome=request.json['nome']
    if nome:
        marca=Marca(nome=nome)
        db.session.add(marca)
        db.session.commit()
        return marca_schema.jsonify(marca),200
    else:
        errorHandler('Erro na inserção - Sem dados de nome')

@app.route('/perfumes',methods=['POST'])
def inserirPerfume():
    nome_perfume=request.json['nome']
    id_marca=request.json['id_marca']
    if nome_perfume and id_marca:
        marca=Marca.query.get(id_marca)
        if marca:
            perfume=Perfume(nome=nome_perfume,id_marca=id_marca)
            db.session.add(perfume)
            db.session.commit()
            return perfume_schema.jsonify(perfume),200
        else:
            return errorHandler('Marca não existe')
    else:
        return errorHandler('Requisição Incompleta - Faltam dados de descrição e marca')
    
@app.route('/essencias',methods=['POST'])
def inserirEssencia():
    descricao=request.json['descricao']
    if descricao:
        essencia=Essencia(descricao=descricao)
        db.session.add(essencia)
        db.session.commit()
        return essencia_schema.jsonify(essencia),200
    else:
        return errorHandler("Erro Inserindo Essencia")
@app.route('/perfumes/essencias',methods=['POST'])
def inserirEssenciaPerfume():
    id_perfume=request.json['id_perfume']
    id_essencia=request.json['id_essencia']
    if id_essencia and id_perfume:
        perfume=Perfume.query.get(id_perfume)
        if perfume:
            essencia=Essencia.query.get(id_essencia)
            if essencia:
                perfume.essencias.append(essencia)
                db.session.commit() #Confirma todas as alterações realizadas no objeto
                return perfume_schema.jsonify(perfume),200
            else:
                return errorHandler("Essencia não cadastrada")
        else:
            return errorHandler("Perfume não cadastrado")
    else:
        return errorHandler('Não informado Id do Perfume e da Essencia')        
def errorHandler(error):
    if error:
        resposta={
            'mensagem':error
        }
    else:
        resposta={
            'mensagem':'Erro Processando Solicitação'
        }
    return jsonify(resposta),404        

if (__name__=='__main__'):
    app.run()