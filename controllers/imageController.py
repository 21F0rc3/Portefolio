from controllers.controllerImports import *

"""
    Cria uma imagem na base de dados e insere no diretorio de imagens
"""
def createImage(request):
    file = request.files['image']
    file.save(os.path.join(app.config['IMAGES_FOLDER'], file.filename))
    
    newImage = image(image_file=file.filename)

    db.session.add(newImage)
    db.session.commit()

    return redirect(url_for('admin'))

"""
    Retorna o url de um id de imagem
"""
def readImage(image_id):
    image_name = image.query.filter_by(id=image_id).first().image_file

    return url_for('static', filename='images/'+image_name)

"""
    Atualiza os dados de uma imagem na base de dados e no diretorio
"""
def updateImage(request):
    """
        @TODO

        Basicamente elimina uma imagem e cria outra
    """

    return redirect(url_for('admin'))

"""
    Elimina uma imagem da base de dados e do diretorio
"""
def deleteImage(image_id):
    deleteImage = image.query.filter_by(id=image_id).first()

    try:
        os.remove(os.path.join(app.config['IMAGES_FOLDER'], deleteImage.image_file))
    except:
        print("Não foi possivel eliminar a imagem. A imagem não existe. Contudo, foi corrigido na base de dados")

    db.session.delete(deleteImage)
    db.session.commit() 

    return redirect(url_for('admin'))

